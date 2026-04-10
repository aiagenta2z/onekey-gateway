## Map (Baidu) - baidu-maps-sse/baidu-maps-sse

### Skill: baidu-maps-sse
#### maps_geocode
Description: Convert an address into geographic coordinates
## Parameters
- address: string — The address to geocode
##### CLI
```
npx onekey agent baidu-maps-sse/baidu-maps-sse maps_geocode '{"address": "Times Square, New York"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"baidu-maps-sse/baidu-maps-sse","api_id":"maps_geocode","data":{"address": "Times Square, New York"}}'
```
##### MCP
```
npx onekey mcp baidu-maps-sse
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-baidu-maps-sse":{
      "url":"https://agent.deepnlp.org/mcp?server_name=baidu-maps-sse&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill baidu-maps-sse -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill baidu-maps-sse
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="baidu-maps-sse/baidu-maps-sse", api_id="maps_geocode", data={"address": "Times Square, New York"})
```

#### maps_reverse_geocode
Description: Convert coordinates into an address
## Parameters
- latitude: number — Latitude coordinate
- longitude: number — Longitude coordinate
##### CLI
```
npx onekey agent baidu-maps-sse/baidu-maps-sse maps_reverse_geocode '{"latitude": 40.758, "longitude": -73.9855}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"baidu-maps-sse/baidu-maps-sse","api_id":"maps_reverse_geocode","data":{"latitude": 40.758, "longitude": -73.9855}}'
```
##### MCP
```
npx onekey mcp baidu-maps-sse
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-baidu-maps-sse":{
      "url":"https://agent.deepnlp.org/mcp?server_name=baidu-maps-sse&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill baidu-maps-sse -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill baidu-maps-sse
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="baidu-maps-sse/baidu-maps-sse", api_id="maps_reverse_geocode", data={"latitude": 40.758, "longitude": -73.9855})
```

#### maps_search_places
Description: Search for places using Google Places API
## Parameters
- query: string — Search query
- location: object — Optional center point for the search
- radius: number — Search radius in meters (max 50000)
##### CLI
```
npx onekey agent baidu-maps-sse/baidu-maps-sse maps_search_places '{"query": "Italian restaurants", "location": {"latitude": 40.758, "longitude": -73.9855}, "radius": 500}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"baidu-maps-sse/baidu-maps-sse","api_id":"maps_search_places","data":{"query": "Italian restaurants", "location": {"latitude": 40.758, "longitude": -73.9855}, "radius": 500}}'
```
##### MCP
```
npx onekey mcp baidu-maps-sse
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-baidu-maps-sse":{
      "url":"https://agent.deepnlp.org/mcp?server_name=baidu-maps-sse&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill baidu-maps-sse -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill baidu-maps-sse
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="baidu-maps-sse/baidu-maps-sse", api_id="maps_search_places", data={"query": "Italian restaurants", "location": {"latitude": 40.758, "longitude": -73.9855}, "radius": 500})
```

#### maps_place_details
Description: Get detailed information about a specific place
## Parameters
- place_id: string — The place ID to get details for
##### CLI
```
npx onekey agent baidu-maps-sse/baidu-maps-sse maps_place_details '{"place_id": "ChIJmQJIxlVYwokRLgeuocVOGVU"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"baidu-maps-sse/baidu-maps-sse","api_id":"maps_place_details","data":{"place_id": "ChIJmQJIxlVYwokRLgeuocVOGVU"}}'
```
##### MCP
```
npx onekey mcp baidu-maps-sse
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-baidu-maps-sse":{
      "url":"https://agent.deepnlp.org/mcp?server_name=baidu-maps-sse&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill baidu-maps-sse -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill baidu-maps-sse
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="baidu-maps-sse/baidu-maps-sse", api_id="maps_place_details", data={"place_id": "ChIJmQJIxlVYwokRLgeuocVOGVU"})
```

#### maps_distance_matrix
Description: Calculate travel distance and time for multiple origins and destinations
## Parameters
- origins: array — Array of origin addresses or coordinates
- destinations: array — Array of destination addresses or coordinates
- mode: string — Travel mode (driving, walking, bicycling, transit)
##### CLI
```
npx onekey agent baidu-maps-sse/baidu-maps-sse maps_distance_matrix '{"origins": ["Times Square, NY"], "destinations": ["Central Park, NY"], "mode": "driving"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"baidu-maps-sse/baidu-maps-sse","api_id":"maps_distance_matrix","data":{"origins": ["Times Square, NY"], "destinations": ["Central Park, NY"], "mode": "driving"}}'
```
##### MCP
```
npx onekey mcp baidu-maps-sse
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-baidu-maps-sse":{
      "url":"https://agent.deepnlp.org/mcp?server_name=baidu-maps-sse&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill baidu-maps-sse -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill baidu-maps-sse
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="baidu-maps-sse/baidu-maps-sse", api_id="maps_distance_matrix", data={"origins": ["Times Square, NY"], "destinations": ["Central Park, NY"], "mode": "driving"})
```

#### maps_elevation
Description: Get elevation data for locations on the earth
## Parameters
- locations: array — Array of locations to get elevation for
##### CLI
```
npx onekey agent baidu-maps-sse/baidu-maps-sse maps_elevation '{"locations": [{"latitude": 36.057944, "longitude": -112.125168}]}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"baidu-maps-sse/baidu-maps-sse","api_id":"maps_elevation","data":{"locations": [{"latitude": 36.057944, "longitude": -112.125168}]}}'
```
##### MCP
```
npx onekey mcp baidu-maps-sse
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-baidu-maps-sse":{
      "url":"https://agent.deepnlp.org/mcp?server_name=baidu-maps-sse&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill baidu-maps-sse -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill baidu-maps-sse
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="baidu-maps-sse/baidu-maps-sse", api_id="maps_elevation", data={"locations": [{"latitude": 36.057944, "longitude": -112.125168}]})
```

#### maps_directions
Description: Get directions between two points
## Parameters
- origin: string — Starting point address or coordinates
- destination: string — Ending point address or coordinates
- mode: string — Travel mode (driving, walking, bicycling, transit)
##### CLI
```
npx onekey agent baidu-maps-sse/baidu-maps-sse maps_directions '{"origin": "Golden Gate Bridge", "destination": "Ferry Building San Francisco", "mode": "driving"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"baidu-maps-sse/baidu-maps-sse","api_id":"maps_directions","data":{"origin": "Golden Gate Bridge", "destination": "Ferry Building San Francisco", "mode": "driving"}}'
```
##### MCP
```
npx onekey mcp baidu-maps-sse
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-baidu-maps-sse":{
      "url":"https://agent.deepnlp.org/mcp?server_name=baidu-maps-sse&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill baidu-maps-sse -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill baidu-maps-sse
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="baidu-maps-sse/baidu-maps-sse", api_id="maps_directions", data={"origin": "Golden Gate Bridge", "destination": "Ferry Building San Francisco", "mode": "driving"})
```
