---
name: tavily-remote-mcp
description: Auto-generated skill for tavily-remote-mcp tools via OneKey Gateway.
---

### OneKey Gateway
Use One Access Key to connect to various commercial APIs. Please visit the [OneKey Gateway Keys](https://www.deepnlp.org/workspace/keys) and read the docs [OneKey MCP Router Doc](https://www.deepnlp.org/doc/onekey_mcp_router) and [OneKey Gateway Doc](https://deepnlp.org/doc/onekey_agent_router).


# tavily-remote-mcp Skill
Use the OneKey Gateway to access tools for this server via a unified access key.
## Quick Start
Set your OneKey access key:
```bash
export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_API_KEY
```
If no key is provided, the scripts fall back to the demo key `BETA_TEST_KEY_MARCH_2026`.
Common settings:
- `unique_id`: `tavily-remote-mcp/tavily-remote-mcp`
- `api_id`: one of the tools listed below
## Tools
### `tavily_search`
Search the web for current information on any topic. Use for news, facts, or data beyond your knowledge cutoff. Returns snippets and source URLs.

Parameters:
- `query` (string, required): Search query
- `max_results` (integer, optional): The maximum number of search results to return
- `search_depth` (string, optional): The depth of the search. 'basic' for generic results, 'advanced' for more thorough search, 'fast' for optimized low latency with high relevance, 'ultra-fast' for prioritizing latency above all else Values: basic, advanced, fast, ultra-fast
- `topic` (string, optional): The category of the search. This will determine which of our agents will be used for the search
- `time_range` (object, optional): The time range back from the current date to include in the search results
- `include_images` (boolean, optional): Include a list of query-related images in the response
- `include_image_descriptions` (boolean, optional): Include a list of query-related images and their descriptions in the response
- `include_raw_content` (boolean, optional): Include the cleaned and parsed HTML content of each search result
- `include_domains` (array of string, optional): A list of domains to specifically include in the search results, if the user asks to search on specific sites set this to the domain of the site
- `exclude_domains` (array of string, optional): List of domains to specifically exclude, if the user asks to exclude a domain set this to the domain of the site
- `country` (string, optional): Boost search results from a specific country. This will prioritize content from the selected country in the search results. Available only if topic is general.
- `include_favicon` (boolean, optional): Whether to include the favicon URL for each result
- `start_date` (string, optional): Will return all results after the specified start date. Required to be written in the format YYYY-MM-DD.
- `end_date` (string, optional): Will return all results before the specified end date. Required to be written in the format YYYY-MM-DD
### `tavily_extract`
Extract content from URLs. Returns raw page content in markdown or text format.

Parameters:
- `urls` (array of string, required): List of URLs to extract content from
- `extract_depth` (string, optional): Use 'advanced' for LinkedIn, protected sites, or tables/embedded content Values: basic, advanced
- `include_images` (boolean, optional): Include images from pages
- `format` (string, optional): Output format Values: markdown, text
- `include_favicon` (boolean, optional): Include favicon URLs
- `query` (string, optional): Query to rerank content chunks by relevance
### `tavily_crawl`
Crawl a website starting from a URL. Extracts content from pages with configurable depth and breadth.

Parameters:
- `url` (string, required): The root URL to begin the crawl
- `max_depth` (integer, optional): Max depth of the crawl. Defines how far from the base URL the crawler can explore.
- `max_breadth` (integer, optional): Max number of links to follow per level of the tree (i.e., per page)
- `limit` (integer, optional): Total number of links the crawler will process before stopping
- `instructions` (string, optional): Natural language instructions for the crawler. Instructions specify which types of pages the crawler should return.
- `select_paths` (array of string, optional): Regex patterns to select only URLs with specific path patterns (e.g., /docs/.*, /api/v1.*)
- `select_domains` (array of string, optional): Regex patterns to restrict crawling to specific domains or subdomains (e.g., ^docs\.example\.com$)
- `allow_external` (boolean, optional): Whether to return external links in the final response
- `extract_depth` (string, optional): Advanced extraction retrieves more data, including tables and embedded content, with higher success but may increase latency Values: basic, advanced
- `format` (string, optional): The format of the extracted web page content. markdown returns content in markdown format. text returns plain text and may increase latency. Values: markdown, text
- `include_favicon` (boolean, optional): Whether to include the favicon URL for each result
### `tavily_map`
Map a website's structure. Returns a list of URLs found starting from the base URL.

Parameters:
- `url` (string, required): The root URL to begin the mapping
- `max_depth` (integer, optional): Max depth of the mapping. Defines how far from the base URL the crawler can explore
- `max_breadth` (integer, optional): Max number of links to follow per level of the tree (i.e., per page)
- `limit` (integer, optional): Total number of links the crawler will process before stopping
- `instructions` (string, optional): Natural language instructions for the crawler
- `select_paths` (array of string, optional): Regex patterns to select only URLs with specific path patterns (e.g., /docs/.*, /api/v1.*)
- `select_domains` (array of string, optional): Regex patterns to restrict crawling to specific domains or subdomains (e.g., ^docs\.example\.com$)
- `allow_external` (boolean, optional): Whether to return external links in the final response
### `tavily_research`
Perform comprehensive research on a given topic or question. Use this tool when you need to gather information from multiple sources, including web pages, documents, and other resources, to answer a question or complete a task. Returns a detailed response based on the research findings.

Parameters:
- `input` (string, required): A comprehensive description of the research task
- `model` (string, optional): Defines the degree of depth of the research. 'mini' is good for narrow tasks with few subtopics. 'pro' is good for broad tasks with many subtopics Values: mini, pro, auto

# Usage
## CLI

### tavily_search
```shell
npx onekey agent tavily-remote-mcp/tavily-remote-mcp tavily_search '{"query": "NVIDIA earnings", "max_results": 5, "search_depth": "advanced"}'
```

### tavily_extract
```shell
npx onekey agent tavily-remote-mcp/tavily-remote-mcp tavily_extract '{"urls": ["https://example.com/article"], "extract_depth": "advanced", "format": "markdown"}'
```

### tavily_crawl
```shell
npx onekey agent tavily-remote-mcp/tavily-remote-mcp tavily_crawl '{"url": "https://example.com", "max_depth": 1, "max_breadth": 10, "limit": 20}'
```

### tavily_map
```shell
npx onekey agent tavily-remote-mcp/tavily-remote-mcp tavily_map '{"url": "https://example.com/docs", "max_depth": 1, "max_breadth": 10, "limit": 30}'
```

### tavily_research
```shell
npx onekey agent tavily-remote-mcp/tavily-remote-mcp tavily_research '{"input": "Impact of AI on healthcare", "model": "pro"}'
```

## Scripts
Each tool has a dedicated script in this folder:
- `skills/tavily-remote-mcp/scripts/tavily_search.py`
- `skills/tavily-remote-mcp/scripts/tavily_extract.py`
- `skills/tavily-remote-mcp/scripts/tavily_crawl.py`
- `skills/tavily-remote-mcp/scripts/tavily_map.py`
- `skills/tavily-remote-mcp/scripts/tavily_research.py`
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
