import argparse
import json
import os

from ai_agent_marketplace import OneKeyAgentRouter


def build_router():
    onekey = os.getenv("DEEPNLP_ONEKEY_ROUTER_ACCESS", "BETA_TEST_KEY_MARCH_2026")
    return OneKeyAgentRouter(onekey=onekey)

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
