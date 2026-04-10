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

def split_list(value):
    return [item.strip() for item in value.split(",") if item.strip()]


def main():
    parser = argparse.ArgumentParser(description="Google Maps Distance Matrix")
    parser.add_argument(
        "--origins",
        required=True,
        type=split_list,
        help="Comma-separated origins (addresses or 'lat,lon')",
    )
    parser.add_argument(
        "--destinations",
        required=True,
        type=split_list,
        help="Comma-separated destinations (addresses or 'lat,lon')",
    )
    parser.add_argument(
        "--mode",
        choices=["driving", "walking", "bicycling", "transit"],
        help="Travel mode",
    )
    args = parser.parse_args()

    payload = {"origins": args.origins, "destinations": args.destinations}
    if args.mode:
        payload["mode"] = args.mode

    router = build_router()
    result = router.invoke(
        unique_id="google-maps/google-maps",
        api_id="maps_distance_matrix",
        data=payload,
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
