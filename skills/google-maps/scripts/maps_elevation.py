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


def parse_locations(value):
    locations = []
    for chunk in value.split(";"):
        chunk = chunk.strip()
        if not chunk:
            continue
        parts = chunk.split(",")
        if len(parts) != 2:
            raise argparse.ArgumentTypeError("locations must be 'lat,lon;lat,lon'")
        locations.append({"latitude": float(parts[0]), "longitude": float(parts[1])})
    if not locations:
        raise argparse.ArgumentTypeError("at least one location is required")
    return locations


def main():
    parser = argparse.ArgumentParser(description="Google Maps Elevation")
    parser.add_argument(
        "--locations",
        required=True,
        type=parse_locations,
        help="Locations as 'lat,lon;lat,lon'",
    )
    args = parser.parse_args()

    router = build_router()
    result = router.invoke(
        unique_id="google-maps/google-maps",
        api_id="maps_elevation",
        data={"locations": args.locations},
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
