## Charts - mcp-server-chart/mcp-server-chart

### Skill: mcp-server-chart
#### generate_area_chart
Description: Generate a area chart to show data trends under continuous independent variables and observe the overall data trend, such as, displacement = velocity (average or instantaneous) × time: s = v × t. If the x-axis is time (t) and the y-axis is velocity (v) at each moment, an area chart allows you to observe the trend of velocity over time and infer the distance traveled by the area's size.
## Parameters
- data: array — Data for area chart, it should be an array of objects, each object contains a `time` field and a `value` field, such as, [{ time: '2015', value: 23 }, { time: '2016', value: 32 }], when stacking is needed for area, the data should contain a `group` field, such as, [{ time: '2015', value: 23, group: 'A' }, { time: '2015', value: 32, group: 'B' }].
- stack: boolean — Whether stacking is enabled. When enabled, area charts require a 'group' field in the data. (default: False)
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
- axisXTitle: string — Set the x-axis title of chart. (default: )
- axisYTitle: string — Set the y-axis title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_area_chart '{"data": [{"time": "2026-01", "value": 1200}, {"time": "2026-02", "value": 1500}], "title": "Visitors"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_area_chart","data":{"data": [{"time": "2026-01", "value": 1200}, {"time": "2026-02", "value": 1500}], "title": "Visitors"}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_area_chart", data={"data": [{"time": "2026-01", "value": 1200}, {"time": "2026-02", "value": 1500}], "title": "Visitors"})
```

#### generate_bar_chart
Description: Generate a horizontal bar chart to show data for numerical comparisons among different categories, such as, comparing categorical data and for horizontal comparisons.
## Parameters
- data: array — Data for bar chart, such as, [{ category: '分类一', value: 10 }, { category: '分类二', value: 20 }], when grouping or stacking is needed for bar, the data should contain a `group` field, such as, when [{ category: '北京', value: 825, group: '油车' }, { category: '北京', value: 1000, group: '电车' }].
- group: boolean — Whether grouping is enabled. When enabled, bar charts require a 'group' field in the data. When `group` is true, `stack` should be false. (default: False)
- stack: boolean — Whether stacking is enabled. When enabled, bar charts require a 'group' field in the data. When `stack` is true, `group` should be false. (default: True)
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
- axisXTitle: string — Set the x-axis title of chart. (default: )
- axisYTitle: string — Set the y-axis title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_bar_chart '{"data": [{"category": "East", "value": 120}, {"category": "West", "value": 150}], "title": "Sales"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_bar_chart","data":{"data": [{"category": "East", "value": 120}, {"category": "West", "value": 150}], "title": "Sales"}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_bar_chart", data={"data": [{"category": "East", "value": 120}, {"category": "West", "value": 150}], "title": "Sales"})
```

#### generate_boxplot_chart
Description: Generate a boxplot chart to show data for statistical summaries among different categories, such as, comparing the distribution of data points across categories.
## Parameters
- data: array — Data for boxplot chart, such as, [{ category: '分类一', value: 10 }] or [{ category: '分类二', value: 20, group: '组别一' }].
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
- axisXTitle: string — Set the x-axis title of chart. (default: )
- axisYTitle: string — Set the y-axis title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_boxplot_chart '{"data": [{"value": 10}, {"value": 20}, {"value": 30}], "title": "Latency"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_boxplot_chart","data":{"data": [{"value": 10}, {"value": 20}, {"value": 30}], "title": "Latency"}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_boxplot_chart", data={"data": [{"value": 10}, {"value": 20}, {"value": 30}], "title": "Latency"})
```

#### generate_column_chart
Description: Generate a column chart, which are best for comparing categorical data, such as, when values are close, column charts are preferable because our eyes are better at judging height than other visual elements like area or angles.
## Parameters
- data: array — Data for column chart, such as, [{ category: 'Category A', value: 10 }, { category: 'Category B', value: 20 }], when grouping or stacking is needed for column, the data should contain a 'group' field, such as, [{ category: 'Beijing', value: 825, group: 'Gas Car' }, { category: 'Beijing', value: 1000, group: 'Electric Car' }].
- group: boolean — Whether grouping is enabled. When enabled, column charts require a 'group' field in the data. When `group` is true, `stack` should be false. (default: True)
- stack: boolean — Whether stacking is enabled. When enabled, column charts require a 'group' field in the data. When `stack` is true, `group` should be false. (default: False)
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
- axisXTitle: string — Set the x-axis title of chart. (default: )
- axisYTitle: string — Set the y-axis title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_column_chart '{"data": [{"category": "Jan", "value": 400}, {"category": "Feb", "value": 520}], "title": "Signups"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_column_chart","data":{"data": [{"category": "Jan", "value": 400}, {"category": "Feb", "value": 520}], "title": "Signups"}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_column_chart", data={"data": [{"category": "Jan", "value": 400}, {"category": "Feb", "value": 520}], "title": "Signups"})
```

#### generate_district_map
Description: Generates regional distribution maps, which are usually used to show the administrative divisions and coverage of a dataset. It is not suitable for showing the distribution of specific locations, such as urban administrative divisions, GDP distribution maps of provinces and cities across the country, etc. This tool is limited to generating data maps within China.
## Parameters
- title: string — The map title should not exceed 16 characters. The content should be consistent with the information the map wants to convey and should be accurate, rich, creative, and attractive.
- data: object — Administrative division data, lower-level administrative divisions are optional. There are usually two scenarios: one is to simply display the regional composition, only `fillColor` needs to be configured, and all administrative divisions are consistent, representing that all blocks are connected as one; the other is the regional data distribution scenario, first determine the `dataType`, `dataValueUnit` and `dataLabel` configurations, `dataValue` should be a meaningful value and consistent with the meaning of dataType, and then determine the style configuration. The `fillColor` configuration represents the default fill color for areas without data. Lower-level administrative divisions do not need `fillColor` configuration, and their fill colors are determined by the `colors` configuration (If `dataType` is "number", only one base color (warm color) is needed in the list to calculate the continuous data mapping color band; if `dataType` is "enum", the number of color values in the list is equal to the number of enumeration values (contrast colors)). If `subdistricts` has a value, `showAllSubdistricts` must be set to true. For example, {"title": "陕西省地级市分布图", "data": {"name": "陕西省", "showAllSubdistricts": true, "dataLabel": "城市", "dataType": "enum", "colors": ["#4ECDC4", "#A5D8FF"], "subdistricts": [{"name": "西安市", "dataValue": "省会"}, {"name": "宝鸡市", "dataValue": "地级市"}, {"name": "咸阳市", "dataValue": "地级市"}, {"name": "铜川市", "dataValue": "地级市"}, {"name": "渭南市", "dataValue": "地级市"}, {"name": "延安市", "dataValue": "地级市"}, {"name": "榆林市", "dataValue": "地级市"}, {"name": "汉中市", "dataValue": "地级市"}, {"name": "安康市", "dataValue": "地级市"}, {"name": "商洛市", "dataValue": "地级市"}]}, "width": 1000, "height": 1000}.
- width: number — Set the width of map, default is 1600. (default: 1600)
- height: number — Set the height of map, default is 1000. (default: 1000)
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_district_map '{"data": [{"name": "Beijing", "value": 2000}], "title": "Users"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_district_map","data":{"data": [{"name": "Beijing", "value": 2000}], "title": "Users"}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_district_map", data={"data": [{"name": "Beijing", "value": 2000}], "title": "Users"})
```

#### generate_dual_axes_chart
Description: Generate a dual axes chart which is a combination chart that integrates two different chart types, typically combining a bar chart with a line chart to display both the trend and comparison of data, such as, the trend of sales and profit over time.
## Parameters
- categories: array — Categories for dual axes chart, such as, ['2015', '2016', '2017'].
- series: array — Series for dual axes chart, such as, [{ type: 'column', data: [91.9, 99.1, 101.6, 114.4, 121], axisYTitle: '销售额' }, { type: 'line', data: [0.055, 0.06, 0.062, 0.07, 0.075], 'axisYTitle': '利润率' }].
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
- axisXTitle: string — Set the x-axis title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_dual_axes_chart '{"data": [{"time": "Jan", "value": 100, "value2": 20}], "title": "Revenue vs Profit"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_dual_axes_chart","data":{"data": [{"time": "Jan", "value": 100, "value2": 20}], "title": "Revenue vs Profit"}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_dual_axes_chart", data={"data": [{"time": "Jan", "value": 100, "value2": 20}], "title": "Revenue vs Profit"})
```

#### generate_fishbone_diagram
Description: Generate a fishbone diagram chart to uses a fish skeleton, like structure to display the causes or effects of a core problem, with the problem as the fish head and the causes/effects as the fish bones. It suits problems that can be split into multiple related factors.
## Parameters
- data: object — Data for fishbone diagram chart which is a hierarchical structure, such as, { name: 'main topic', children: [{ name: 'topic 1', children: [{ name: 'subtopic 1-1' }] }] }, and the maximum depth is 3.
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_fishbone_diagram '{"data": {"problem": "Bug", "causes": ["People", "Process", "Tools"]}}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_fishbone_diagram","data":{"data": {"problem": "Bug", "causes": ["People", "Process", "Tools"]}}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_fishbone_diagram", data={"data": {"problem": "Bug", "causes": ["People", "Process", "Tools"]}})
```

#### generate_flow_diagram
Description: Generate a flow diagram chart to show the steps and decision points of a process or system, such as, scenarios requiring linear process presentation.
## Parameters
- data: object — Data for flow diagram chart, such as, { nodes: [{ name: 'node1' }, { name: 'node2' }], edges: [{ source: 'node1', target: 'node2', name: 'edge1' }] }.
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_flow_diagram '{"data": {"nodes": ["Landing", "Signup", "Pay"]}}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_flow_diagram","data":{"data": {"nodes": ["Landing", "Signup", "Pay"]}}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_flow_diagram", data={"data": {"nodes": ["Landing", "Signup", "Pay"]}})
```

#### generate_funnel_chart
Description: Generate a funnel chart to visualize the progressive reduction of data as it passes through stages, such as, the conversion rates of users from visiting a website to completing a purchase.
## Parameters
- data: array — Data for funnel chart, such as, [{ category: '浏览网站', value: 50000 }, { category: '放入购物车', value: 35000 }, { category: '生成订单', value: 25000 }, { category: '支付订单', value: 15000 }, { category: '完成交易', value: 8000 }].
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_funnel_chart '{"data": [{"stage": "Visit", "value": 1000}, {"stage": "Checkout", "value": 200}], "title": "Conversion"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_funnel_chart","data":{"data": [{"stage": "Visit", "value": 1000}, {"stage": "Checkout", "value": 200}], "title": "Conversion"}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_funnel_chart", data={"data": [{"stage": "Visit", "value": 1000}, {"stage": "Checkout", "value": 200}], "title": "Conversion"})
```

#### generate_histogram_chart
Description: Generate a histogram chart to show the frequency of data points within a certain range. It can observe data distribution, such as, normal and skewed distributions, and identify data concentration areas and extreme points.
## Parameters
- data: array — Data for histogram chart, it should be an array of numbers, such as, [78, 88, 60, 100, 95].
- binNumber: number — Number of intervals to define the number of intervals in a histogram, when not specified, a built-in value will be used.
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
- axisXTitle: string — Set the x-axis title of chart. (default: )
- axisYTitle: string — Set the y-axis title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_histogram_chart '{"data": [50, 60, 70, 80, 90], "title": "Scores"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_histogram_chart","data":{"data": [50, 60, 70, 80, 90], "title": "Scores"}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_histogram_chart", data={"data": [50, 60, 70, 80, 90], "title": "Scores"})
```

#### generate_line_chart
Description: Generate a line chart to show trends over time, such as, the ratio of Apple computer sales to Apple's profits changed from 2000 to 2016.
## Parameters
- data: array — Data for line chart, it should be an array of objects, each object contains a `time` field and a `value` field, such as, [{ time: '2015', value: 23 }, { time: '2016', value: 32 }], when the data is grouped by time, the `group` field should be used to specify the group, such as, [{ time: '2015', value: 23, group: 'A' }, { time: '2015', value: 32, group: 'B' }].
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
- axisXTitle: string — Set the x-axis title of chart. (default: )
- axisYTitle: string — Set the y-axis title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_line_chart '{"data": [{"time": "t1", "value": 30}, {"time": "t2", "value": 45}], "title": "CPU"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_line_chart","data":{"data": [{"time": "t1", "value": 30}, {"time": "t2", "value": 45}], "title": "CPU"}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_line_chart", data={"data": [{"time": "t1", "value": 30}, {"time": "t2", "value": 45}], "title": "CPU"})
```

#### generate_liquid_chart
Description: Generate a liquid chart to visualize a single value as a percentage, such as, the current occupancy rate of a reservoir or the completion percentage of a project.
## Parameters
- percent: number — The percentage value to display in the liquid chart, should be a number between 0 and 1, where 1 represents 100%. For example, 0.75 represents 75%.
- shape: string — The shape of the liquid chart, can be 'circle', 'rect', 'pin', or 'triangle'. Default is 'circle'. (default: circle)
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_liquid_chart '{"data": 0.76, "title": "Completion"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_liquid_chart","data":{"data": 0.76, "title": "Completion"}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_liquid_chart", data={"data": 0.76, "title": "Completion"})
```

#### generate_mind_map
Description: Generate a mind map chart to organizes and presents information in a hierarchical structure with branches radiating from a central topic, such as, a diagram showing the relationship between a main topic and its subtopics.
## Parameters
- data: object — Data for mind map chart which is a hierarchical structure, such as, { name: 'main topic', children: [{ name: 'topic 1', children: [{ name:'subtopic 1-1' }] }, and the maximum depth is 3.
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_mind_map '{"data": {"title": "Project Plan", "nodes": ["Research", "Design", "Build"]}}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_mind_map","data":{"data": {"title": "Project Plan", "nodes": ["Research", "Design", "Build"]}}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_mind_map", data={"data": {"title": "Project Plan", "nodes": ["Research", "Design", "Build"]}})
```

#### generate_network_graph
Description: Generate a network graph chart to show relationships (edges) between entities (nodes), such as, relationships between people in social networks.
## Parameters
- data: object — Data for network graph chart, such as, { nodes: [{ name: 'node1' }, { name: 'node2' }], edges: [{ source: 'node1', target: 'node2', name: 'edge1' }] }
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_network_graph '{"data": [{"source": "A", "target": "B", "value": 1}]}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_network_graph","data":{"data": [{"source": "A", "target": "B", "value": 1}]}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_network_graph", data={"data": [{"source": "A", "target": "B", "value": 1}]})
```

#### generate_organization_chart
Description: Generate an organization chart to visualize the hierarchical structure of an organization, such as, a diagram showing the relationship between a CEO and their direct reports.
## Parameters
- data: object — Data for organization chart which is a hierarchical structure, such as, { name: 'CEO', description: 'Chief Executive Officer', children: [{ name: 'CTO', description: 'Chief Technology Officer', children: [{ name: 'Dev Manager', description: 'Development Manager' }] }] }, and the maximum depth is 3.
- orient: string — Orientation of the organization chart, either horizontal or vertical. Default is vertical, when the level of the chart is more than 3, it is recommended to use horizontal orientation. (default: vertical)
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_organization_chart '{"data": {"name": "CEO", "children": [{"name": "CTO"}]}}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_organization_chart","data":{"data": {"name": "CEO", "children": [{"name": "CTO"}]}}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_organization_chart", data={"data": {"name": "CEO", "children": [{"name": "CTO"}]}})
```

#### generate_path_map
Description: Generate a route map to display the user's planned route, such as travel guide routes.
## Parameters
- title: string — The map title should not exceed 16 characters. The content should be consistent with the information the map wants to convey and should be accurate, rich, creative, and attractive.
- data: array — Routes, each group represents all POIs along a route. For example, [{ "data": ["西安钟楼", "西安大唐不夜城", "西安大雁塔"] }, { "data": ["西安曲江池公园", "西安回民街"] }]
- width: number — Set the width of map, default is 1600. (default: 1600)
- height: number — Set the height of map, default is 1000. (default: 1000)
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_path_map '{"data": [{"lng": 116.39, "lat": 39.9}, {"lng": 121.47, "lat": 31.23}]}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_path_map","data":{"data": [{"lng": 116.39, "lat": 39.9}, {"lng": 121.47, "lat": 31.23}]}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_path_map", data={"data": [{"lng": 116.39, "lat": 39.9}, {"lng": 121.47, "lat": 31.23}]})
```

#### generate_pie_chart
Description: Generate a pie chart to show the proportion of parts, such as, market share and budget allocation.
## Parameters
- data: array — Data for pie chart, it should be an array of objects, each object contains a `category` field and a `value` field, such as, [{ category: '分类一', value: 27 }].
- innerRadius: number — Set the innerRadius of pie chart, the value between 0 and 1. Set the pie chart as a donut chart. Set the value to 0.6 or number in [0 ,1] to enable it. (default: 0)
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_pie_chart '{"data": [{"type": "A", "value": 40}, {"type": "B", "value": 30}], "title": "Market Share"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_pie_chart","data":{"data": [{"type": "A", "value": 40}, {"type": "B", "value": 30}], "title": "Market Share"}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_pie_chart", data={"data": [{"type": "A", "value": 40}, {"type": "B", "value": 30}], "title": "Market Share"})
```

#### generate_pin_map
Description: Generate a point map to display the location and distribution of point data on the map, such as the location distribution of attractions, hospitals, supermarkets, etc.
## Parameters
- title: string — The map title should not exceed 16 characters. The content should be consistent with the information the map wants to convey and should be accurate, rich, creative, and attractive.
- data: array — A list of keywords for the names of points of interest (POIs) in Chinese. These POIs usually contain a group of places with similar locations, so the names should be more descriptive, must adding attributives to indicate that they are different places in the same area, such as "北京市" is better than "北京", "杭州西湖" is better than "西湖"; in addition, if you can determine that a location may appear in multiple areas, you can be more specific, such as "杭州西湖的苏堤春晓" is better than "苏堤春晓". The tool will use these keywords to search for specific POIs and query their detailed data, such as latitude and longitude, location photos, etc. For example, ["西安钟楼", "西安大唐不夜城", "西安大雁塔"].
- markerPopup: object — Marker type, one is simple mode, which is just an icon and does not require `markerPopup` configuration; the other is image mode, which displays location photos and requires `markerPopup` configuration. Among them, `width`/`height`/`borderRadius` can be combined to realize rectangular photos and square photos. In addition, when `borderRadius` is half of the width and height, it can also be a circular photo.
- width: number — Set the width of map, default is 1600. (default: 1600)
- height: number — Set the height of map, default is 1000. (default: 1000)
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_pin_map '{"data": [{"name": "NYC", "lng": -74.0, "lat": 40.7}]}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_pin_map","data":{"data": [{"name": "NYC", "lng": -74.0, "lat": 40.7}]}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_pin_map", data={"data": [{"name": "NYC", "lng": -74.0, "lat": 40.7}]})
```

#### generate_radar_chart
Description: Generate a radar chart to display multidimensional data (four dimensions or more), such as, evaluate Huawei and Apple phones in terms of five dimensions: ease of use, functionality, camera, benchmark scores, and battery life.
## Parameters
- data: array — Data for radar chart, it should be an array of objects, each object contains a `name` field and a `value` field, such as, [{ name: 'Design', value: 70 }], when the data is grouped by `group`, the `group` field is required, such as, [{ name: 'Design', value: 70, group: 'Huawei' }].
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_radar_chart '{"data": [{"item": "JS", "score": 80}, {"item": "Python", "score": 90}]}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_radar_chart","data":{"data": [{"item": "JS", "score": 80}, {"item": "Python", "score": 90}]}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_radar_chart", data={"data": [{"item": "JS", "score": 80}, {"item": "Python", "score": 90}]})
```

#### generate_sankey_chart
Description: Generate a sankey chart to visualize the flow of data between different stages or categories, such as, the user journey from landing on a page to completing a purchase.
## Parameters
- data: array — Date for sankey chart, such as, [{ source: 'Landing Page', target: 'Product Page', value: 50000 }, { source: 'Product Page', target: 'Add to Cart', value: 35000 }, { source: 'Add to Cart', target: 'Checkout', value: 25000 }, { source: 'Checkout', target: 'Payment', value: 15000 }, { source: 'Payment', target: 'Purchase Completed', value: 8000 }].
- nodeAlign: string — Alignment of nodes in the sankey chart, such as, 'left', 'right', 'justify', or 'center'. (default: center)
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_sankey_chart '{"data": [{"source": "Coal", "target": "Electricity", "value": 40}]}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_sankey_chart","data":{"data": [{"source": "Coal", "target": "Electricity", "value": 40}]}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_sankey_chart", data={"data": [{"source": "Coal", "target": "Electricity", "value": 40}]})
```

#### generate_scatter_chart
Description: Generate a scatter chart to show the relationship between two variables, helps discover their relationship or trends, such as, the strength of correlation, data distribution patterns.
## Parameters
- data: array — Data for scatter chart, such as, [{ x: 10, y: 15 }], when the data is grouped, the group name can be specified in the `group` field, such as, [{ x: 10, y: 15, group: 'Group A' }].
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
- axisXTitle: string — Set the x-axis title of chart. (default: )
- axisYTitle: string — Set the y-axis title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_scatter_chart '{"data": [{"x": 170, "y": 65}, {"x": 180, "y": 80}]}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_scatter_chart","data":{"data": [{"x": 170, "y": 65}, {"x": 180, "y": 80}]}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_scatter_chart", data={"data": [{"x": 170, "y": 65}, {"x": 180, "y": 80}]})
```

#### generate_treemap_chart
Description: Generate a treemap chart to display hierarchical data and can intuitively show comparisons between items at the same level, such as, show disk space usage with treemap.
## Parameters
- data: array — Data for treemap chart which is a hierarchical structure, such as, [{ name: 'Design', value: 70, children: [{ name: 'Tech', value: 20 }] }], and the maximum depth is 3.
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_treemap_chart '{"data": [{"name": "Tech", "value": 60}]}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_treemap_chart","data":{"data": [{"name": "Tech", "value": 60}]}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_treemap_chart", data={"data": [{"name": "Tech", "value": 60}]})
```

#### generate_venn_chart
Description: Generate a Venn diagram to visualize the relationships between different sets, showing how they intersect and overlap, such as the commonalities and differences between various groups.
## Parameters
- data: array — Data for venn chart, such as, [{ label: 'A', value: 10, sets: ['A'] }, { label: 'B', value: 20, sets: ['B'] }, { label: 'C', value: 30, sets: ['C'] }, { label: 'AB', value: 5, sets: ['A', 'B'] }].
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_venn_chart '{"data": [{"sets": ["A"], "size": 10}, {"sets": ["B"], "size": 8}, {"sets": ["A", "B"], "size": 3}]}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_venn_chart","data":{"data": [{"sets": ["A"], "size": 10}, {"sets": ["B"], "size": 8}, {"sets": ["A", "B"], "size": 3}]}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_venn_chart", data={"data": [{"sets": ["A"], "size": 10}, {"sets": ["B"], "size": 8}, {"sets": ["A", "B"], "size": 3}]})
```

#### generate_violin_chart
Description: Generate a violin chart to show data for statistical summaries among different categories, such as, comparing the distribution of data points across categories.
## Parameters
- data: array — Data for violin chart, such as, [{ category: 'Category A', value: 10 }], when the data is grouped, the 'group' field is required, such as, [{ category: 'Category B', value: 20, group: 'Group A' }].
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
- axisXTitle: string — Set the x-axis title of chart. (default: )
- axisYTitle: string — Set the y-axis title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_violin_chart '{"data": [1, 2, 3, 4, 5]}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_violin_chart","data":{"data": [1, 2, 3, 4, 5]}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_violin_chart", data={"data": [1, 2, 3, 4, 5]})
```

#### generate_waterfall_chart
Description: Generate a waterfall chart to visualize the cumulative effect of sequentially introduced positive or negative values, such as showing how an initial value is affected by a series of intermediate positive or negative values leading to a final result. Waterfall charts are ideal for financial analysis, budget tracking, profit and loss statements, and understanding the composition of changes over time or categories.
## Parameters
- data: array — Data for waterfall chart, it should be an array of objects. Each object must contain a `category` field. For regular items, a `value` field is also required. The `isIntermediateTotal` field marks intermediate subtotals, and the `isTotal` field marks the final total. For example, [{ category: 'Initial', value: 100 }, { category: 'Increase', value: 50 }, { category: 'Subtotal', isIntermediateTotal: true }, { category: 'Decrease', value: -30 }, { category: 'Total', isTotal: true }].
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
- axisXTitle: string — Set the x-axis title of chart. (default: )
- axisYTitle: string — Set the y-axis title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_waterfall_chart '{"data": [{"name": "Revenue", "value": 100}, {"name": "COGS", "value": -40}]}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_waterfall_chart","data":{"data": [{"name": "Revenue", "value": 100}, {"name": "COGS", "value": -40}]}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_waterfall_chart", data={"data": [{"name": "Revenue", "value": 100}, {"name": "COGS", "value": -40}]})
```

#### generate_word_cloud_chart
Description: Generate a word cloud chart to show word frequency or weight through text size variation, such as, analyzing common words in social media, reviews, or feedback.
## Parameters
- data: array — Data for word cloud chart, it should be an array of objects, each object contains a `text` field and a `value` field, such as, [{ value: 4.272, text: '形成' }].
- style: object — Style configuration for the chart with a JSON object, optional.
- theme: string — Set the theme for the chart, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
- title: string — Set the title of chart. (default: )
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_word_cloud_chart '{"data": [{"text": "AI", "weight": 10}, {"text": "Data", "weight": 8}]}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_word_cloud_chart","data":{"data": [{"text": "AI", "weight": 10}, {"text": "Data", "weight": 8}]}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_word_cloud_chart", data={"data": [{"text": "AI", "weight": 10}, {"text": "Data", "weight": 8}]})
```

#### generate_spreadsheet
Description: Generate a spreadsheet or pivot table for displaying tabular data. When 'rows' or 'values' fields are provided, it renders as a pivot table (cross-tabulation); otherwise, it renders as a regular table. Useful for displaying structured data, comparing values across categories, and creating data summaries.
## Parameters
- data: array — Data for spreadsheet, an array of objects where each object represents a row. Keys are column names and values can be string, number, or null. Such as, [{ name: 'John', age: 30 }, { name: 'Jane', age: 25 }].
- rows: array — Row header fields for pivot table. When 'rows' or 'values' is provided, the spreadsheet will be rendered as a pivot table.
- columns: array — Column header fields, used to specify the order of columns. For regular tables, this determines column order; for pivot tables, this is used for column grouping.
- values: array — Value fields for pivot table. When 'rows' or 'values' is provided, the spreadsheet will be rendered as a pivot table.
- theme: string — Set the theme for the spreadsheet, optional, default is 'default'. (default: default)
- width: number — Set the width of chart, default is 600. (default: 600)
- height: number — Set the height of chart, default is 400. (default: 400)
##### CLI
```
onekey agent mcp-server-chart/mcp-server-chart generate_spreadsheet '{"data": [["Item", "Cost"], ["Server", 100]]}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"mcp-server-chart/mcp-server-chart","api_id":"generate_spreadsheet","data":{"data": [["Item", "Cost"], ["Server", 100]]}}'
```
##### MCP
```
onekey mcp mcp-server-chart
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-mcp-server-chart":{
      "url":"https://agent.deepnlp.org/mcp?server_name=mcp-server-chart&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill mcp-server-chart -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill mcp-server-chart
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(unique_id="mcp-server-chart/mcp-server-chart", api_id="generate_spreadsheet", data={"data": [["Item", "Cost"], ["Server", 100]]})
```
