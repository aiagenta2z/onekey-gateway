#!/usr/bin/env python3

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request


def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_payload(args):
    if args.data and args.data_file:
        raise SystemExit("Use only one of --data or --data-file.")
    if args.data:
        return json.loads(args.data)
    if args.data_file:
        return read_json(args.data_file)
    return {}


def apply_query_params(url, payload):
    if not payload or not isinstance(payload, dict):
        return url
    parsed = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    for k, v in payload.items():
        if v is None:
            continue
        if isinstance(v, list):
            for item in v:
                query.append((k, str(item)))
        else:
            query.append((k, str(v)))
    new_query = urllib.parse.urlencode(query, doseq=True)
    return urllib.parse.urlunsplit(
        (parsed.scheme, parsed.netloc, parsed.path, new_query, parsed.fragment)
    )


def main():
    parser = argparse.ArgumentParser(description="Run one API from reference/api_meta.json")
    parser.add_argument("--api", required=True, help="api_id to run")
    parser.add_argument("--data", help="JSON string payload")
    parser.add_argument("--data-file", help="Path to JSON file payload")
    args = parser.parse_args()

    meta_path = os.path.join(os.path.dirname(__file__), "..", "reference", "api_meta.json")
    meta = read_json(meta_path)
    apis = meta.get("apis", {})
    api_info = apis.get(args.api)
    if not api_info:
        raise SystemExit(f"Unknown api_id: {args.api}. Known: {', '.join(apis.keys())}")

    payload = load_payload(args)
    method = str(api_info.get("method", "GET")).upper()
    endpoint = api_info.get("endpoint")
    if not endpoint:
        raise SystemExit("Missing endpoint in api_meta.json")

    headers = dict(api_info.get("headers") or {})
    auth = api_info.get("auth") or {}
    auth_header = auth.get("header")
    auth_env = auth.get("env") or auth.get("value")
    if auth_header and auth_env and os.getenv(auth_env):
        headers[auth_header] = os.getenv(auth_env)

    data_bytes = None
    url = endpoint
    if method in ("GET", "DELETE"):
        url = apply_query_params(endpoint, payload)
    else:
        headers.setdefault("Content-Type", "application/json")
        data_bytes = json.dumps(payload or {}).encode("utf-8")

    req = urllib.request.Request(url=url, method=method, headers=headers, data=data_bytes)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        sys.stderr.write(json.dumps({"status": e.code, "body": body}, indent=2, ensure_ascii=False) + "\n")
        raise SystemExit(1)


if __name__ == "__main__":
    main()

