## Image Search - bing-image-search-mcp/bing-image-search-mcp

### Skill: bing-image-search-mcp
#### search_images
Description: Get Public Available Stock Symbols from Global Marketplace

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
## Parameters
- query: string (default: )
- limit: integer (default: 10)
##### CLI
```
onekey agent bing-image-search-mcp/bing-image-search-mcp search_images '{"query": "Eiffel Tower sunset", "limit": 5}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"bing-image-search-mcp/bing-image-search-mcp","api_id":"search_images","data":{"query": "Eiffel Tower sunset", "limit": 5}}'
```
##### MCP
```
onekey mcp bing-image-search-mcp
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-bing-image-search-mcp":{
      "url":"https://agent.deepnlp.org/mcp?server_name=bing-image-search-mcp&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill bing-image-search-mcp -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill bing-image-search-mcp
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="bing-image-search-mcp/bing-image-search-mcp", api_id="search_images", data={"query": "Eiffel Tower sunset", "limit": 5})
```

#### search_images_batch
Description: Batch Method of Search Images From Bing Web Search

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
## Parameters
- query_list: array
- limit: integer (default: 10)
##### CLI
```
onekey agent bing-image-search-mcp/bing-image-search-mcp search_images_batch '{"query_list": ["Eiffel Tower sunset", "Louvre at night"], "limit": 3}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"bing-image-search-mcp/bing-image-search-mcp","api_id":"search_images_batch","data":{"query_list": ["Eiffel Tower sunset", "Louvre at night"], "limit": 3}}'
```
##### MCP
```
onekey mcp bing-image-search-mcp
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-bing-image-search-mcp":{
      "url":"https://agent.deepnlp.org/mcp?server_name=bing-image-search-mcp&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill bing-image-search-mcp -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill bing-image-search-mcp
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="bing-image-search-mcp/bing-image-search-mcp", api_id="search_images_batch", data={"query_list": ["Eiffel Tower sunset", "Louvre at night"], "limit": 3})
```
