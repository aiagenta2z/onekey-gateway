import argparse
import json
import os
import sys

from ai_agent_marketplace import OneKeyAgentRouter


def build_router():
    api_key = os.getenv("DEEPNLP_ONEKEY_ROUTER_ACCESS")

    if not api_key:
        print("\n" + "=" * 60)
        print("WARNING: DEMO MODE — NO API KEY SET")
        print("Using default test key (BETA_TEST_KEY_MARCH_2026)")
        print("Results may be mocked or inaccurate")
        print("Set: export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_key")
        print("=" * 60 + "\n")
        api_key = "BETA_TEST_KEY_MARCH_2026"

    return OneKeyAgentRouter(onekey=api_key)


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
    missing = [key for key in ['data'] if key not in payload]
    if missing:
        raise SystemExit(f"Missing required fields: {', '.join(missing)}")


def main():
    parser = argparse.ArgumentParser(description="mcp-server-chart generate_fishbone_diagram")
    parser.add_argument("--data", help="JSON string payload for tool input")
    parser.add_argument("--data-file", help="Path to JSON file payload")
    args = parser.parse_args()

    payload = load_payload(args)
    validate_required(payload)

    router = build_router()
    result = router.invoke(
        unique_id="mcp-server-chart/mcp-server-chart",
        api_id="generate_fishbone_diagram",
        data=payload,
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
