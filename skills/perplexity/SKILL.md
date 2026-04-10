---
name: perplexity
description: Auto-generated skill for perplexity tools via OneKey Gateway.
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


# perplexity Skill
Use the OneKey Gateway to access tools for this server via a unified access key.
## Quick Start
Set your OneKey access key:
```bash
export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_API_KEY
```
If no key is provided, the scripts fall back to the demo key `BETA_TEST_KEY_MARCH_2026`.
Common settings:
- `unique_id`: `perplexity/perplexity`
- `api_id`: one of the tools listed below
## Tools
### `perplexity_ask`
Answer a question using web-grounded AI (Sonar Pro model). Best for: quick factual questions, summaries, explanations, and general Q&A. Returns a text response with numbered citations. Fastest and cheapest option. Supports filtering by recency (hour/day/week/month/year), domain restrictions, and search context size. For in-depth multi-source research, use perplexity_research instead. For step-by-step reasoning and analysis, use perplexity_reason instead.

Parameters:
- `messages` (array of object, required): Array of conversation messages
- `messages[].role` (string, required): Role of the message sender Values: system, user, assistant
- `messages[].content` (string, required): The content of the message
- `search_recency_filter` (string, optional): Filter search results by recency. Use 'hour' for very recent news, 'day' for today's updates, 'week' for this week, etc. Values: hour, day, week, month, year
- `search_domain_filter` (array of string, optional): Restrict search results to specific domains (e.g., ['wikipedia.org', 'arxiv.org']). Use '-' prefix for exclusion (e.g., ['-reddit.com']).
- `search_context_size` (string, optional): Controls how much web context is retrieved. 'low' (default) is fastest, 'high' provides more comprehensive results. Values: low, medium, high
### `perplexity_research`
Conduct deep, multi-source research on a topic (Sonar Deep Research model). Best for: literature reviews, comprehensive overviews, investigative queries needing many sources. Returns a detailed response with numbered citations. Significantly slower than other tools (30+ seconds). For quick factual questions, use perplexity_ask instead. For logical analysis and reasoning, use perplexity_reason instead.

Parameters:
- `messages` (array of object, required): Array of conversation messages
- `messages[].role` (string, required): Role of the message sender Values: system, user, assistant
- `messages[].content` (string, required): The content of the message
- `strip_thinking` (boolean, optional): If true, removes <think>...</think> tags and their content from the response to save context tokens. Default is false.
- `reasoning_effort` (string, optional): Controls depth of deep research reasoning. Higher values produce more thorough analysis. Values: minimal, low, medium, high
### `perplexity_reason`
Analyze a question using step-by-step reasoning with web grounding (Sonar Reasoning Pro model). Best for: math, logic, comparisons, complex arguments, and tasks requiring chain-of-thought. Returns a reasoned response with numbered citations. Supports filtering by recency (hour/day/week/month/year), domain restrictions, and search context size. For quick factual questions, use perplexity_ask instead. For comprehensive multi-source research, use perplexity_research instead.

Parameters:
- `messages` (array of object, required): Array of conversation messages
- `messages[].role` (string, required): Role of the message sender Values: system, user, assistant
- `messages[].content` (string, required): The content of the message
- `strip_thinking` (boolean, optional): If true, removes <think>...</think> tags and their content from the response to save context tokens. Default is false.
- `search_recency_filter` (string, optional): Filter search results by recency. Use 'hour' for very recent news, 'day' for today's updates, 'week' for this week, etc. Values: hour, day, week, month, year
- `search_domain_filter` (array of string, optional): Restrict search results to specific domains (e.g., ['wikipedia.org', 'arxiv.org']). Use '-' prefix for exclusion (e.g., ['-reddit.com']).
- `search_context_size` (string, optional): Controls how much web context is retrieved. 'low' (default) is fastest, 'high' provides more comprehensive results. Values: low, medium, high
### `perplexity_search`
Search the web and return a ranked list of results with titles, URLs, snippets, and dates. Best for: finding specific URLs, checking recent news, verifying facts, discovering sources. Returns formatted results (title, URL, snippet, date) — no AI synthesis. For AI-generated answers with citations, use perplexity_ask instead.

Parameters:
- `query` (string, required): Search query string
- `max_results` (number, optional): Maximum number of results to return (1-20, default: 10)
- `max_tokens_per_page` (number, optional): Maximum tokens to extract per webpage (default: 1024)
- `country` (string, optional): ISO 3166-1 alpha-2 country code for regional results (e.g., 'US', 'GB')

# Usage
## CLI

### perplexity_ask
```shell
npx onekey agent perplexity/perplexity perplexity_ask '{"question": "Who won the 2024 World Series?"}'
```

### perplexity_research
```shell
npx onekey agent perplexity/perplexity perplexity_research '{"query": "renewable energy policies US"}'
```

### perplexity_reason
```shell
npx onekey agent perplexity/perplexity perplexity_reason '{"topic": "impact of quantum computing"}'
```

### perplexity_search
```shell
npx onekey agent perplexity/perplexity perplexity_search '{"query": "best VR headsets 2026"}'
```

## Scripts
Each tool has a dedicated script in this folder:
- `skills/perplexity/scripts/perplexity_ask.py`
- `skills/perplexity/scripts/perplexity_research.py`
- `skills/perplexity/scripts/perplexity_reason.py`
- `skills/perplexity/scripts/perplexity_search.py`
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
Use the `npx onekey` CLI as the preferred method to run the skills.
