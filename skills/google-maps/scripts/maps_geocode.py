import argparse
import json
import os

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


def main():
    parser = argparse.ArgumentParser(description="Google Maps Geocode")
    parser.add_argument("--address", required=True, help="The address to geocode")
    args = parser.parse_args()

    router = build_router()
    result = router.invoke(
        unique_id="google-maps/google-maps",
        api_id="maps_geocode",
        data={"address": args.address},
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
