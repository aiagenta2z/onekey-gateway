import argparse
import json
import os

from ai_agent_marketplace import OneKeyAgentRouter


def build_router():
    onekey = os.getenv("DEEPNLP_ONEKEY_ROUTER_ACCESS", "BETA_TEST_KEY_MARCH_2026")
    return OneKeyAgentRouter(onekey=onekey)


def parse_location(value):
    parts = value.split(",")
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("location must be 'lat,lon'")
    return {"latitude": float(parts[0]), "longitude": float(parts[1])}


def main():
    parser = argparse.ArgumentParser(description="Google Maps Search Places")
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument(
        "--location",
        type=parse_location,
        help="Optional center point as 'lat,lon'",
    )
    parser.add_argument(
        "--radius",
        type=float,
        help="Search radius in meters (max 50000)",
    )
    args = parser.parse_args()

    payload = {"query": args.query}
    if args.location:
        payload["location"] = args.location
    if args.radius is not None:
        payload["radius"] = args.radius

    router = build_router()
    result = router.invoke(
        unique_id="google-maps/google-maps",
        api_id="maps_search_places",
        data=payload,
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
