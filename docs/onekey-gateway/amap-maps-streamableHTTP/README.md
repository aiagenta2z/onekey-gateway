## Map (Amap/Gaode Map) - amap-maps-streamableHTTP/amap-maps-streamableHTTP

### Skill: amap-maps-streamableHTTP
#### maps_direction_bicycling
Description: 骑行路径规划用于规划骑行通勤方案，规划时会考虑天桥、单行线、封路等情况。最大支持 500km 的骑行路线规划
## Parameters
- origin: string — 出发点经纬度，坐标格式为：经度，纬度
- destination: string — 目的地经纬度，坐标格式为：经度，纬度
##### CLI
```
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_direction_bicycling '{"origin": "116.481028,39.989643", "destination": "116.465302,40.004717"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"amap-maps-streamableHTTP/amap-maps-streamableHTTP","api_id":"maps_direction_bicycling","data":{"origin": "116.481028,39.989643", "destination": "116.465302,40.004717"}}'
```
##### MCP
```
npx onekey mcp amap-maps-streamableHTTP
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-amap-maps-streamableHTTP":{
      "url":"https://agent.deepnlp.org/mcp?server_name=amap-maps-streamableHTTP&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="amap-maps-streamableHTTP/amap-maps-streamableHTTP", api_id="maps_direction_bicycling", data={"origin": "116.481028,39.989643", "destination": "116.465302,40.004717"})
```

#### maps_direction_driving
Description: 驾车路径规划 API 可以根据用户起终点经纬度坐标规划以小客车、轿车通勤出行的方案，并且返回通勤方案的数据。
## Parameters
- origin: string — 出发点经纬度，坐标格式为：经度，纬度
- destination: string — 目的地经纬度，坐标格式为：经度，纬度
##### CLI
```
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_direction_driving '{"origin": "116.481028,39.989643", "destination": "116.465302,40.004717"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"amap-maps-streamableHTTP/amap-maps-streamableHTTP","api_id":"maps_direction_driving","data":{"origin": "116.481028,39.989643", "destination": "116.465302,40.004717"}}'
```
##### MCP
```
npx onekey mcp amap-maps-streamableHTTP
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-amap-maps-streamableHTTP":{
      "url":"https://agent.deepnlp.org/mcp?server_name=amap-maps-streamableHTTP&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="amap-maps-streamableHTTP/amap-maps-streamableHTTP", api_id="maps_direction_driving", data={"origin": "116.481028,39.989643", "destination": "116.465302,40.004717"})
```

#### maps_direction_transit_integrated
Description: 根据用户起终点经纬度坐标规划综合各类公共（火车、公交、地铁）交通方式的通勤方案，并且返回通勤方案的数据，跨城场景下必须传起点城市与终点城市
## Parameters
- origin: string — 出发点经纬度，坐标格式为：经度，纬度
- destination: string — 目的地经纬度，坐标格式为：经度，纬度
- city: string — 公共交通规划起点城市
- cityd: string — 公共交通规划终点城市
##### CLI
```
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_direction_transit_integrated '{"origin": "116.481028,39.989643", "destination": "116.465302,40.004717", "city": "北京", "cityd": "上海"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"amap-maps-streamableHTTP/amap-maps-streamableHTTP","api_id":"maps_direction_transit_integrated","data":{"origin": "116.481028,39.989643", "destination": "116.465302,40.004717", "city": "北京", "cityd": "上海"}}'
```
##### MCP
```
npx onekey mcp amap-maps-streamableHTTP
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-amap-maps-streamableHTTP":{
      "url":"https://agent.deepnlp.org/mcp?server_name=amap-maps-streamableHTTP&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="amap-maps-streamableHTTP/amap-maps-streamableHTTP", api_id="maps_direction_transit_integrated", data={"origin": "116.481028,39.989643", "destination": "116.465302,40.004717", "city": "北京", "cityd": "上海"})
```

#### maps_direction_walking
Description: 根据输入起点终点经纬度坐标规划100km 以内的步行通勤方案，并且返回通勤方案的数据
## Parameters
- origin: string — 出发点经度，纬度，坐标格式为：经度，纬度
- destination: string — 目的地经度，纬度，坐标格式为：经度，纬度
##### CLI
```
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_direction_walking '{"origin": "116.481028,39.989643", "destination": "116.465302,40.004717"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"amap-maps-streamableHTTP/amap-maps-streamableHTTP","api_id":"maps_direction_walking","data":{"origin": "116.481028,39.989643", "destination": "116.465302,40.004717"}}'
```
##### MCP
```
npx onekey mcp amap-maps-streamableHTTP
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-amap-maps-streamableHTTP":{
      "url":"https://agent.deepnlp.org/mcp?server_name=amap-maps-streamableHTTP&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="amap-maps-streamableHTTP/amap-maps-streamableHTTP", api_id="maps_direction_walking", data={"origin": "116.481028,39.989643", "destination": "116.465302,40.004717"})
```

#### maps_distance
Description: 测量两个经纬度坐标之间的距离,支持驾车、步行以及球面距离测量
## Parameters
- origins: string — 起点经度，纬度，可以传多个坐标，使用竖线隔离，比如120,30|120,31，坐标格式为：经度，纬度
- destination: string — 终点经度，纬度，坐标格式为：经度，纬度
- type: string — 距离测量类型,1代表驾车距离测量，0代表直线距离测量，3步行距离测量
##### CLI
```
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_distance '{"origins": "116.481028,39.989643|116.465302,40.004717", "destination": "116.481028,39.989643", "type": "1"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"amap-maps-streamableHTTP/amap-maps-streamableHTTP","api_id":"maps_distance","data":{"origins": "116.481028,39.989643|116.465302,40.004717", "destination": "116.481028,39.989643", "type": "1"}}'
```
##### MCP
```
npx onekey mcp amap-maps-streamableHTTP
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-amap-maps-streamableHTTP":{
      "url":"https://agent.deepnlp.org/mcp?server_name=amap-maps-streamableHTTP&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="amap-maps-streamableHTTP/amap-maps-streamableHTTP", api_id="maps_distance", data={"origins": "116.481028,39.989643|116.465302,40.004717", "destination": "116.481028,39.989643", "type": "1"})
```

#### maps_geo
Description: 将详细的结构化地址转换为经纬度坐标。支持对地标性名胜景区、建筑物名称解析为经纬度坐标
## Parameters
- address: string — 待解析的结构化地址信息
- city: string — 指定查询的城市
##### CLI
```
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_geo '{"address": "Beijing Capital Airport", "city": "北京"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"amap-maps-streamableHTTP/amap-maps-streamableHTTP","api_id":"maps_geo","data":{"address": "Beijing Capital Airport", "city": "北京"}}'
```
##### MCP
```
npx onekey mcp amap-maps-streamableHTTP
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-amap-maps-streamableHTTP":{
      "url":"https://agent.deepnlp.org/mcp?server_name=amap-maps-streamableHTTP&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="amap-maps-streamableHTTP/amap-maps-streamableHTTP", api_id="maps_geo", data={"address": "Beijing Capital Airport", "city": "北京"})
```

#### maps_regeocode
Description: 将一个高德经纬度坐标转换为行政区划地址信息
## Parameters
- location: string — 经纬度
##### CLI
```
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_regeocode '{"location": "116.481488,39.990464"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"amap-maps-streamableHTTP/amap-maps-streamableHTTP","api_id":"maps_regeocode","data":{"location": "116.481488,39.990464"}}'
```
##### MCP
```
npx onekey mcp amap-maps-streamableHTTP
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-amap-maps-streamableHTTP":{
      "url":"https://agent.deepnlp.org/mcp?server_name=amap-maps-streamableHTTP&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="amap-maps-streamableHTTP/amap-maps-streamableHTTP", api_id="maps_regeocode", data={"location": "116.481488,39.990464"})
```

#### maps_ip_location
Description: IP 定位根据用户输入的 IP 地址，定位 IP 的所在位置
## Parameters
- ip: string — IP地址
##### CLI
```
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_ip_location '{"ip": "8.8.8.8"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"amap-maps-streamableHTTP/amap-maps-streamableHTTP","api_id":"maps_ip_location","data":{"ip": "8.8.8.8"}}'
```
##### MCP
```
npx onekey mcp amap-maps-streamableHTTP
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-amap-maps-streamableHTTP":{
      "url":"https://agent.deepnlp.org/mcp?server_name=amap-maps-streamableHTTP&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="amap-maps-streamableHTTP/amap-maps-streamableHTTP", api_id="maps_ip_location", data={"ip": "8.8.8.8"})
```

#### maps_schema_personal_map
Description: 用于行程规划结果在高德地图展示。将行程规划位置点按照行程顺序填入lineList，返回结果为高德地图打开的URI链接，该结果不需总结，直接返回！
## Parameters
- orgName: string — 行程规划地图小程序名称
- lineList: array — 行程列表
##### CLI
```
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_schema_personal_map '{"orgName": "Weekend Trip", "lineList": [{"title": "Day1", "pointInfoList": [{"name": "Tiananmen", "lon": 116.3975, "lat": 39.9087, "poiId": "B000A8UIN8"}]}]}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"amap-maps-streamableHTTP/amap-maps-streamableHTTP","api_id":"maps_schema_personal_map","data":{"orgName": "Weekend Trip", "lineList": [{"title": "Day1", "pointInfoList": [{"name": "Tiananmen", "lon": 116.3975, "lat": 39.9087, "poiId": "B000A8UIN8"}]}]}}'
```
##### MCP
```
npx onekey mcp amap-maps-streamableHTTP
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-amap-maps-streamableHTTP":{
      "url":"https://agent.deepnlp.org/mcp?server_name=amap-maps-streamableHTTP&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="amap-maps-streamableHTTP/amap-maps-streamableHTTP", api_id="maps_schema_personal_map", data={"orgName": "Weekend Trip", "lineList": [{"title": "Day1", "pointInfoList": [{"name": "Tiananmen", "lon": 116.3975, "lat": 39.9087, "poiId": "B000A8UIN8"}]}]})
```

#### maps_around_search
Description: 周边搜，根据用户传入关键词以及坐标location，搜索出radius半径范围的POI
## Parameters
- keywords: string — 搜索关键词
- location: string — 中心点经度纬度
- radius: string — 搜索半径
- strategy: integer — 召回策略，0=默认召回策略，1=优先召回扫街榜POI (default: 0)
##### CLI
```
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_around_search '{"keywords": "coffee", "location": "116.481488,39.990464", "radius": "2000"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"amap-maps-streamableHTTP/amap-maps-streamableHTTP","api_id":"maps_around_search","data":{"keywords": "coffee", "location": "116.481488,39.990464", "radius": "2000"}}'
```
##### MCP
```
npx onekey mcp amap-maps-streamableHTTP
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-amap-maps-streamableHTTP":{
      "url":"https://agent.deepnlp.org/mcp?server_name=amap-maps-streamableHTTP&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="amap-maps-streamableHTTP/amap-maps-streamableHTTP", api_id="maps_around_search", data={"keywords": "coffee", "location": "116.481488,39.990464", "radius": "2000"})
```

#### maps_search_detail
Description: 查询关键词搜或者周边搜获取到的POI ID的详细信息
## Parameters
- id: string — 关键词搜或者周边搜获取到的POI ID
##### CLI
```
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_search_detail '{"id": "B0FFFABCD1"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"amap-maps-streamableHTTP/amap-maps-streamableHTTP","api_id":"maps_search_detail","data":{"id": "B0FFFABCD1"}}'
```
##### MCP
```
npx onekey mcp amap-maps-streamableHTTP
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-amap-maps-streamableHTTP":{
      "url":"https://agent.deepnlp.org/mcp?server_name=amap-maps-streamableHTTP&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="amap-maps-streamableHTTP/amap-maps-streamableHTTP", api_id="maps_search_detail", data={"id": "B0FFFABCD1"})
```

#### maps_text_search
Description: 关键字搜索 API 根据用户输入的关键字进行 POI 搜索，并返回相关的信息
## Parameters
- keywords: string — 查询关键字
- city: string — 查询城市
- citylimit: boolean — 是否限制城市范围内搜索，默认不限制 (default: False)
##### CLI
```
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_text_search '{"keywords": "Tsinghua University", "city": "北京", "citylimit": true}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"amap-maps-streamableHTTP/amap-maps-streamableHTTP","api_id":"maps_text_search","data":{"keywords": "Tsinghua University", "city": "北京", "citylimit": true}}'
```
##### MCP
```
npx onekey mcp amap-maps-streamableHTTP
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-amap-maps-streamableHTTP":{
      "url":"https://agent.deepnlp.org/mcp?server_name=amap-maps-streamableHTTP&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="amap-maps-streamableHTTP/amap-maps-streamableHTTP", api_id="maps_text_search", data={"keywords": "Tsinghua University", "city": "北京", "citylimit": true})
```

#### maps_schema_navi
Description: Schema唤醒客户端-导航页面，用于根据用户输入终点信息，返回一个拼装好的客户端唤醒URI，用户点击该URI即可唤起对应的客户端APP。唤起客户端后，会自动跳转到导航页面。
## Parameters
- lon: string — 终点经度
- lat: string — 终点纬度
##### CLI
```
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_schema_navi '{"lon": "116.3975", "lat": "39.9087"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"amap-maps-streamableHTTP/amap-maps-streamableHTTP","api_id":"maps_schema_navi","data":{"lon": "116.3975", "lat": "39.9087"}}'
```
##### MCP
```
npx onekey mcp amap-maps-streamableHTTP
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-amap-maps-streamableHTTP":{
      "url":"https://agent.deepnlp.org/mcp?server_name=amap-maps-streamableHTTP&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="amap-maps-streamableHTTP/amap-maps-streamableHTTP", api_id="maps_schema_navi", data={"lon": "116.3975", "lat": "39.9087"})
```

#### maps_schema_take_taxi
Description: 根据用户输入的起点和终点信息，返回一个拼装好的客户端唤醒URI，直接唤起高德地图进行打车。直接展示生成的链接，不需要总结
## Parameters
- slon: string — 起点经度
- slat: string — 起点纬度
- sname: string — 起点名称
- dlon: string — 终点经度
- dlat: string — 终点纬度
- dname: string — 终点名称
##### CLI
```
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_schema_take_taxi '{"slon": "116.3975", "slat": "39.9087", "sname": "Tiananmen", "dlon": "116.481028", "dlat": "39.989643", "dname": "Sanlitun"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"amap-maps-streamableHTTP/amap-maps-streamableHTTP","api_id":"maps_schema_take_taxi","data":{"slon": "116.3975", "slat": "39.9087", "sname": "Tiananmen", "dlon": "116.481028", "dlat": "39.989643", "dname": "Sanlitun"}}'
```
##### MCP
```
npx onekey mcp amap-maps-streamableHTTP
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-amap-maps-streamableHTTP":{
      "url":"https://agent.deepnlp.org/mcp?server_name=amap-maps-streamableHTTP&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="amap-maps-streamableHTTP/amap-maps-streamableHTTP", api_id="maps_schema_take_taxi", data={"slon": "116.3975", "slat": "39.9087", "sname": "Tiananmen", "dlon": "116.481028", "dlat": "39.989643", "dname": "Sanlitun"})
```

#### maps_weather
Description: 根据城市名称或者标准adcode查询指定城市的天气
## Parameters
- city: string — 城市名称或者adcode
##### CLI
```
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_weather '{"city": "北京"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"amap-maps-streamableHTTP/amap-maps-streamableHTTP","api_id":"maps_weather","data":{"city": "北京"}}'
```
##### MCP
```
npx onekey mcp amap-maps-streamableHTTP
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-amap-maps-streamableHTTP":{
      "url":"https://agent.deepnlp.org/mcp?server_name=amap-maps-streamableHTTP&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill amap-maps-streamableHTTP
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="amap-maps-streamableHTTP/amap-maps-streamableHTTP", api_id="maps_weather", data={"city": "北京"})
```
