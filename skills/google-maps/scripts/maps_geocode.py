import argparse
import json
import os

from ai_agent_marketplace import OneKeyAgentRouter


def build_router():
    onekey = os.getenv("DEEPNLP_ONEKEY_ROUTER_ACCESS", "BETA_TEST_KEY_MARCH_2026")
    return OneKeyAgentRouter(onekey=onekey)


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
