import argparse
import json
import os

from ai_agent_marketplace import OneKeyAgentRouter


def build_router():
    onekey = os.getenv("DEEPNLP_ONEKEY_ROUTER_ACCESS", "BETA_TEST_KEY_MARCH_2026")
    return OneKeyAgentRouter(onekey=onekey)

def main():
    parser = argparse.ArgumentParser(description="Google Maps Directions")
    parser.add_argument("--origin", required=True, help="Starting point address or coordinates")
    parser.add_argument("--destination", required=True, help="Ending point address or coordinates")
    parser.add_argument(
        "--mode",
        choices=["driving", "walking", "bicycling", "transit"],
        help="Travel mode",
    )
    args = parser.parse_args()

    payload = {"origin": args.origin, "destination": args.destination}
    if args.mode:
        payload["mode"] = args.mode

    router = build_router()
    result = router.invoke(
        unique_id="google-maps/google-maps",
        api_id="maps_directions",
        data=payload,
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
