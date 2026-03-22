---
name: google-search
description: Auto-generated skill for google-search tools via OneKey Gateway.
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

# google-search Skill
Use the OneKey Gateway to access tools for this server via a unified access key.
## Quick Start
Set your OneKey access key:
```bash
export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_API_KEY
```
If no key is provided, the scripts fall back to the demo key `BETA_TEST_KEY_MARCH_2026`.
Common settings:
- `unique_id`: `google-search/google-search`
- `api_id`: one of the tools listed below
## Tools
### `google_search`
Generates google search results by calling google custom search engine API. https://www.googleapis.com/customsearch/v1
            
        Args:
            query: Annotated[str, "Search Query that User Input"] = "",
            num: Annotated[int, "Return number of search results"] = 10,
            start: Annotated[str, "pagination start index of search item at the number of 0. start=0, num=10 means items from [0, 10), start=10, num=10 means items from [10, 12)"] = 0

        Return:
            results: List[Any], list of search results

Parameters:
- `query` (string, optional):
- `num` (integer, optional):
- `start` (integer, optional):
- `return_fields` (array of object, optional):

# Usage
## CLI

### google_search
```shell
npx onekey agent google-search/google-search google_search '{"query": "US inflation rate February 2026", "num": 5, "start": 0}'
```

## Scripts
Each tool has a dedicated script in this folder:
- `skills/google-search/scripts/google_search.py`
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
