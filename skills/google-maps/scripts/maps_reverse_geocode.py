import argparse
import json
import os

from ai_agent_marketplace import OneKeyAgentRouter


def build_router():
    onekey = os.getenv("DEEPNLP_ONEKEY_ROUTER_ACCESS", "BETA_TEST_KEY_MARCH_2026")
    return OneKeyAgentRouter(onekey=onekey)


def main():
    parser = argparse.ArgumentParser(description="Google Maps Reverse Geocode")
    parser.add_argument("--latitude", required=True, type=float, help="Latitude coordinate")
    parser.add_argument("--longitude", required=True, type=float, help="Longitude coordinate")
    args = parser.parse_args()

    router = build_router()
    result = router.invoke(
        unique_id="google-maps/google-maps",
        api_id="maps_reverse_geocode",
        data={"latitude": args.latitude, "longitude": args.longitude},
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
