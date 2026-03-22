---
name: bing-image-search-mcp
description: Auto-generated skill for bing-image-search-mcp tools via OneKey Gateway.
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


# bing-image-search-mcp Skill
Use the OneKey Gateway to access tools for this server via a unified access key.
## Quick Start
Set your OneKey access key:
```bash
export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_API_KEY
```
If no key is provided, the scripts fall back to the demo key `BETA_TEST_KEY_MARCH_2026`.
Common settings:
- `unique_id`: `bing-image-search-mcp/bing-image-search-mcp`
- `api_id`: one of the tools listed below
## Tools
### `search_images`
Search Images

        Args:
            query: str, query used in Bing search engine
            limit: int, number of images information returned
  
        Return: 
            str: json str with below values samples

            [{'title': 'Italy Travel Guide: The Ultimate 2-week Road Trip · Salt in our Hair',
               'thumbnail_url': 'http://ts2.mm.bing.net/th?id=OIP.TEuPMUk1s2A3OBkq3LrTnwHaFc&pid=15.1',
               'url': 'http://ts2.mm.bing.net/th?id=OIP.TEuPMUk1s2A3OBkq3LrTnwHaFc&pid=15.1'},
              {'title': '25 Best Places to Visit in Italy (+ Map to Find Them!) - Our Escape Clause',
               'thumbnail_url': 'http://ts2.mm.bing.net/th?id=OIP.kle1eO_p_4crE4lRtWK8AgHaE8&pid=15.1',
               'url': 'http://ts2.mm.bing.net/th?id=OIP.kle1eO_p_4crE4lRtWK8AgHaE8&pid=15.1'}
               ]

Parameters:
- `query` (string, optional):
- `limit` (integer, optional):
### `search_images_batch`
Batch Method of Search Images From Bing Web Search

        Args:
            query_list: List[str], List of query used in Bing Image search engine
            limit: int, number of images information returned
  
        Return: 
            Dict: json Dict with below values samples

            [{'title': 'Italy Travel Guide: The Ultimate 2-week Road Trip · Salt in our Hair',
               'thumbnail_url': 'http://ts2.mm.bing.net/th?id=OIP.TEuPMUk1s2A3OBkq3LrTnwHaFc&pid=15.1',
               'url': 'http://ts2.mm.bing.net/th?id=OIP.TEuPMUk1s2A3OBkq3LrTnwHaFc&pid=15.1'},
              {'title': '25 Best Places to Visit in Italy (+ Map to Find Them!) - Our Escape Clause',
               'thumbnail_url': 'http://ts2.mm.bing.net/th?id=OIP.kle1eO_p_4crE4lRtWK8AgHaE8&pid=15.1',
               'url': 'http://ts2.mm.bing.net/th?id=OIP.kle1eO_p_4crE4lRtWK8AgHaE8&pid=15.1'}
               ]

Parameters:
- `query_list` (array of string, required):
- `limit` (integer, optional):

# Usage
## CLI

### search_images
```shell
npx onekey agent bing-image-search-mcp/bing-image-search-mcp search_images '{"query": "Eiffel Tower sunset", "limit": 5}'
```

### search_images_batch
```shell
npx onekey agent bing-image-search-mcp/bing-image-search-mcp search_images_batch '{"query_list": ["Eiffel Tower sunset", "Louvre at night"], "limit": 3}'
```

## Scripts
Each tool has a dedicated script in this folder:
- `skills/bing-image-search-mcp/scripts/search_images.py`
- `skills/bing-image-search-mcp/scripts/search_images_batch.py`
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
