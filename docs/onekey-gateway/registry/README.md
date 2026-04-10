## 🚀 OneKey Gateway API Registry

Easily register, route, track, and monetize your APIs with OneKey Gateway. Convert your API to CLIs, Skills and more.


This guide walks you through:

A quick example using <api_endpoint> + <data>
How to register your API
How to call it via OneKey Gateway (REST + CLI)
Full JSON/YAML configuration examples
Secure Authentication, support header API keys `AUTH_HEADER`, `Bearer Token`, etc.

#### OneKey Gateway Agent/Skills/MCP Conversion Matrix

Register and maintain your APIs/MCP server only once, AI Agent Marketplace registry, convert to other formats 10x faster, supported APIs/CLIs/Skills/Rest API/MCPs 

| From \ To            | API | CLI | Skills | Routed API | MCPs (StreamingHTTP) | MCPs (Stdio Local) |
|---------------------|-----|-----|--------|------------|----------------------|--------------------|
| **API**             | -   | ✅   | ✅      | ✅          | ✅                    | -       |
| **CLI**             | -   | -   | ✅      | -          | -                    | ✅                  |
| **Skills**          | -   | -   | -      | -          | ✅                    | ✅                  |
| **Routed API**        | -   | -   | -      | -          | -                    | -                  |
| **MCPs (Streaming HTTP)** | -   | -   | -      | -          | -                    | -                  |
| **MCPs (Stdio Local)**    | -   | -   | -      | -          | -                    | -                  |


###  Quickstart


#### Example 1: Convert Food Calories API with header Access Key to Agent Skills/CLIs
The workflow is like: USDA FoodData Central API → OneKey Gateway Registry -> CLIs/REST API/MCPs/Skills

[Food Data API](https://fdc.nal.usda.gov/api-guide) and [Keys](https://fdc.nal.usda.gov/api-key-signup)

This example will introduce you how to register the Food Nutrition API with unique Access Key
and convert to CLIs/REST API/MCPs/Skills. 

##### 1. Prepare API Specs in Agent Config
Define the APIs endpoint, authentification and other informations (OpenAPI Specs). Follow the format below.   
Create `agent.yaml` (or `agent.json`) with your API metadata, see [agent.json](https://raw.githubusercontent.com/aiagenta2z/onekey-gateway/refs/heads/main/examples/usda_food_api/agent.json) and [agent.yaml](https://raw.githubusercontent.com/aiagenta2z/onekey-gateway/refs/heads/main/examples/usda_food_api/agent.yaml).    
The fdc_api.json and fdc_api.yaml are downloaded OpenAPI Specs from website, it will be referenced when you use claude code/codex to generate the agent.json api_list fields.    

User your Claude Code or Codex to help you generate the meta file 

```shell
Generate agent.json and agent.yaml file following the format of ./examples/usda_food_api/agent.json and agent.yaml format,
fill in the api_list key, with meta of APIs: api_id,protocol,description,endpoint,method,params,auth, For params, you can read the necessary informations from the the OpenAPI specs of fdc_api.json.
Output to /agent.json or /agent.yaml formats
```


---

##### 2. Register Your API to Registry

Get the Access Key from [Website Console](https://deepnlp.org/workspace/keys) to authenticate you are owner of registered Agentic APIs under scene 'ai_agent_marketplace_api'.

```bash
export AI_AGENT_MARKETPLACE_ACCESS_KEY=YOUR_REGISTRY_KEY

agtm upload --config ./agent.yaml
# or
agtm upload --config ./agent.json
```

The unique_id of your agent "user_id/repo_name" format, the user_id is the one associated with the ACCESS_KEY, and the repo_name
is in the agent.json files "name" field. In our case, "fdcnal/usda-fooddata-central-agent", see [detailed page](https://www.deepnlp.org/store/ai-agent/ai-agent/pub-fdcnal/usda-fooddata-central-agent)

##### 3. Usage

We will see how to use the `search_foods` api of registered agent in various formats usage: 
`unique_id`: `fdcnal/usda-fooddata-central-agent`
`api_id`: `search_foods`

<details>
<summary>Api2RestApi</summary>

Get the OneKey Router [Access](https://www.deepnlp.org/workspace/keys). This access is users' side access key, different from the api registration developer one.

```shell
export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_ROUTER_KEY

curl -X POST "https://agent.deepnlp.org/agent_router" \
-H "Content-Type: application/json" \
-H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
-d '{
  "unique_id": "fdcnal/usda-fooddata-central-agent",
  "api_id": "search_foods",
  "data": {
    "query": "Cheddar Cheese",
    "pageSize": 10
  }
}'
```

</details>


<details>
<summary>Api2CLI</summary>

```shell
npx onekey agent <unique_id> <api_id> $JSON_DATA

npx onekey agent fdcnal/usda-fooddata-central-agent search_foods '{"query": "Cheddar Cheese","pageSize": 10}'
```

</details>


<details>
<summary>Api2Skills</summary>

Run the cli to fetch api_data from central registry or load from local agent.json/yaml format files.
Create the skills/new-skills/SKILL.md,scripts/,reference/ files.

```shell
export AI_AGENT_MARKETPLACE_ACCESS_KEY=YOUR_REGISTRY_KEY

npx agtm skills build <unique_id>
## e.g.
npx agtm skills build fdcnal/usda-fooddata-central-agent
```

Generates:
```
skills/fdcnal-usda-fooddata-central-agent/
  ├── SKILL.md
  ├── scripts/
  └── reference/
```

See generated skills under [GitHub](https://github.com/aiagenta2z/onekey-gateway/skills)

</details>

<details>
<summary>Api2MCPServer</summary>

```shell
npx onekey mcp fdcnal/usda-fooddata-central-agent
```

Generates the config, you can just copy and paste the StreamingHttp into your clients (Claude Code/Cursor/etc)
```
{
  "mcpServers": {
    "deepnlp-onekey-fdcnal-usda-fooddata-central-agent": {
      "url": "https://agent.deepnlp.org/mcp?server_name=fdcnal/usda-fooddata-central-agent&onekey=YOUR_KEY"
    }
  }
}
```

</details>

#### Example 2: Financial API with header Access Key to Other Formats

##### 1. Prepare API Specs in Agent Config

You can use coding agent to help you fill the api and agent meta data.

Assume you already have an API with these information

```shell
curl -X POST <api_endpoint> \
  -H "Content-Type: application/json" \
  -H "<AUTH_HEADER>: $YOUR_API_KEY" \
  -d '<data>'
```

**Example**
```shell
export FINANCE_AGENT_API_KEY=your_finance_agent_key 

curl -X POST https://aiagenta2z.aiagenta2z.com/financeagent/api/v1/get_hk_stock_market_hkex \
  -H "Content-Type: application/json" \
  -H "X-Finance-Key: $FINANCE_AGENT_API_KEY" \
  -d '{"symbol_list": ["700", "1024"]}'
```

#### Describe Your API (Meta)

| Field       | Example                    | Description           |
| ----------- |----------------------------| --------------------- |
| api_id      | `get_hk_stock_market_hkex` | Unique API identifier |
| protocol    | `http`, `mcp`, `rpc`       | Default is `http`     |
| endpoint    | `<api_endpoint>`           | Your API URL          |
| method      | `POST`                     | GET / POST            |
| params      | `<data>`                   | Request body or query |
| auth.type   | `API_KEY`                  | Auth type             |
| auth.header | `X-Finance-Key`            | Header name           |
| auth.value  | `$YOUR_API_KEY`            | Your API key          |


#### Auth Fields Explanation
| KEY         | Type | Description                                                                                                                                           |
|-------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| auth.type       | str  | including `API_KEY`, `BEAR_TOKEN`                                                                                                                     |
| auth.header       | str  | Headers Key header, for type=`API_KEY`, set as `X-Custome-Key`, for type=`BEAR_TOKEN`, set as `Authorization`                                         |
| auth.value       | str  | Headers Value header, for type=`API_KEY`, set as `Header-Value`, for type=`BEAR_TOKEN`, set as `Bearer $YOUR_BEARER_ACCESS`, keep prefix in the value |


##### 2. Register Your API

Create a config file:

```shell
agent.json   
# OR 
agent.yaml
```

Upload API and Agent meta using CLI `agtm`:

Get the registry [Agent Marketplace Keys](https://deepnlp.org/workspace/keys).

```
## Get your Onw Registry Keys
export AI_AGENT_MARKETPLACE_ACCESS_KEY="TEST_KEY_AI_AGENT_REGISTRY"

agtm upload --config ./agent.json
# or
agtm upload --config ./agent.yaml
```

##### 3. Usage
Call via OneKey Gateway

After registration, you can start to use onekey gateway to authenticate
and start to track your API usage and routed by agent APIs and command lines CLI.

<details>
<summary>Api2RestAPI</summary>

Get the onekey-gateway keys DEEPNLP_ONEKEY_ROUTER_ACCESS [Keys](https://deepnlp.org/workspace/keys).

```shell
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key

curl -X POST "https://agent.deepnlp.org/agent_router" \
-H "Content-Type: application/json" \
-H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
-d '{
  "unique_id": "aiagenta2z/financeagent",
  "api_id": "get_hk_stock_market_hkex",
  "data": {
    "symbol_list": ["700", "1024"]
  }
}'
```


</details>


<details>
<summary>Api2CLI</summary>

```shell
npx onekey agent aiagenta2z/financeagent get_hk_stock_market_hkex '{"symbol_list": ["700", "1024"]}'
```

</details>


<details>
<summary>Api2Skills</summary>

```shell
npx agtm skills build <unique_id>

npx agtm skills build aiagenta2z/financeagent
```

Generates Skills Format:
```
skills/aiagenta2z-financeagent/
  ├── SKILL.md
  ├── scripts/
  └── reference/
```

See generated skills under [GitHub](https://github.com/aiagenta2z/onekey-gateway/skills)

</details>

<details>
<summary>Api2MCPServer</summary>

```shell
npx onekey mcp aiagenta2z/financeagent
```

Generates:
```
{
  "mcpServers": {
    "deepnlp-onekey-aiagenta2z-financeagent": {
      "url": "https://agent.deepnlp.org/mcp?server_name=aiagenta2z/financeagent&onekey=YOUR_KEY"
    }
  }
}
```
</details>


### API Meta Schema

#### Parameters

| KEY         | Type | Description                                         |
|-------------|------|-----------------------------------------------------|
| api_list    | List | List of API Information                             |
| api_id      | str  | The unique Id to identifiy each API                 |
| protocol    | str  | `http`,`mcp`,`rpc` Default to `http` for API Calling |
| description | str  | Description Usage                                   |
| endpoint    | str  | endpoint URL                                        |
| method      | str  | GET/POST                                            |
| params      | Dict | Parameters                                          |
| auth        | Dict | The authentication method of the API                |


#### Auth Fields
| KEY         | Type | Description                                                                                                                                           |
|-------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| auth.type       | str  | `API_KEY`, `BEAR_TOKEN`                                                                                                                               |
| auth.header       | str  | Headers Key header, for type=`API_KEY`, set as `X-Custome-Key`, for type=`BEAR_TOKEN`, set as `Authorization`                                         |
| auth.value       | str  | Headers Value header, for type=`API_KEY`, set as `Header-Value`, for type=`BEAR_TOKEN`, set as `Bearer $YOUR_BEARER_ACCESS`, keep prefix in the value |


📦 Full Example (JSON)

#### Json
`agent.json` file, see [agent.json](../../../examples/finance_agent_api/agent.json)


#### yaml

`agent.yaml` file contents, see [agent.yaml](../../../examples/finance_agent_api/agent.yaml) for example.

🔁 Request Flow (Mental Model)
```shell
User / CLI
   ↓
OneKey Gateway
   ↓
Your Registered API
   ↓
Response returned + usage tracked + credits deducted

```


### Common Issues

<details>
<summary>400 Error: API not found</summary>

Ensure correct unique_id, you can use curl to check if the Agent Meta and APIs are correctly registered as in [Doc](https://deepnlp.org/doc/ai_agent_marketplace)
Note that the APIs infos are propriety to the devs only, so your auth keys  are safe and the curl will be return proprietary informations.

e.g. 
```shell
curl 'https://www.deepnlp.org/api/ai_agent_marketplace/v2?mode=list&id={user_id/repo_name}'
```

```
fdcnal/usda-fooddata-central-agent
```
</details>


<details>
<summary>Auth Issues</summary>

The gateway handles authentication securely before forwarding the request.

```shell
Request → OneKey Gateway (encrypted authentication) → Forward to your registered API with verified credentials
```

The gateway handles authentication securely before forwarding the request.

Supported authentication methods include:

API_KEY — supports custom headers, e.g.  X-Customize-API: ${header_value},
BEARER_TOKEN — uses standard authorization format, e.g.  Authorization: Bearer ${your_bearer_access}

Your original credentials are never exposed directly. They are securely stored, encrypted, and authenticated within the gateway registry before being used in requests.

```
    auth:
      type: "API_KEY"
      header: "X-API-Key"
      value: "REGISTRY_API_GET_KEY"
```

or 

```
    auth:
      type: "BEAR_TOKEN"
      header: "Authorization"
      value: "YOUR_BEARER_ACCESS"
```

</details>

