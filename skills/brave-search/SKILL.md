---
name: brave-search
description: Auto-generated skill for brave-search tools via OneKey Gateway.
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

### OneKey Gateway
Use One Access Key to connect to various commercial APIs. Please visit the [OneKey Gateway Keys](https://www.deepnlp.org/workspace/keys) and read the docs [OneKey MCP Router Doc](https://www.deepnlp.org/doc/onekey_mcp_router) and [OneKey Gateway Doc](https://deepnlp.org/doc/onekey_agent_router).

# brave-search Skill
Use the OneKey Gateway to access tools for this server via a unified access key.
## Quick Start
Set your OneKey access key:
```bash
export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_API_KEY
```
If no key is provided, the scripts fall back to the demo key `BETA_TEST_KEY_MARCH_2026`.
Common settings:
- `unique_id`: `brave-search/brave-search`
- `api_id`: one of the tools listed below
``## Tools
### `brave_web_search`
Performs a web search using the Brave Search API, ideal for general queries, news, articles, and online content. Use this for broad information gathering, recent events, or when you need diverse web sources. Supports pagination, content filtering, and freshness controls. Maximum 20 results per request, with offset for pagination.

``Parameters:
- `query` (string, required): Search query (max 400 chars, 50 words)
- `count` (number, optional): Number of results (1-20, default 10)
- `offset` (number, optional): Pagination offset (max 9, default 0)
### `brave_local_search`
Searches for local businesses and places using Brave's Local Search API. Best for queries related to physical locations, businesses, restaurants, services, etc. Returns detailed information including:
- Business names and addresses
- Ratings and review counts
- Phone numbers and opening hours
Use this when the query implies 'near me' or mentions specific locations. Automatically falls back to web search if no local results are found.

Parameters:
- `query` (string, required): Local search query (e.g. 'pizza near Central Park')
- `count` (number, optional): Number of results (1-20, default 5)

# Usage
## CLI

### brave_web_search
```shell
npx onekey agent brave-search/brave-search brave_web_search '{"query": "latest AI research 2026"}'
```

### brave_local_search
```shell
npx onekey agent brave-search/brave-search brave_local_search '{"query": "coffee near Times Square"}'
```

## Scripts
Each tool has a dedicated script in this folder:
- `skills/brave-search/scripts/brave_web_search.py`
- `skills/brave-search/scripts/brave_local_search.py`
### Example
```bash
python3 scripts/<tool_name>.py --data '{"key": "value"}'
```

### Related DeepNLP OneKey Gateway Documents
[AI Agent Marketplace](https://www.deepnlp.org/store/ai-agent)    
[Skills Marketplace](https://www.deepnlp.org/store/skills)
[AI Agent A2Z Deployment](https://www.deepnlp.org/workspace/deploy)    
[PH AI Agent A2Z Infra](https://www.producthunt.com/products/ai-agent-a2z)    
[GitHub AI Agent Marketplace](https://github.com/aiagenta2z/ai-agent-marketplace)
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
