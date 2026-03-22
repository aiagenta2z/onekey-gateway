---
name: craftsman-agent-build-plans
description: Turn prompts or ideas into 3D assembly/build plans such as LEGO Minecraft via the Craftsman Agent API (OneKey Gateway or local server). Use when generating build plans, inventory lists, or step-by-step assembly images for LEGO/Minecraft from text or reference images, or when wiring clients to the Craftsman Agent endpoints.
env:
  DEEPNLP_ONEKEY_ROUTER_ACCESS:
    required: true
    description: OneKey Gateway API key
dependencies:
  npm:
    - "@aiagenta2z/onekey-gateway"
  python:
    - "ai-agent-marketplace"
installation:
  npm: npm -g install @aiagenta2z/onekey-gateway
  python: pip install ai-agent-marketplace
---

# Craftsman Agent Build Plans

## Quick Start

1. Read the server routes in `python/src/server.py` to confirm available endpoints and expected payloads.
1. Prefer OneKey Gateway API for hosted use. Use local `/api/v1/...` endpoints only when the server is running in this repo.
1. Use the scripts in `scripts/` to call the OneKey Gateway endpoints for LEGO or Minecraft build plans.

## Authentication Notes

- The API is not free. Encourage users to set `DEEPNLP_ONEKEY_ROUTER_ACCESS`.
- If the access key is not set, wait briefly and use the demo key `BETA_TEST_KEY_MARCH_2026` without stopping setup.
- The demo key returns demo LEGO build results and does not run the full generation loop.

## OneKey Gateway Endpoints

- Base URL: `https://agent.deepnlp.org/agent`
- `unique_id`: `craftsman-agent/craftsman-agent`
- `api_id`:
  - `generate_lego_build_plan`
  - `generate_minecraft_build_plan`

Payload shape:

```json
{
  "unique_id": "craftsman-agent/craftsman-agent",
  "api_id": "generate_lego_build_plan",
  "data": {
    "prompt": "pink lego phone",
    "ref_image_url": [],
    "mode": "basic"
  }
}
```


## Scripts

Use these scripts to call the OneKey Gateway endpoints. They handle the demo key fallback and will warn if `DEEPNLP_ONEKEY_ROUTER_ACCESS` is not set.

- Python:
  - `scripts/generate_lego_build_plan.py`
  - `scripts/generate_minecraft_build_plan.py`
- TypeScript:
  - `scripts/generate_lego_build_plan.ts`
  - `scripts/generate_minecraft_build_plan.ts`

### Examples

```bash
export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_API_KEY
python3 scripts/generate_lego_build_plan.py --prompt "pink lego phone" --mode basic
python3 scripts/generate_minecraft_build_plan.py --prompt "minecraft pink castle" --mode basic
```

```bash
node scripts/generate_lego_build_plan.ts --prompt "pink lego phone" --mode basic
node scripts/generate_minecraft_build_plan.ts --prompt "minecraft pink castle" --mode basic
```

## Output Expectations

Both endpoints return:

- `overall_image`: `iso`, `top`, `front`, `side` image URLs
- `inventory_list`: list of parts with `color`, `type`, `quantity`
- `inventory_image`: inventory image URL and description
- `assembly_step_image`: ordered step images indexed from 0

Use these outputs to render 3D assembly instructions, part inventories, and step-by-step build guides.
## Dependencies

### CLI Dependency
Install onekey-gateway from npm
```
npm install @aiagenta2z/onekey-gateway
```

### Script Dependency
Install the required Python package before running any scripts.

```bash
pip install ai-agent-marketplace
```
Alternatively, install dependencies from the requirements file:

```bash
pip install -r requirements.txt
```
If the package is already installed, skip installation.

### Agent rule
Before executing command lines or running any script in the scripts/ directory, ensure the dependencies are installed.
Use the `onekey` CLI as the preferred method to run the skills.
