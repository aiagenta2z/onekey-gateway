## Web Search - tavily-remote-mcp/tavily-remote-mcp

### Skill: tavily-remote-mcp
#### tavily_search
Description: Search the web for current information on any topic. Use for news, facts, or data beyond your knowledge cutoff. Returns snippets and source URLs.
## Parameters
- query: string — Search query
- max_results: integer — The maximum number of search results to return (default: 5)
- search_depth: string — The depth of the search. 'basic' for generic results, 'advanced' for more thorough search, 'fast' for optimized low latency with high relevance, 'ultra-fast' for prioritizing latency above all else (default: basic)
- topic: string — The category of the search. This will determine which of our agents will be used for the search (default: general)
- time_range: string/null — The time range back from the current date to include in the search results
- include_images: boolean — Include a list of query-related images in the response (default: False)
- include_image_descriptions: boolean — Include a list of query-related images and their descriptions in the response (default: False)
- include_raw_content: boolean — Include the cleaned and parsed HTML content of each search result (default: False)
- include_domains: array — A list of domains to specifically include in the search results, if the user asks to search on specific sites set this to the domain of the site (default: [])
- exclude_domains: array — List of domains to specifically exclude, if the user asks to exclude a domain set this to the domain of the site (default: [])
- country: string — Boost search results from a specific country. This will prioritize content from the selected country in the search results. Available only if topic is general. (default: )
- include_favicon: boolean — Whether to include the favicon URL for each result (default: False)
- start_date: string — Will return all results after the specified start date. Required to be written in the format YYYY-MM-DD. (default: )
- end_date: string — Will return all results before the specified end date. Required to be written in the format YYYY-MM-DD (default: )
##### CLI
```
onekey agent tavily-remote-mcp/tavily-remote-mcp tavily_search '{"query": "NVIDIA earnings", "max_results": 5, "search_depth": "advanced"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"tavily-remote-mcp/tavily-remote-mcp","api_id":"tavily_search","data":{"query": "NVIDIA earnings", "max_results": 5, "search_depth": "advanced"}}'
```
##### MCP
```
onekey mcp tavily-remote-mcp
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-tavily-remote-mcp":{
      "url":"https://agent.deepnlp.org/mcp?server_name=tavily-remote-mcp&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill tavily-remote-mcp -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill tavily-remote-mcp
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="tavily-remote-mcp/tavily-remote-mcp", api_id="tavily_search", data={"query": "NVIDIA earnings", "max_results": 5, "search_depth": "advanced"})
```

#### tavily_extract
Description: Extract content from URLs. Returns raw page content in markdown or text format.
## Parameters
- urls: array — List of URLs to extract content from
- extract_depth: string — Use 'advanced' for LinkedIn, protected sites, or tables/embedded content (default: basic)
- include_images: boolean — Include images from pages (default: False)
- format: string — Output format (default: markdown)
- include_favicon: boolean — Include favicon URLs (default: False)
- query: string — Query to rerank content chunks by relevance (default: )
##### CLI
```
onekey agent tavily-remote-mcp/tavily-remote-mcp tavily_extract '{"urls": ["https://example.com/article"], "extract_depth": "advanced", "format": "markdown"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"tavily-remote-mcp/tavily-remote-mcp","api_id":"tavily_extract","data":{"urls": ["https://example.com/article"], "extract_depth": "advanced", "format": "markdown"}}'
```
##### MCP
```
onekey mcp tavily-remote-mcp
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-tavily-remote-mcp":{
      "url":"https://agent.deepnlp.org/mcp?server_name=tavily-remote-mcp&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill tavily-remote-mcp -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill tavily-remote-mcp
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="tavily-remote-mcp/tavily-remote-mcp", api_id="tavily_extract", data={"urls": ["https://example.com/article"], "extract_depth": "advanced", "format": "markdown"})
```

#### tavily_crawl
Description: Crawl a website starting from a URL. Extracts content from pages with configurable depth and breadth.
## Parameters
- url: string — The root URL to begin the crawl
- max_depth: integer — Max depth of the crawl. Defines how far from the base URL the crawler can explore. (default: 1)
- max_breadth: integer — Max number of links to follow per level of the tree (i.e., per page) (default: 20)
- limit: integer — Total number of links the crawler will process before stopping (default: 50)
- instructions: string — Natural language instructions for the crawler. Instructions specify which types of pages the crawler should return. (default: )
- select_paths: array — Regex patterns to select only URLs with specific path patterns (e.g., /docs/.*, /api/v1.*) (default: [])
- select_domains: array — Regex patterns to restrict crawling to specific domains or subdomains (e.g., ^docs\.example\.com$) (default: [])
- allow_external: boolean — Whether to return external links in the final response (default: True)
- extract_depth: string — Advanced extraction retrieves more data, including tables and embedded content, with higher success but may increase latency (default: basic)
- format: string — The format of the extracted web page content. markdown returns content in markdown format. text returns plain text and may increase latency. (default: markdown)
- include_favicon: boolean — Whether to include the favicon URL for each result (default: False)
##### CLI
```
onekey agent tavily-remote-mcp/tavily-remote-mcp tavily_crawl '{"url": "https://example.com", "max_depth": 1, "max_breadth": 10, "limit": 20}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"tavily-remote-mcp/tavily-remote-mcp","api_id":"tavily_crawl","data":{"url": "https://example.com", "max_depth": 1, "max_breadth": 10, "limit": 20}}'
```
##### MCP
```
onekey mcp tavily-remote-mcp
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-tavily-remote-mcp":{
      "url":"https://agent.deepnlp.org/mcp?server_name=tavily-remote-mcp&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill tavily-remote-mcp -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill tavily-remote-mcp
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="tavily-remote-mcp/tavily-remote-mcp", api_id="tavily_crawl", data={"url": "https://example.com", "max_depth": 1, "max_breadth": 10, "limit": 20})
```

#### tavily_map
Description: Map a website's structure. Returns a list of URLs found starting from the base URL.
## Parameters
- url: string — The root URL to begin the mapping
- max_depth: integer — Max depth of the mapping. Defines how far from the base URL the crawler can explore (default: 1)
- max_breadth: integer — Max number of links to follow per level of the tree (i.e., per page) (default: 20)
- limit: integer — Total number of links the crawler will process before stopping (default: 50)
- instructions: string — Natural language instructions for the crawler (default: )
- select_paths: array — Regex patterns to select only URLs with specific path patterns (e.g., /docs/.*, /api/v1.*) (default: [])
- select_domains: array — Regex patterns to restrict crawling to specific domains or subdomains (e.g., ^docs\.example\.com$) (default: [])
- allow_external: boolean — Whether to return external links in the final response (default: True)
##### CLI
```
onekey agent tavily-remote-mcp/tavily-remote-mcp tavily_map '{"url": "https://example.com/docs", "max_depth": 1, "max_breadth": 10, "limit": 30}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"tavily-remote-mcp/tavily-remote-mcp","api_id":"tavily_map","data":{"url": "https://example.com/docs", "max_depth": 1, "max_breadth": 10, "limit": 30}}'
```
##### MCP
```
onekey mcp tavily-remote-mcp
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-tavily-remote-mcp":{
      "url":"https://agent.deepnlp.org/mcp?server_name=tavily-remote-mcp&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill tavily-remote-mcp -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill tavily-remote-mcp
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="tavily-remote-mcp/tavily-remote-mcp", api_id="tavily_map", data={"url": "https://example.com/docs", "max_depth": 1, "max_breadth": 10, "limit": 30})
```

#### tavily_research
Description: Perform comprehensive research on a given topic or question. Use this tool when you need to gather information from multiple sources, including web pages, documents, and other resources, to answer a question or complete a task. Returns a detailed response based on the research findings.
## Parameters
- input: string — A comprehensive description of the research task
- model: string — Defines the degree of depth of the research. 'mini' is good for narrow tasks with few subtopics. 'pro' is good for broad tasks with many subtopics (default: auto)
##### CLI
```
onekey agent tavily-remote-mcp/tavily-remote-mcp tavily_research '{"input": "Impact of AI on healthcare", "model": "pro"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"tavily-remote-mcp/tavily-remote-mcp","api_id":"tavily_research","data":{"input": "Impact of AI on healthcare", "model": "pro"}}'
```
##### MCP
```
onekey mcp tavily-remote-mcp
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-tavily-remote-mcp":{
      "url":"https://agent.deepnlp.org/mcp?server_name=tavily-remote-mcp&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill tavily-remote-mcp -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill tavily-remote-mcp
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="tavily-remote-mcp/tavily-remote-mcp", api_id="tavily_research", data={"input": "Impact of AI on healthcare", "model": "pro"})
```
