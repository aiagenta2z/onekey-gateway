## Web Search - google-search/google-search

### Skill: google-search
#### google_search
Description: Generates google search results by calling google custom search engine API. https://www.googleapis.com/customsearch/v1
            
        Args:
            query: Annotated[str, "Search Query that User Input"] = "",
            num: Annotated[int, "Return number of search results"] = 10,
            start: Annotated[str, "pagination start index of search item at the number of 0. start=0, num=10 means items from [0, 10), start=10, num=10 means items from [10, 12)"] = 0

        Return:
            results: List[Any], list of search results
## Parameters
- query: string (default: )
- num: integer (default: 10)
- start: integer (default: 0)
- return_fields: array (default: [])
##### CLI
```
onekey agent google-search/google-search google_search '{"query": "US inflation rate February 2026", "num": 5, "start": 0}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"google-search/google-search","api_id":"google_search","data":{"query": "US inflation rate February 2026", "num": 5, "start": 0}}'
```
##### MCP
```
onekey mcp google-search
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-google-search":{
      "url":"https://agent.deepnlp.org/mcp?server_name=google-search&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill google-search -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill google-search
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="google-search/google-search", api_id="google_search", data={"query": "US inflation rate February 2026", "num": 5, "start": 0})
```
