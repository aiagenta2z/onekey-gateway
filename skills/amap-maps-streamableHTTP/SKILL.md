---
name: amap-maps-streamableHTTP
description: Auto-generated skill for amap-maps-streamableHTTP tools via OneKey Gateway.
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

## Dependencies

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
Before executing any script in the scripts/ directory, ensure the dependencies are installed.

# amap-maps-streamableHTTP Skill
Use the OneKey Gateway to access tools for this server via a unified access key.
## Quick Start
Set your OneKey access key:
```bash
export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_API_KEY
```
If no key is provided, the scripts fall back to the demo key `BETA_TEST_KEY_MARCH_2026`.
Common settings:
- `unique_id`: `amap-maps-streamableHTTP/amap-maps-streamableHTTP`
- `api_id`: one of the tools listed below
## Tools
### `maps_direction_bicycling`
骑行路径规划用于规划骑行通勤方案，规划时会考虑天桥、单行线、封路等情况。最大支持 500km 的骑行路线规划

Parameters:
- `origin` (string, required): 出发点经纬度，坐标格式为：经度，纬度
- `destination` (string, required): 目的地经纬度，坐标格式为：经度，纬度
### `maps_direction_driving`
驾车路径规划 API 可以根据用户起终点经纬度坐标规划以小客车、轿车通勤出行的方案，并且返回通勤方案的数据。

Parameters:
- `origin` (string, required): 出发点经纬度，坐标格式为：经度，纬度
- `destination` (string, required): 目的地经纬度，坐标格式为：经度，纬度
### `maps_direction_transit_integrated`
根据用户起终点经纬度坐标规划综合各类公共（火车、公交、地铁）交通方式的通勤方案，并且返回通勤方案的数据，跨城场景下必须传起点城市与终点城市

Parameters:
- `origin` (string, required): 出发点经纬度，坐标格式为：经度，纬度
- `destination` (string, required): 目的地经纬度，坐标格式为：经度，纬度
- `city` (string, required): 公共交通规划起点城市
- `cityd` (string, required): 公共交通规划终点城市
### `maps_direction_walking`
根据输入起点终点经纬度坐标规划100km 以内的步行通勤方案，并且返回通勤方案的数据

Parameters:
- `origin` (string, required): 出发点经度，纬度，坐标格式为：经度，纬度
- `destination` (string, required): 目的地经度，纬度，坐标格式为：经度，纬度
### `maps_distance`
测量两个经纬度坐标之间的距离,支持驾车、步行以及球面距离测量

Parameters:
- `origins` (string, required): 起点经度，纬度，可以传多个坐标，使用竖线隔离，比如120,30|120,31，坐标格式为：经度，纬度
- `destination` (string, required): 终点经度，纬度，坐标格式为：经度，纬度
- `type` (string, optional): 距离测量类型,1代表驾车距离测量，0代表直线距离测量，3步行距离测量
### `maps_geo`
将详细的结构化地址转换为经纬度坐标。支持对地标性名胜景区、建筑物名称解析为经纬度坐标

Parameters:
- `address` (string, required): 待解析的结构化地址信息
- `city` (string, optional): 指定查询的城市
### `maps_regeocode`
将一个高德经纬度坐标转换为行政区划地址信息

Parameters:
- `location` (string, required): 经纬度
### `maps_ip_location`
IP 定位根据用户输入的 IP 地址，定位 IP 的所在位置

Parameters:
- `ip` (string, required): IP地址
### `maps_schema_personal_map`
用于行程规划结果在高德地图展示。将行程规划位置点按照行程顺序填入lineList，返回结果为高德地图打开的URI链接，该结果不需总结，直接返回！

Parameters:
- `orgName` (string, required): 行程规划地图小程序名称
- `lineList` (array of object, required): 行程列表
- `lineList[].title` (string, required): 行程名称描述（按行程顺序）
- `lineList[].pointInfoList` (array of object, required): 行程目标位置点描述
- `lineList[].pointInfoList[].name` (string, required): 行程目标位置点名称
- `lineList[].pointInfoList[].lon` (number, required): 行程目标位置点经度
- `lineList[].pointInfoList[].lat` (number, required): 行程目标位置点纬度
- `lineList[].pointInfoList[].poiId` (string, required): 行程目标位置点POIID
### `maps_around_search`
周边搜，根据用户传入关键词以及坐标location，搜索出radius半径范围的POI

Parameters:
- `keywords` (string, required): 搜索关键词
- `location` (string, required): 中心点经度纬度
- `radius` (string, optional): 搜索半径
- `strategy` (integer, optional): 召回策略，0=默认召回策略，1=优先召回扫街榜POI
### `maps_search_detail`
查询关键词搜或者周边搜获取到的POI ID的详细信息

Parameters:
- `id` (string, required): 关键词搜或者周边搜获取到的POI ID
### `maps_text_search`
关键字搜索 API 根据用户输入的关键字进行 POI 搜索，并返回相关的信息

Parameters:
- `keywords` (string, required): 查询关键字
- `city` (string, optional): 查询城市
- `citylimit` (boolean, optional): 是否限制城市范围内搜索，默认不限制
### `maps_schema_navi`
Schema唤醒客户端-导航页面，用于根据用户输入终点信息，返回一个拼装好的客户端唤醒URI，用户点击该URI即可唤起对应的客户端APP。唤起客户端后，会自动跳转到导航页面。

Parameters:
- `lon` (string, required): 终点经度
- `lat` (string, required): 终点纬度
### `maps_schema_take_taxi`
根据用户输入的起点和终点信息，返回一个拼装好的客户端唤醒URI，直接唤起高德地图进行打车。直接展示生成的链接，不需要总结

Parameters:
- `slon` (string, optional): 起点经度
- `slat` (string, optional): 起点纬度
- `sname` (string, optional): 起点名称
- `dlon` (string, required): 终点经度
- `dlat` (string, required): 终点纬度
- `dname` (string, required): 终点名称
### `maps_weather`
根据城市名称或者标准adcode查询指定城市的天气

Parameters:
- `city` (string, required): 城市名称或者adcode

# Usage
## CLI

### maps_direction_bicycling
```shell
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_direction_bicycling '{"origin": "116.481028,39.989643", "destination": "116.465302,40.004717"}'
```

### maps_direction_driving
```shell
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_direction_driving '{"origin": "116.481028,39.989643", "destination": "116.465302,40.004717"}'
```

### maps_direction_transit_integrated
```shell
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_direction_transit_integrated '{"origin": "116.481028,39.989643", "destination": "116.465302,40.004717", "city": "北京", "cityd": "上海"}'
```

### maps_direction_walking
```shell
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_direction_walking '{"origin": "116.481028,39.989643", "destination": "116.465302,40.004717"}'
```

### maps_distance
```shell
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_distance '{"origins": "116.481028,39.989643|116.465302,40.004717", "destination": "116.481028,39.989643", "type": "1"}'
```

### maps_geo
```shell
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_geo '{"address": "Beijing Capital Airport", "city": "北京"}'
```

### maps_regeocode
```shell
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_regeocode '{"location": "116.481488,39.990464"}'
```

### maps_ip_location
```shell
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_ip_location '{"ip": "8.8.8.8"}'
```

### maps_schema_personal_map
```shell
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_schema_personal_map '{"orgName": "Weekend Trip", "lineList": [{"title": "Day1", "pointInfoList": [{"name": "Tiananmen", "lon": 116.3975, "lat": 39.9087, "poiId": "B000A8UIN8"}]}]}'
```

### maps_around_search
```shell
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_around_search '{"keywords": "coffee", "location": "116.481488,39.990464", "radius": "2000"}'
```

### maps_search_detail
```shell
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_search_detail '{"id": "B0FFFABCD1"}'
```

### maps_text_search
```shell
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_text_search '{"keywords": "Tsinghua University", "city": "北京", "citylimit": true}'
```

### maps_schema_navi
```shell
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_schema_navi '{"lon": "116.3975", "lat": "39.9087"}'
```

### maps_schema_take_taxi
```shell
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_schema_take_taxi '{"slon": "116.3975", "slat": "39.9087", "sname": "Tiananmen", "dlon": "116.481028", "dlat": "39.989643", "dname": "Sanlitun"}'
```

### maps_weather
```shell
npx onekey agent amap-maps-streamableHTTP/amap-maps-streamableHTTP maps_weather '{"city": "北京"}'
```

## Scripts
Each tool has a dedicated script in this folder:
- `skills/amap-maps-streamableHTTP/scripts/maps_direction_bicycling.py`
- `skills/amap-maps-streamableHTTP/scripts/maps_direction_driving.py`
- `skills/amap-maps-streamableHTTP/scripts/maps_direction_transit_integrated.py`
- `skills/amap-maps-streamableHTTP/scripts/maps_direction_walking.py`
- `skills/amap-maps-streamableHTTP/scripts/maps_distance.py`
- `skills/amap-maps-streamableHTTP/scripts/maps_geo.py`
- `skills/amap-maps-streamableHTTP/scripts/maps_regeocode.py`
- `skills/amap-maps-streamableHTTP/scripts/maps_ip_location.py`
- `skills/amap-maps-streamableHTTP/scripts/maps_schema_personal_map.py`
- `skills/amap-maps-streamableHTTP/scripts/maps_around_search.py`
- `skills/amap-maps-streamableHTTP/scripts/maps_search_detail.py`
- `skills/amap-maps-streamableHTTP/scripts/maps_text_search.py`
- `skills/amap-maps-streamableHTTP/scripts/maps_schema_navi.py`
- `skills/amap-maps-streamableHTTP/scripts/maps_schema_take_taxi.py`
- `skills/amap-maps-streamableHTTP/scripts/maps_weather.py`
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
