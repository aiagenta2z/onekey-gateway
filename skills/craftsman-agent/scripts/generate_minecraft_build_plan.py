#!/usr/bin/env python3
"""Call Craftsman Agent OneKey Router to generate a Minecraft build plan."""

import argparse
import json
import os
import sys
import time
from urllib import request, parse, error

ENDPOINT = "https://agent.deepnlp.org/agent"
UNIQUE_ID = "craftsman-agent/craftsman-agent"
API_ID = "generate_minecraft_build_plan"
ENV_KEY = "DEEPNLP_ONEKEY_ROUTER_ACCESS"
DEMO_KEY = "BETA_TEST_KEY_MARCH_2026"


def warn_missing_key():
    sys.stderr.write(
        "DEEPNLP_ONEKEY_ROUTER_ACCESS is not set. "
        "The API is not free; using demo key after a short wait.\n"
    )
    sys.stderr.write(
        "Set with: export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_API_KEY\n"
    )
    time.sleep(2)


def build_payload(prompt, ref_image_url, mode):
    return {
        "unique_id": UNIQUE_ID,
        "api_id": API_ID,
        "data": {
            "prompt": prompt,
            "ref_image_url": ref_image_url,
            "mode": mode,
        },
    }


def post_json(url, payload):
    data = json.dumps(payload).encode("utf-8")
    req = request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with request.urlopen(req, timeout=60) as resp:
        body = resp.read().decode("utf-8")
        return resp.status, body


def main():
    parser = argparse.ArgumentParser(description="Generate Minecraft build plan via Craftsman Agent")
    parser.add_argument("--prompt", required=True, help="Text prompt for the build")
    parser.add_argument(
        "--ref-image-url",
        action="append",
        default=[],
        help="Reference image URL (repeatable)",
    )
    parser.add_argument("--mode", default="basic", help="demo|basic|standard|advanced")
    args = parser.parse_args()

    api_key = os.getenv(ENV_KEY)
    if not api_key:
        warn_missing_key()
        api_key = DEMO_KEY

    query = parse.urlencode({"onekey": api_key})
    url = f"{ENDPOINT}?{query}"

    payload = build_payload(args.prompt, args.ref_image_url, args.mode)

    try:
        status, body = post_json(url, payload)
    except error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        sys.stderr.write(f"HTTP {e.code}: {error_body}\n")
        sys.exit(1)
    except error.URLError as e:
        sys.stderr.write(f"Network error: {e.reason}\n")
        sys.exit(1)

    try:
        parsed = json.loads(body)
        print(json.dumps(parsed, indent=2))
    except json.JSONDecodeError:
        print(body)


if __name__ == "__main__":
    main()
