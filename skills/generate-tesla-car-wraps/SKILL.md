---
name: generate-tesla-car-wraps
description: Call Craftsman Agent API OneKey Router to generate Tesla Car Wrap Images and Paints that will display on 3D screen.
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

# Generate Tesla Car Wraps

Call Craftsman Agent API OneKey Router to generate Tesla Car Wrap Images and Paints that will display on 3D screen.

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
onekey agent craftsman-agent/craftsman-agent generate_tesla_wraps '{"prompt":"I would like to paint my tesla model YL similar to race car, color of a blue and purple with stars","images":[],"mode":"basic","car_model":"tesla_model_yl","output_number":1}' --timeout 30000
```

### 2. Python REST API

```bash
python3 scripts/generate_tesla_wraps.py --prompt "I would like to paint my tesla model YL similar to race car, color of a blue and purple with stars" --mode basic --car-model tesla_model_yl --output-number 1
```

### 3. TypeScript REST API

```bash
node scripts/generate_tesla_wraps.ts --prompt "I would like to paint my tesla model YL similar to race car, color of a blue and purple with stars" --mode basic --car-model tesla_model_yl --output-number 1
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
