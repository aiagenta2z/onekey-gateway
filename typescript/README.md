# OneKey Gateway
AI Agent Gateway to Commercial APIs, Skills, MCPs and more using just one access key for most benefits.

[GitHub](https://github.com/aiagenta2z/onekey-gateway)|[Document](http://www.deepnlp.org/doc/onekey_gateway)|[AI Agent Marketplace](http://www.deepnlp.org/store/ai-agent)|[AI Agent Search](http://www.deepnlp.org/search/agent) | [AI Agent A2Z Deployment](https://deepnlp.org/doc/agent_mcp_deployment) | [Agent A2Z Payment](https://www.deepnlp.org/doc/agent_a2z_payment)

**Onekey Gateway** focuses on commercial agent APIs/MCPs/Skills, which typically require multiple subscriptions or access keys for web search,image generation, financial data, 3D rendering. 
Our mission is to help users authenticate once and enjoy the most benefits, discounted, pay-as-you-go usage. Accessing Agent APIs, MCPs, and LLMs across 30+ categories and 100+ tools via our credit system, 
you can eliminate multiple expensive subscriptions and maximize your benefits. More SOTA agent/models are available in the [DeepNLP AI Agent Mareketplace](https://deepnlp.org/store/ai-agent).

## Overview
[OneKey Gateway Document](https://www.deepnlp.org/doc/onekey_gateway)   

OneKey Gateway provides CLI tool, Restful API, MCP, Skills and Python/Typescript methods for Agent and human to use commercial Agent APIs.

| Gateway Type | Description                                                                                                   | BASE URL                               | CLI            |         
|-------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------|----------------|   
| Agent APIs  | Allow your AI Agent to Access APIs [OneKey Agent Router Doc](https://www.deepnlp.org/doc/onekey_agent_router) | https://agent.deepnlp.org/agent_router | `onekey agent` | 
| MCP  | Allow your AI clients to connect to commercial Http MCP [OneKey MCP Router Doc](https://www.deepnlp.org/doc/onekey_mcp_router)                                                       | https://agent.deepnlp.org/mcp          | `onekey mcp`   | 
| LLM | Allow your AI clients to call LLM endpoint proxy   [OneKey LLM Router Doc](https://www.deepnlp.org/doc/onekey_llm_router)                                                             | https://agent.deepnlp.org/llm          | `onekey llm`   |


### Architecture
This is an example of how onekey-gateway can help you and your AI agents to use commercial
API,Skills and MCPs in one single gateway.

```shell
                   ┌─────────────┐
                   │   Client    │
                   │ (App / CLI) │
                   └─────┬───────┘
                         │
                         ▼
                ┌───────────────────┐
                │ OneKey Gateway    │
                │───────────────────│
                │ • Authentication  │
                │ • Security        │
                │ • Billing/Quotas  │
                │ • Rate Limiting   │
                └─────┬─────────────┘
                         │
                         ▼
                 ┌──────────────────┐
                 │  OneKey Router   │
                 ├──────────────────┤
                 │ • Routes requests│
                 │ • Load balances  │
                 │ • Policy checks  │
                 └─────┬────────────┘
          ┌────────────┼────────────┐
          ▼            ▼            ▼
 ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
 │ Agent Router   │ │ MCP Router     │ │ LLM Router     │
 │ (Agents /      │ │ (Tools / MCPs) │ │ (LLM Providers)│
 │ Skills)        │ │                │ │                │
 └─────┬──────────┘ └─────┬──────────┘ └─────┬──────────┘
       │                  │                  │
       ▼                  ▼                  ▼
 ┌─────────────┐   ┌─────────────┐    ┌─────────────┐
 │ Execution   │   │ Execution   │    │ Execution   │
 │ Layer       │   │ Layer       │    │ Layer       │
 │ • APIs      │   │ • MCP       │    │ • LLM       │
 │ • Orchest   │   │Servers/Tools│    │ Providers   │
 └─────┬───────┘   └─────┬───────┘    └─────┬───────┘
       ▼                  ▼                  ▼
 ┌──────────────────────────────────────────────┐
 │           Provider APIs / External Services  │
 │ • LLM APIs, SaaS tools, Databases, etc.      │
 └──────────────────────────────────────────────┘
```

### Install

```bash
npm install @aiagenta2z/onekey-gateway
```

### OneKey Access Key

**Step 1**. Get AI Agent A2Z OneKey access key
You can get the OneKey Gateway [Access Keys](https://deepnlp.org/workspace/keys).

**Step 2**. Set OneKey Access 
```shell
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
```
For demo purpose, use the demo key for demo results.

```shell
export DEEPNLP_ONEKEY_ROUTER_ACCESS=BETA_TEST_KEY_MAR_2026
```
The CLI reads the access key from `DEEPNLP_ONEKEY_ROUTER_ACCESS`. If not set, it falls back to `BETA_TEST_KEY_MARCH_2026`. 

## Quickstart 

### OneKey CLI

#### Example 1: Google Maps 
Your Agent will search Google Maps to find places, rankings, etc. 
prompt: New York City Italian Restaurants

```bash

onekey agent google-maps/google-maps maps_search_places '{"query":"New York City Italian Restaurants"}'
```
Result
```shell
{"success":true,"data":"[\"{\\n  \\\"places\\\": [\\n    {\\n      \\\"name\\\": \\\"Carmine's - Time Square\\\",\\n      \\\"formatted_address\\\": \\\"200 W 44th St, New York, NY 10036, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.757498,\\n        \\\"lng\\\": -73.986654\\n      },\\n      \\\"place_id\\\": \\\"ChIJR9So-lRYwokRX1xEjA0rChA\\\",\\n      \\\"rating\\\": 4.5,\\n      \\\"types\\\": [\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"Osteria La Baia\\\",\\n      \\\"formatted_address\\\": \\\"129 W 52nd St, New York, NY 10019, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.7618881,\\n        \\\"lng\\\": -73.9809702\\n      },\\n      \\\"place_id\\\": \\\"ChIJo9FTvDBZwokRFAZ0i4jbLuk\\\",\\n      \\\"rating\\\": 4.9,\\n      \\\"types\\\": [\\n        \\\"bar\\\",\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"Tony's Di Napoli\\\",\\n      \\\"formatted_address\\\": \\\"147 W 43rd St, New York, NY 10036, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.7564842,\\n        \\\"lng\\\": -73.9853808\\n      },\\n      \\\"place_id\\\": \\\"ChIJVS2qI1VYwokRFo18YsKvHYM\\\",\\n      \\\"rating\\\": 4.6,\\n      \\\"types\\\": [\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"La Lanterna di Vittorio\\\",\\n      \\\"formatted_address\\\": \\\"129 MacDougal St, New York, NY 10012, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.7306651,\\n        \\\"lng\\\": -74.0000496\\n      },\\n      \\\"place_id\\\": \\\"ChIJPxCEeZFZwokRzk5UghlXZWU\\\",\\n      \\\"rating\\\": 4.5,\\n      \\\"types\\\": [\\n        \\\"bar\\\",\\n        \\\"cafe\\\",\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"night_club\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\",\\n        \\\"store\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"Scarpetta\\\",\\n      \\\"formatted_address\\\": \\\"88 Madison Ave, New York, NY 10016, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.74458180000001,\\n        \\\"lng\\\": -73.9856202\\n      },\\n      \\\"place_id\\\": \\\"ChIJt8W7n79ZwokRsyXs3QDbE3o\\\",\\n      \\\"rating\\\": 4.6,\\n      \\\"types\\\": [\\n        \\\"bar\\\",\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"Osteria Nonnino\\\",\\n      \\\"formatted_address\\\": \\\"637 Hudson St, New York, NY 10014, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.7388972,\\n        \\\"lng\\\": -74.0057401\\n      },\\n      \\\"place_id\\\": \\\"ChIJu3WF-z9ZwokRSIlFddmXX1k\\\",\\n      \\\"rating\\\": 4.8,\\n      \\\"types\\\": [\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"OLIO E PIÙ\\\",\\n      \\\"formatted_address\\\": \\\"3 Greenwich Ave, New York, NY 10014, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.7338208,\\n        \\\"lng\\\": -73.99979309999999\\n      },\\n      \\\"place_id\\\": \\\"ChIJ_RUJvZZZwokRNUEv3K4nSik\\\",\\n      \\\"rating\\\": 4.7,\\n      \\\"types\\\": [\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"La Pecora Bianca SoHo\\\",\\n      \\\"formatted_address\\\": \\\"54 Prince St, New York, NY 10012, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.72346,\\n        \\\"lng\\\": -73.9963118\\n      },\\n      \\\"place_id\\\": \\\"ChIJfe6ZYKFZwokR_mHm7GNoAxc\\\",\\n      \\\"rating\\\": 4.8,\\n      \\\"types\\\": [\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"Osteria Barocca\\\",\\n      \\\"formatted_address\\\": \\\"133 Mulberry St, New York, NY 10013, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.7186467,\\n        \\\"lng\\\": -73.99792409999999\\n      },\\n      \\\"place_id\\\": \\\"ChIJK0YQvsRZwokR9r2ubFZRd7E\\\",\\n      \\\"rating\\\": 4.6,\\n      \\\"types\\\": [\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"Sicily Osteria\\\",\\n      \\\"formatted_address\\\": \\\"328-330 W 46th St, New York, NY 10036, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.7601601,\\n        \\\"lng\\\": -73.9891863\\n      },\\n      \\\"place_id\\\": \\\"ChIJ03krMjJZwokRYRF15upaCHw\\\",\\n      \\\"rating\\\": 4.6,\\n      \\\"types\\\": [\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"La Pecora Bianca NoMad\\\",\\n      \\\"formatted_address\\\": \\\"1133 Broadway, New York, NY 10010, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.7436754,\\n        \\\"lng\\\": -73.9891719\\n      },\\n      \\\"place_id\\\": \\\"ChIJPf0L06VZwokRD6L-7RV-7Yg\\\",\\n      \\\"rating\\\": 4.7,\\n      \\\"types\\\": [\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"Da Andrea Greenwich Village\\\",\\n      \\\"formatted_address\\\": \\\"35 W 13th St, New York, NY 10011, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.7361918,\\n        \\\"lng\\\": -73.9958515\\n      },\\n      \\\"place_id\\\": \\\"ChIJS1uszZRZwokRbKPTzS6hnWM\\\",\\n      \\\"rating\\\": 4.6,\\n      \\\"types\\\": [\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"Via Carota\\\",\\n      \\\"formatted_address\\\": \\\"51 Grove St, New York, NY 10014, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.7331959,\\n        \\\"lng\\\": -74.00364940000001\\n      },\\n      \\\"place_id\\\": \\\"ChIJr7FOf5NZwokRu3CDYtzVmuQ\\\",\\n      \\\"rating\\\": 4.4,\\n      \\\"types\\\": [\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"Masseria Dei Vini\\\",\\n      \\\"formatted_address\\\": \\\"887 9th Ave, New York, NY 10019, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.7684477,\\n        \\\"lng\\\": -73.9857048\\n      },\\n      \\\"place_id\\\": \\\"ChIJeVfr_FhYwokRVM1IjwyvQpE\\\",\\n      \\\"rating\\\": 4.6,\\n      \\\"types\\\": [\\n        \\\"bar\\\",\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"La Masseria NY\\\",\\n      \\\"formatted_address\\\": \\\"235 W 48th St, New York, NY 10036, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.76088499999999,\\n        \\\"lng\\\": -73.9863\\n      },\\n      \\\"place_id\\\": \\\"ChIJjfIegVZYwokRyqdwvzBC27s\\\",\\n      \\\"rating\\\": 4.5,\\n      \\\"types\\\": [\\n        \\\"bar\\\",\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"Zia Maria Little Italy\\\",\\n      \\\"formatted_address\\\": \\\"138 Mulberry St, New York, NY 10013, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.7187113,\\n        \\\"lng\\\": -73.9975649\\n      },\\n      \\\"place_id\\\": \\\"ChIJm7QTo_lZwokRRnjGuJABJPQ\\\",\\n      \\\"rating\\\": 4.6,\\n      \\\"types\\\": [\\n        \\\"bar\\\",\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\",\\n        \\\"store\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"Piccola Cucina Osteria Siciliana\\\",\\n      \\\"formatted_address\\\": \\\"196 Spring St, New York, NY 10012, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.7250308,\\n        \\\"lng\\\": -74.0032774\\n      },\\n      \\\"place_id\\\": \\\"ChIJowhlWYxZwokRgrvA8f_x8Es\\\",\\n      \\\"rating\\\": 4.6,\\n      \\\"types\\\": [\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"Trattoria Trecolori\\\",\\n      \\\"formatted_address\\\": \\\"254 W 47th St, New York, NY 10036, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.7599972,\\n        \\\"lng\\\": -73.9867421\\n      },\\n      \\\"place_id\\\": \\\"ChIJYepwLVRYwokRsvXclA3XFqo\\\",\\n      \\\"rating\\\": 4.5,\\n      \\\"types\\\": [\\n        \\\"bar\\\",\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"Don Angie\\\",\\n      \\\"formatted_address\\\": \\\"103 Greenwich Ave, New York, NY 10014, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.7378037,\\n        \\\"lng\\\": -74.00209389999999\\n      },\\n      \\\"place_id\\\": \\\"ChIJfxC19JVZwokRX2uKgQAL17c\\\",\\n      \\\"rating\\\": 4.6,\\n      \\\"types\\\": [\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    },\\n    {\\n      \\\"name\\\": \\\"Casa D'Angelo New York\\\",\\n      \\\"formatted_address\\\": \\\"146 Mulberry St, New York, NY 10013, USA\\\",\\n      \\\"location\\\": {\\n        \\\"lat\\\": 40.7188063,\\n        \\\"lng\\\": -73.9972296\\n      },\\n      \\\"place_id\\\": \\\"ChIJCxhnSohZwokRxmUkfrQWLfs\\\",\\n      \\\"rating\\\": 4.6,\\n      \\\"types\\\": [\\n        \\\"bar\\\",\\n        \\\"establishment\\\",\\n        \\\"food\\\",\\n        \\\"point_of_interest\\\",\\n        \\\"restaurant\\\"\\n      ]\\n    }\\n  ]\\n}\"]","error":null}
```


#### Example 2: Image Generation

model:
- gemini-3-pro-image-preview
- gemini-2.5-flash-image

```
onekey agent gemini-nano-banana/gemini-nano-banana generate_image_gemini '{"model":"gemini-2.5-flash-image", "prompt":"Generate a minecraft scene of steve fighting zombies in purple crystal fields."}'
```

```
{"success":true,"data":"[\"{\\n  \\\"image_path\\\": \\\"/data/python/mcp_tool_use/files-wd/user_2177/7629e198-b10c-4a8b-8f61-5c0a6744cab0/gemini_output_images.png\\\",\\n  \\\"image_url\\\": \\\"https://us-static.aiagenta2z.com/local/files-wd/user_2177/7629e198-b10c-4a8b-8f61-5c0a6744cab0/gemini_output_images.png\\\",\\n  \\\"message\\\": \\\"\\\",\\n  \\\"success\\\": true\\n}\"]","error":null}
## url of image generated
https://us-static.aiagenta2z.com/local/files-wd/user_2177/7629e198-b10c-4a8b-8f61-5c0a6744cab0/gemini_output_images.png
```
**Return Image URL Result**

<img src="https://raw.githubusercontent.com/aiagenta2z/onekey-agent-router/refs/heads/main/docs/onekey-gateway-example-gemini.jpg" style="width:500px" alt="Image generation">


## Tutorial

### CLI Usage
```bash
onekey agent <unique_id> <api_id> <data_json|@file>
onekey mcp <server_name> [--name config_name]
onekey llm --provider <provider> --model <model> --messages <json|@file> [--temperature <num>] [--response-format <format>] [--options <json|@file>]
onekey llm --payload <json|@file>
```

Supported ids can be found in the table below.

### OneKey Agent API

**CLI**

```bash
onekey agent google-maps/google-maps maps_search_places '{"query":"New York City Italian Restaurants"}'
```

**Skills**

`agtm` package
```bash
npx agtm add https://github.com/aiagenta2z/onekey-gateway  ## add all onekey router skills
npx agtm add aiagenta2z/onekey-gateway --skill google-maps -g  ## install to global path
```
`skills` package
```
npx skills add https://github.com/aiagenta2z/onekey-agent-router
## single skill
npx skills add https://github.com/aiagenta2z/onekey-agent-router --skill amap-maps-streamableHTTP
```

### OneKey MCP Config

```bash
onekey mcp google-maps
```
Put below config into your clients
```shell
{
  "mcpServers": {
    "deepnlp-onekey-google-maps": {
      "url": "https://agent.deepnlp.org/mcp?server_name=google-maps&onekey=your_access_key"
    }
  }
}
```

### OneKey LLM Router
Call Gemini 3 LLM and Image Nano Banana model
```bash
onekey llm --provider gemini --model gemini-3-flash-preview --messages @messages.json --temperature 0.7 --response-format json
```

## Gateway Categories

| Domain               | Unique Id                                                                                          | Skill ID                 | API ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 
|----------------------|----------------------------------------------------------------------------------------------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Map (Google)         | google-maps/google-maps [Doc](./docs/google-maps/README.md)                                        | google-maps              | maps_directions<br>maps_distance_matrix<br>maps_elevation<br>maps_geocode<br>maps_place_details<br>maps_reverse_geocode<br>maps_search_places                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Map (Amap/Gaode Map) | amap-maps-streamableHTTP/amap-maps-streamableHTTP [Doc](./docs/amap-maps-streamableHTTP/README.md) | amap-maps-streamableHTTP | maps_around_search<br>maps_direction_bicycling<br>maps_direction_driving<br>maps_direction_transit_integrated<br>maps_direction_walking<br>maps_distance<br>maps_geo<br>maps_ip_location<br>maps_regeocode<br>maps_schema_navi<br>maps_schema_personal_map<br>maps_schema_take_taxi<br>maps_search_detail<br>maps_text_search<br>maps_weather                                                                                                                                                                                                                                                                                                                                                   | 
| Map (Baidu)          | baidu-maps-sse/baidu-maps-sse  [Doc](./docs/baidu-maps-sse/README.md)                              | baidu-maps-sse           | maps_directions<br>maps_distance_matrix<br>maps_elevation<br>maps_geocode<br>maps_place_details<br>maps_reverse_geocode<br>maps_search_places                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 
| Image Search         | bing-image-search-mcp/bing-image-search-mcp [Doc](./docs/bing-image-search-mcp/README.md)          | bing-image-search-mcp    | search_images<br>search_images_batch                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 
| Web Search           | brave-search/brave-search   [Doc](./docs/brave-search/README.md)                                   | brave-search             | brave_local_search<br>brave_web_search                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 
| Web Search           | google-search/google-search  [Doc](./docs/google-search/README.md)                                 | google-search            | google_search                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 
| Web Search           | tavily-remote-mcp/tavily-remote-mcp [Doc](./docs/tavily-remote-mcp/README.md)                      | tavily-remote-mcp        | tavily_crawl<br>tavily_extract<br>tavily_map<br>tavily_research<br>tavily_search                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 
| Web Crawl / Browser  | firecrawl-mcp/firecrawl-mcp  [Doc](./docs/firecrawl-mcp/README.md)                                 | firecrawl-mcp            | firecrawl_agent<br>firecrawl_agent_status<br>firecrawl_browser_create<br>firecrawl_browser_delete<br>firecrawl_browser_execute<br>firecrawl_browser_list<br>firecrawl_check_crawl_status<br>firecrawl_crawl<br>firecrawl_extract<br>firecrawl_map<br>firecrawl_scrape<br>firecrawl_search                                                                                                                                                                                                                                                                                                                                                                                                       | 
| Image Generation     | gemini/gemini      [Doc](./docs/gemini/README.md)                                                  | gemini (Nano Banana)     | generate_image_gemini<br>generate_image_nano_banana<br>generate_image_nano_banana_with_reference<br>ocr_extract_text_from_image<br>list_items_from_image                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 
| Image Generation     | gemini-nano-banana/gemini-nano-banana      [Doc](./docs/gemini-nano-banana/README.md)              | gemini-nano-banana       | generate_image_gemini<br>generate_image_nano_banana<br>generate_image_nano_banana_with_reference<br>ocr_extract_text_from_image<br>list_items_from_image                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 
| Charts               | mcp-server-chart/mcp-server-chart  [Doc](./docs/mcp-server-chart/README.md)                        | mcp-server-chart         | generate_area_chart<br>generate_bar_chart<br>generate_boxplot_chart<br>generate_column_chart<br>generate_district_map<br>generate_dual_axes_chart<br>generate_fishbone_diagram<br>generate_flow_diagram<br>generate_funnel_chart<br>generate_histogram_chart<br>generate_line_chart<br>generate_liquid_chart<br>generate_mind_map<br>generate_network_graph<br>generate_organization_chart<br>generate_path_map<br>generate_pie_chart<br>generate_pin_map<br>generate_radar_chart<br>generate_sankey_chart<br>generate_scatter_chart<br>generate_spreadsheet<br>generate_treemap_chart<br>generate_venn_chart<br>generate_violin_chart<br>generate_waterfall_chart<br>generate_word_cloud_chart | 
| Research QA          | perplexity/perplexity  [Doc](./docs/perplexity/README.md)                                          | perplexity               | perplexity_ask<br>perplexity_reason<br>perplexity_research<br>perplexity_search                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 
| 3D Generation        | craftsman-agent/craftsman-agent [Doc](./docs/craftsman-agent/README.md)                            | craftsman-agent          | generate_lego_build_plan<br>generate_minecraft_build_plan                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 


#### Example 1: Google Maps Search

```bash
onekey agent google-maps/google-maps maps_search_places '{"query":"New York City Italian Restaurants"}'
```

```bash
curl -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{
    "unique_id": "google-maps/google-maps",
    "api_id": "maps_search_places",
    "data": {
      "query": "New York City Italian Restaurants"
    }
  }'
```

#### Example 2: Image Generation

model:
- gemini-3-pro-image-preview
- gemini-2.5-flash-image

```
onekey agent gemini-nano-banana/gemini-nano-banana generate_image_gemini '{"model":"gemini-2.5-flash-image", "prompt":"Generate a minecraft scene of steve fighting zombies in purple crystal fields."}'
```

```
{"success":true,"data":"[\"{\\n  \\\"image_path\\\": \\\"/data/python/mcp_tool_use/files-wd/user_2177/7629e198-b10c-4a8b-8f61-5c0a6744cab0/gemini_output_images.png\\\",\\n  \\\"image_url\\\": \\\"https://us-static.aiagenta2z.com/local/files-wd/user_2177/7629e198-b10c-4a8b-8f61-5c0a6744cab0/gemini_output_images.png\\\",\\n  \\\"message\\\": \\\"\\\",\\n  \\\"success\\\": true\\n}\"]","error":null}

## Return Image url: 
https://us-static.aiagenta2z.com/local/files-wd/user_2177/7629e198-b10c-4a8b-8f61-5c0a6744cab0/gemini_output_images.png
```


### Related

