import argparse
import json
import os
import sys

from ai_agent_marketplace import OneKeyAgentRouter


def build_router():
    onekey = os.getenv("DEEPNLP_ONEKEY_ROUTER_ACCESS")
    if not onekey:
        raise ValueError("DEEPNLP_ONEKEY_ROUTER_ACCESS environment variable is required")
    return OneKeyAgentRouter(onekey=onekey)


def load_payload(args):
    if args.data and args.data_file:
        raise SystemExit("Use only one of --data or --data-file.")
    if args.data:
        return json.loads(args.data)
    if args.data_file:
        with open(args.data_file, "r", encoding="utf-8") as f:
            return json.load(f)
    raise SystemExit("Missing input. Provide --data or --data-file.")


def validate_required(payload):
    missing = [key for key in [] if key not in payload]
    if missing:
        raise SystemExit(f"Missing required fields: {', '.join(missing)}")


def main():
    parser = argparse.ArgumentParser(description="gemini generate_image_nano_banana")
    parser.add_argument("--data", help="JSON string payload for tool input")
    parser.add_argument("--data-file", help="Path to JSON file payload")
    args = parser.parse_args()

    payload = load_payload(args)
    validate_required(payload)

    router = build_router()
    result = router.invoke(
        unique_id="gemini/gemini",
        api_id="generate_image_nano_banana",
        data=payload,
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
