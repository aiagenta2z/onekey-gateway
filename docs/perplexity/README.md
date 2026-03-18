## Research QA - perplexity/perplexity

### Skill: perplexity
#### perplexity_ask
Description: Answer a question using web-grounded AI (Sonar Pro model). Best for: quick factual questions, summaries, explanations, and general Q&A. Returns a text response with numbered citations. Fastest and cheapest option. Supports filtering by recency (hour/day/week/month/year), domain restrictions, and search context size. For in-depth multi-source research, use perplexity_research instead. For step-by-step reasoning and analysis, use perplexity_reason instead.
## Parameters
- messages: array — Array of conversation messages
- search_recency_filter: string — Filter search results by recency. Use 'hour' for very recent news, 'day' for today's updates, 'week' for this week, etc.
- search_domain_filter: array — Restrict search results to specific domains (e.g., ['wikipedia.org', 'arxiv.org']). Use '-' prefix for exclusion (e.g., ['-reddit.com']).
- search_context_size: string — Controls how much web context is retrieved. 'low' (default) is fastest, 'high' provides more comprehensive results.
##### CLI
```
onekey agent perplexity/perplexity perplexity_ask '{"question": "Who won the 2024 World Series?"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"perplexity/perplexity","api_id":"perplexity_ask","data":{"question": "Who won the 2024 World Series?"}}'
```
##### MCP
```
onekey mcp perplexity
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-perplexity":{
      "url":"https://agent.deepnlp.org/mcp?server_name=perplexity&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill perplexity -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill perplexity
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="perplexity/perplexity", api_id="perplexity_ask", data={"question": "Who won the 2024 World Series?"})
```

#### perplexity_research
Description: Conduct deep, multi-source research on a topic (Sonar Deep Research model). Best for: literature reviews, comprehensive overviews, investigative queries needing many sources. Returns a detailed response with numbered citations. Significantly slower than other tools (30+ seconds). For quick factual questions, use perplexity_ask instead. For logical analysis and reasoning, use perplexity_reason instead.
## Parameters
- messages: array — Array of conversation messages
- strip_thinking: boolean — If true, removes <think>...</think> tags and their content from the response to save context tokens. Default is false.
- reasoning_effort: string — Controls depth of deep research reasoning. Higher values produce more thorough analysis.
##### CLI
```
onekey agent perplexity/perplexity perplexity_research '{"query": "renewable energy policies US"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"perplexity/perplexity","api_id":"perplexity_research","data":{"query": "renewable energy policies US"}}'
```
##### MCP
```
onekey mcp perplexity
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-perplexity":{
      "url":"https://agent.deepnlp.org/mcp?server_name=perplexity&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill perplexity -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill perplexity
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="perplexity/perplexity", api_id="perplexity_research", data={"query": "renewable energy policies US"})
```

#### perplexity_reason
Description: Analyze a question using step-by-step reasoning with web grounding (Sonar Reasoning Pro model). Best for: math, logic, comparisons, complex arguments, and tasks requiring chain-of-thought. Returns a reasoned response with numbered citations. Supports filtering by recency (hour/day/week/month/year), domain restrictions, and search context size. For quick factual questions, use perplexity_ask instead. For comprehensive multi-source research, use perplexity_research instead.
## Parameters
- messages: array — Array of conversation messages
- strip_thinking: boolean — If true, removes <think>...</think> tags and their content from the response to save context tokens. Default is false.
- search_recency_filter: string — Filter search results by recency. Use 'hour' for very recent news, 'day' for today's updates, 'week' for this week, etc.
- search_domain_filter: array — Restrict search results to specific domains (e.g., ['wikipedia.org', 'arxiv.org']). Use '-' prefix for exclusion (e.g., ['-reddit.com']).
- search_context_size: string — Controls how much web context is retrieved. 'low' (default) is fastest, 'high' provides more comprehensive results.
##### CLI
```
onekey agent perplexity/perplexity perplexity_reason '{"topic": "impact of quantum computing"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"perplexity/perplexity","api_id":"perplexity_reason","data":{"topic": "impact of quantum computing"}}'
```
##### MCP
```
onekey mcp perplexity
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-perplexity":{
      "url":"https://agent.deepnlp.org/mcp?server_name=perplexity&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill perplexity -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill perplexity
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="perplexity/perplexity", api_id="perplexity_reason", data={"topic": "impact of quantum computing"})
```

#### perplexity_search
Description: Search the web and return a ranked list of results with titles, URLs, snippets, and dates. Best for: finding specific URLs, checking recent news, verifying facts, discovering sources. Returns formatted results (title, URL, snippet, date) — no AI synthesis. For AI-generated answers with citations, use perplexity_ask instead.
## Parameters
- query: string — Search query string
- max_results: number — Maximum number of results to return (1-20, default: 10)
- max_tokens_per_page: number — Maximum tokens to extract per webpage (default: 1024)
- country: string — ISO 3166-1 alpha-2 country code for regional results (e.g., 'US', 'GB')
##### CLI
```
onekey agent perplexity/perplexity perplexity_search '{"query": "best VR headsets 2026"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"perplexity/perplexity","api_id":"perplexity_search","data":{"query": "best VR headsets 2026"}}'
```
##### MCP
```
onekey mcp perplexity
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-perplexity":{
      "url":"https://agent.deepnlp.org/mcp?server_name=perplexity&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill perplexity -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill perplexity
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="perplexity/perplexity", api_id="perplexity_search", data={"query": "best VR headsets 2026"})
```
