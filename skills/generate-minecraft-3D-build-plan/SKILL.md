---
name: generate-minecraft-3D-build-plan
description: Call Craftsman Agent API OneKey Router to generate a Minecraft 3D scene build plan.
env:
  DEEPNLP_ONEKEY_ROUTER_ACCESS:
    required: true
    description: OneKey Gateway API key (DEEPNLP_ONEKEY_ROUTER_ACCESS)
dependencies:
  npm:
    - "@aiagenta2z/onekey-gateway"
  python:
    - "ai-agent-marketplace"
installation:
  npm: npm -g install @aiagenta2z/onekey-gateway
  python: pip install ai-agent-marketplace
---

# Generate Minecraft 3D Build Plan

Call Craftsman Agent API OneKey Router to generate a Minecraft 3D scene build plan.

## Quick Start

1. Set your environment variable `DEEPNLP_ONEKEY_ROUTER_ACCESS`.
2. Use the CLI (primary suggested method) or the provided scripts.

## Usage

### 1. CLI (Recommended)

#### CLI Illustration
```shell
onekey agent <unique_id> <api_id> $JSON --timeout 30000
```
- `<unique_id>`: the unique identifier of the onekey routed agents, "owner/repo".
- `<api_id>`: refers to the unique endpoint name of API.
- `$JSON`: the json string passed to cli.
- `--timeout`: controlls the timeout of API calling, unit is mill seconds.

#### Example
```bash
export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_ACCESS_KEY
onekey agent craftsman-agent/craftsman-agent generate_minecraft_build_plan '{"prompt":"Minecraft scene of Grassland and TNT Block, Purple Crystals","images":[],"mode":"basic"}' --timeout 30000
```

### 2. Python REST API

```bash
python3 scripts/generate_minecraft_build_plan.py --prompt "Minecraft scene of Grassland and TNT Block, Purple Crystals" --mode basic
```

### 3. TypeScript REST API

```bash
node scripts/generate_minecraft_build_plan.ts --prompt "Minecraft scene of Grassland and TNT Block, Purple Crystals" --mode basic
```

## Authentication

Remember to set the environment variable:
```bash
export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_ACCESS_KEY
```
Get your key at [DeepNLP Workspace](https://www.deepnlp.org/workspace/keys).

## Demo Result

```json
{"success":true,"text":"","images":[{"url":"https://us-static.aiagenta2z.com/local/files-wd/onekey_llm_router/efd67a8f-a427-4e56-8b00-c02d4eb332d5.png"}]}
```
