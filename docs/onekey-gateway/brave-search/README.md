## Web Search - brave-search/brave-search

### Skill: brave-search
#### brave_web_search
Description: Performs a web search using the Brave Search API, ideal for general queries, news, articles, and online content. Use this for broad information gathering, recent events, or when you need diverse web sources. Supports pagination, content filtering, and freshness controls. Maximum 20 results per request, with offset for pagination.
## Parameters
- query: string — Search query (max 400 chars, 50 words)
- count: number — Number of results (1-20, default 10) (default: 10)
- offset: number — Pagination offset (max 9, default 0) (default: 0)
##### CLI
```
npx onekey agent brave-search/brave-search brave_web_search '{"query": "latest AI research 2026"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"brave-search/brave-search","api_id":"brave_web_search","data":{"query": "latest AI research 2026"}}'
```
##### MCP
```
npx onekey mcp brave-search
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-brave-search":{
      "url":"https://agent.deepnlp.org/mcp?server_name=brave-search&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill brave-search -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill brave-search
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="brave-search/brave-search", api_id="brave_web_search", data={"query": "latest AI research 2026"})
```

#### brave_local_search
Description: Searches for local businesses and places using Brave's Local Search API. Best for queries related to physical locations, businesses, restaurants, services, etc. Returns detailed information including:
- Business names and addresses
- Ratings and review counts
- Phone numbers and opening hours
Use this when the query implies 'near me' or mentions specific locations. Automatically falls back to web search if no local results are found.
## Parameters
- query: string — Local search query (e.g. 'pizza near Central Park')
- count: number — Number of results (1-20, default 5) (default: 5)
##### CLI
```
npx onekey agent brave-search/brave-search brave_local_search '{"query": "coffee near Times Square"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"brave-search/brave-search","api_id":"brave_local_search","data":{"query": "coffee near Times Square"}}'
```
##### MCP
```
npx onekey mcp brave-search
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-brave-search":{
      "url":"https://agent.deepnlp.org/mcp?server_name=brave-search&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill brave-search -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill brave-search
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="brave-search/brave-search", api_id="brave_local_search", data={"query": "coffee near Times Square"})
```
