---
name: mcp-server-chart
description: Auto-generated skill for mcp-server-chart tools via OneKey Gateway.
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


# mcp-server-chart Skill
Use the OneKey Gateway to access tools for this server via a unified access key.
## Quick Start
Set your OneKey access key:
```bash
export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_API_KEY
```
If no key is provided, the scripts fall back to the demo key `BETA_TEST_KEY_MARCH_2026`.
Common settings:
- `unique_id`: `mcp-server-chart/mcp-server-chart`
- `api_id`: one of the tools listed below
## Tools
### `generate_area_chart`
Generate a area chart to show data trends under continuous independent variables and observe the overall data trend, such as, displacement = velocity (average or instantaneous) × time: s = v × t. If the x-axis is time (t) and the y-axis is velocity (v) at each moment, an area chart allows you to observe the trend of velocity over time and infer the distance traveled by the area's size.

Parameters:
- `data` (array of object, required): Data for area chart, it should be an array of objects, each object contains a `time` field and a `value` field, such as, [{ time: '2015', value: 23 }, { time: '2016', value: 32 }], when stacking is needed for area, the data should contain a `group` field, such as, [{ time: '2015', value: 23, group: 'A' }, { time: '2015', value: 32, group: 'B' }].
- `data[].time` (string, required):
- `data[].value` (number, required):
- `data[].group` (string, optional):
- `stack` (boolean, optional): Whether stacking is enabled. When enabled, area charts require a 'group' field in the data.
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.palette` (array of string, optional): Color palette for the chart, it is a collection of colors.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `style.lineWidth` (number, optional): Line width for the lines of chart, such as 4.
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
- `axisXTitle` (string, optional): Set the x-axis title of chart.
- `axisYTitle` (string, optional): Set the y-axis title of chart.
### `generate_bar_chart`
Generate a horizontal bar chart to show data for numerical comparisons among different categories, such as, comparing categorical data and for horizontal comparisons.

Parameters:
- `data` (array of object, required): Data for bar chart, such as, [{ category: '分类一', value: 10 }, { category: '分类二', value: 20 }], when grouping or stacking is needed for bar, the data should contain a `group` field, such as, when [{ category: '北京', value: 825, group: '油车' }, { category: '北京', value: 1000, group: '电车' }].
- `data[].category` (string, required):
- `data[].value` (number, required):
- `data[].group` (string, optional):
- `group` (boolean, optional): Whether grouping is enabled. When enabled, bar charts require a 'group' field in the data. When `group` is true, `stack` should be false.
- `stack` (boolean, optional): Whether stacking is enabled. When enabled, bar charts require a 'group' field in the data. When `stack` is true, `group` should be false.
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.palette` (array of string, optional): Color palette for the chart, it is a collection of colors.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
- `axisXTitle` (string, optional): Set the x-axis title of chart.
- `axisYTitle` (string, optional): Set the y-axis title of chart.
### `generate_boxplot_chart`
Generate a boxplot chart to show data for statistical summaries among different categories, such as, comparing the distribution of data points across categories.

Parameters:
- `data` (array of object, required): Data for boxplot chart, such as, [{ category: '分类一', value: 10 }] or [{ category: '分类二', value: 20, group: '组别一' }].
- `data[].category` (string, required): Category of the data point, such as '分类一'.
- `data[].value` (number, required): Value of the data point, such as 10.
- `data[].group` (string, optional): Optional group for the data point, used for grouping in the boxplot.
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.palette` (array of string, optional): Color palette for the chart, it is a collection of colors.
- `style.startAtZero` (boolean, optional): Whether to start the axis at zero, optional, default is false.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
- `axisXTitle` (string, optional): Set the x-axis title of chart.
- `axisYTitle` (string, optional): Set the y-axis title of chart.
### `generate_column_chart`
Generate a column chart, which are best for comparing categorical data, such as, when values are close, column charts are preferable because our eyes are better at judging height than other visual elements like area or angles.

Parameters:
- `data` (array of object, required): Data for column chart, such as, [{ category: 'Category A', value: 10 }, { category: 'Category B', value: 20 }], when grouping or stacking is needed for column, the data should contain a 'group' field, such as, [{ category: 'Beijing', value: 825, group: 'Gas Car' }, { category: 'Beijing', value: 1000, group: 'Electric Car' }].
- `data[].category` (string, required):
- `data[].value` (number, required):
- `data[].group` (string, optional):
- `group` (boolean, optional): Whether grouping is enabled. When enabled, column charts require a 'group' field in the data. When `group` is true, `stack` should be false.
- `stack` (boolean, optional): Whether stacking is enabled. When enabled, column charts require a 'group' field in the data. When `stack` is true, `group` should be false.
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.palette` (array of string, optional): Color palette for the chart, it is a collection of colors.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
- `axisXTitle` (string, optional): Set the x-axis title of chart.
- `axisYTitle` (string, optional): Set the y-axis title of chart.
### `generate_district_map`
Generates regional distribution maps, which are usually used to show the administrative divisions and coverage of a dataset. It is not suitable for showing the distribution of specific locations, such as urban administrative divisions, GDP distribution maps of provinces and cities across the country, etc. This tool is limited to generating data maps within China.

Parameters:
- `title` (string, required): The map title should not exceed 16 characters. The content should be consistent with the information the map wants to convey and should be accurate, rich, creative, and attractive.
- `data` (object, required): Administrative division data, lower-level administrative divisions are optional. There are usually two scenarios: one is to simply display the regional composition, only `fillColor` needs to be configured, and all administrative divisions are consistent, representing that all blocks are connected as one; the other is the regional data distribution scenario, first determine the `dataType`, `dataValueUnit` and `dataLabel` configurations, `dataValue` should be a meaningful value and consistent with the meaning of dataType, and then determine the style configuration. The `fillColor` configuration represents the default fill color for areas without data. Lower-level administrative divisions do not need `fillColor` configuration, and their fill colors are determined by the `colors` configuration (If `dataType` is "number", only one base color (warm color) is needed in the list to calculate the continuous data mapping color band; if `dataType` is "enum", the number of color values in the list is equal to the number of enumeration values (contrast colors)). If `subdistricts` has a value, `showAllSubdistricts` must be set to true. For example, {"title": "陕西省地级市分布图", "data": {"name": "陕西省", "showAllSubdistricts": true, "dataLabel": "城市", "dataType": "enum", "colors": ["#4ECDC4", "#A5D8FF"], "subdistricts": [{"name": "西安市", "dataValue": "省会"}, {"name": "宝鸡市", "dataValue": "地级市"}, {"name": "咸阳市", "dataValue": "地级市"}, {"name": "铜川市", "dataValue": "地级市"}, {"name": "渭南市", "dataValue": "地级市"}, {"name": "延安市", "dataValue": "地级市"}, {"name": "榆林市", "dataValue": "地级市"}, {"name": "汉中市", "dataValue": "地级市"}, {"name": "安康市", "dataValue": "地级市"}, {"name": "商洛市", "dataValue": "地级市"}]}, "width": 1000, "height": 1000}.
- `data.name` (string, required): Keywords for the Chinese name of an administrative region (must be within China), and must be one of China, province, city, district, or county. The name should be more specific and add attributive descriptions, for example, "西安市" is better than "西安", "杭州西湖区" is better than "西湖区". It cannot be a specific place name or a vague name, such as "其它".
- `data.style` (object, optional): Style settings.
- `data.style.fillColor` (string, optional): Fill color, rgb or rgba format.
- `data.colors` (array of string, optional): Data color list, in rgb or rgba format.
- `data.dataType` (string, optional): The type of the data value, numeric or enumeration type Values: number, enum
- `data.dataLabel` (string, optional): Data label, such as "GDP"
- `data.dataValue` (string, optional): Data value, numeric string or enumeration string.
- `data.dataValueUnit` (string, optional): Data unit, such as "万亿"
- `data.showAllSubdistricts` (boolean, optional): Whether to display all subdistricts.
- `data.subdistricts` (array of object, optional): Sub-administrative regions are used to display the regional composition or regional distribution of related data.
- `data.subdistricts[].name` (string, required): Keywords for the Chinese name of an administrative region (must be within China), and must be one of China, province, city, district, or county. The name should be more specific and add attributive descriptions, for example, "西安市" is better than "西安", "杭州西湖区" is better than "西湖区". It cannot be a specific place name or a vague name, such as "其它".
- `data.subdistricts[].dataValue` (string, optional): Data value, numeric string or enumeration string.
- `data.subdistricts[].style` (object, optional): Style settings.
- `data.subdistricts[].style.fillColor` (string, optional): Fill color, rgb or rgba format.
- `width` (number, optional): Set the width of map, default is 1600.
- `height` (number, optional): Set the height of map, default is 1000.
### `generate_dual_axes_chart`
Generate a dual axes chart which is a combination chart that integrates two different chart types, typically combining a bar chart with a line chart to display both the trend and comparison of data, such as, the trend of sales and profit over time.

Parameters:
- `categories` (array of string, required): Categories for dual axes chart, such as, ['2015', '2016', '2017'].
- `series` (array of object, required): Series for dual axes chart, such as, [{ type: 'column', data: [91.9, 99.1, 101.6, 114.4, 121], axisYTitle: '销售额' }, { type: 'line', data: [0.055, 0.06, 0.062, 0.07, 0.075], 'axisYTitle': '利润率' }].
- `series[].type` (string, required): The optional value can be 'column' or 'line'. Values: column, line
- `series[].data` (array of number, required): When type is column, the data represents quantities, such as [91.9, 99.1, 101.6, 114.4, 121]. When type is line, the data represents ratios and its values are recommended to be less than 1, such as [0.055, 0.06, 0.062, 0.07, 0.075].
- `series[].axisYTitle` (string, optional): Set the y-axis title of the chart series, such as, axisYTitle: '销售额'.
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.palette` (array of string, optional): Color palette for the chart, it is a collection of colors.
- `style.startAtZero` (boolean, optional): Whether to start the axis at zero, optional, default is false.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
- `axisXTitle` (string, optional): Set the x-axis title of chart.
### `generate_fishbone_diagram`
Generate a fishbone diagram chart to uses a fish skeleton, like structure to display the causes or effects of a core problem, with the problem as the fish head and the causes/effects as the fish bones. It suits problems that can be split into multiple related factors.

Parameters:
- `data` (object, required): Data for fishbone diagram chart which is a hierarchical structure, such as, { name: 'main topic', children: [{ name: 'topic 1', children: [{ name: 'subtopic 1-1' }] }] }, and the maximum depth is 3.
- `data.name` (string, required):
- `data.children` (array of object, optional):
- `data.children[].name` (string, required):
- `data.children[].children` (array of object, optional):
- `data.children[].children[].name` (string, required):
- `data.children[].children[].children` (array of object, optional):
- `data.children[].children[].children[].name` (string, required):
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
### `generate_flow_diagram`
Generate a flow diagram chart to show the steps and decision points of a process or system, such as, scenarios requiring linear process presentation.

Parameters:
- `data` (object, required): Data for flow diagram chart, such as, { nodes: [{ name: 'node1' }, { name: 'node2' }], edges: [{ source: 'node1', target: 'node2', name: 'edge1' }] }.
- `data.nodes` (array of object, required):
- `data.nodes[].name` (string, required):
- `data.edges` (array of object, required):
- `data.edges[].source` (string, required):
- `data.edges[].target` (string, required):
- `data.edges[].name` (string, optional):
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
### `generate_funnel_chart`
Generate a funnel chart to visualize the progressive reduction of data as it passes through stages, such as, the conversion rates of users from visiting a website to completing a purchase.

Parameters:
- `data` (array of object, required): Data for funnel chart, such as, [{ category: '浏览网站', value: 50000 }, { category: '放入购物车', value: 35000 }, { category: '生成订单', value: 25000 }, { category: '支付订单', value: 15000 }, { category: '完成交易', value: 8000 }].
- `data[].category` (string, required):
- `data[].value` (number, required):
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.palette` (array of string, optional): Color palette for the chart, it is a collection of colors.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
### `generate_histogram_chart`
Generate a histogram chart to show the frequency of data points within a certain range. It can observe data distribution, such as, normal and skewed distributions, and identify data concentration areas and extreme points.

Parameters:
- `data` (array of number, required): Data for histogram chart, it should be an array of numbers, such as, [78, 88, 60, 100, 95].
- `binNumber` (number, optional): Number of intervals to define the number of intervals in a histogram, when not specified, a built-in value will be used.
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.palette` (array of string, optional): Color palette for the chart, it is a collection of colors.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
- `axisXTitle` (string, optional): Set the x-axis title of chart.
- `axisYTitle` (string, optional): Set the y-axis title of chart.
### `generate_line_chart`
Generate a line chart to show trends over time, such as, the ratio of Apple computer sales to Apple's profits changed from 2000 to 2016.

Parameters:
- `data` (array of object, required): Data for line chart, it should be an array of objects, each object contains a `time` field and a `value` field, such as, [{ time: '2015', value: 23 }, { time: '2016', value: 32 }], when the data is grouped by time, the `group` field should be used to specify the group, such as, [{ time: '2015', value: 23, group: 'A' }, { time: '2015', value: 32, group: 'B' }].
- `data[].time` (string, required):
- `data[].value` (number, required):
- `data[].group` (string, optional):
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.palette` (array of string, optional): Color palette for the chart, it is a collection of colors.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `style.startAtZero` (boolean, optional): Whether to start the axis at zero, optional, default is false.
- `style.lineWidth` (number, optional): Line width for the lines of chart, such as 4.
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
- `axisXTitle` (string, optional): Set the x-axis title of chart.
- `axisYTitle` (string, optional): Set the y-axis title of chart.
### `generate_liquid_chart`
Generate a liquid chart to visualize a single value as a percentage, such as, the current occupancy rate of a reservoir or the completion percentage of a project.

Parameters:
- `percent` (number, required): The percentage value to display in the liquid chart, should be a number between 0 and 1, where 1 represents 100%. For example, 0.75 represents 75%.
- `shape` (string, optional): The shape of the liquid chart, can be 'circle', 'rect', 'pin', or 'triangle'. Default is 'circle'. Values: circle, rect, pin, triangle
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `style.color` (string, optional): Custom color for the liquid chart, if not specified, defaults to the theme color.
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
### `generate_mind_map`
Generate a mind map chart to organizes and presents information in a hierarchical structure with branches radiating from a central topic, such as, a diagram showing the relationship between a main topic and its subtopics.

Parameters:
- `data` (object, required): Data for mind map chart which is a hierarchical structure, such as, { name: 'main topic', children: [{ name: 'topic 1', children: [{ name:'subtopic 1-1' }] }, and the maximum depth is 3.
- `data.name` (string, required):
- `data.children` (array of object, optional):
- `data.children[].name` (string, required):
- `data.children[].children` (array of object, optional):
- `data.children[].children[].name` (string, required):
- `data.children[].children[].children` (array of object, optional):
- `data.children[].children[].children[].name` (string, required):
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
### `generate_network_graph`
Generate a network graph chart to show relationships (edges) between entities (nodes), such as, relationships between people in social networks.

Parameters:
- `data` (object, required): Data for network graph chart, such as, { nodes: [{ name: 'node1' }, { name: 'node2' }], edges: [{ source: 'node1', target: 'node2', name: 'edge1' }] }
- `data.nodes` (array of object, required):
- `data.nodes[].name` (string, required):
- `data.edges` (array of object, required):
- `data.edges[].source` (string, required):
- `data.edges[].target` (string, required):
- `data.edges[].name` (string, optional):
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
### `generate_organization_chart`
Generate an organization chart to visualize the hierarchical structure of an organization, such as, a diagram showing the relationship between a CEO and their direct reports.

Parameters:
- `data` (object, required): Data for organization chart which is a hierarchical structure, such as, { name: 'CEO', description: 'Chief Executive Officer', children: [{ name: 'CTO', description: 'Chief Technology Officer', children: [{ name: 'Dev Manager', description: 'Development Manager' }] }] }, and the maximum depth is 3.
- `data.name` (string, required):
- `data.description` (string, optional):
- `data.children` (array of object, optional):
- `data.children[].name` (string, required):
- `data.children[].description` (string, optional):
- `data.children[].children` (array of object, optional):
- `data.children[].children[].name` (string, required):
- `data.children[].children[].description` (string, optional):
- `data.children[].children[].children` (array of object, optional):
- `data.children[].children[].children[].name` (string, required):
- `data.children[].children[].children[].description` (string, optional):
- `orient` (string, optional): Orientation of the organization chart, either horizontal or vertical. Default is vertical, when the level of the chart is more than 3, it is recommended to use horizontal orientation. Values: horizontal, vertical
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
### `generate_path_map`
Generate a route map to display the user's planned route, such as travel guide routes.

Parameters:
- `title` (string, required): The map title should not exceed 16 characters. The content should be consistent with the information the map wants to convey and should be accurate, rich, creative, and attractive.
- `data` (array of object, required): Routes, each group represents all POIs along a route. For example, [{ "data": ["西安钟楼", "西安大唐不夜城", "西安大雁塔"] }, { "data": ["西安曲江池公园", "西安回民街"] }]
- `data[].data` (array of string, required): A list of keywords for the names of points of interest (POIs) in Chinese. These POIs usually contain a group of places with similar locations, so the names should be more descriptive, must adding attributives to indicate that they are different places in the same area, such as "北京市" is better than "北京", "杭州西湖" is better than "西湖"; in addition, if you can determine that a location may appear in multiple areas, you can be more specific, such as "杭州西湖的苏堤春晓" is better than "苏堤春晓". The tool will use these keywords to search for specific POIs and query their detailed data, such as latitude and longitude, location photos, etc. For example, ["西安钟楼", "西安大唐不夜城", "西安大雁塔"].
- `width` (number, optional): Set the width of map, default is 1600.
- `height` (number, optional): Set the height of map, default is 1000.
### `generate_pie_chart`
Generate a pie chart to show the proportion of parts, such as, market share and budget allocation.

Parameters:
- `data` (array of object, required): Data for pie chart, it should be an array of objects, each object contains a `category` field and a `value` field, such as, [{ category: '分类一', value: 27 }].
- `data[].category` (string, required):
- `data[].value` (number, required):
- `innerRadius` (number, optional): Set the innerRadius of pie chart, the value between 0 and 1. Set the pie chart as a donut chart. Set the value to 0.6 or number in [0 ,1] to enable it.
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.palette` (array of string, optional): Color palette for the chart, it is a collection of colors.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
### `generate_pin_map`
Generate a point map to display the location and distribution of point data on the map, such as the location distribution of attractions, hospitals, supermarkets, etc.

Parameters:
- `title` (string, required): The map title should not exceed 16 characters. The content should be consistent with the information the map wants to convey and should be accurate, rich, creative, and attractive.
- `data` (array of string, required): A list of keywords for the names of points of interest (POIs) in Chinese. These POIs usually contain a group of places with similar locations, so the names should be more descriptive, must adding attributives to indicate that they are different places in the same area, such as "北京市" is better than "北京", "杭州西湖" is better than "西湖"; in addition, if you can determine that a location may appear in multiple areas, you can be more specific, such as "杭州西湖的苏堤春晓" is better than "苏堤春晓". The tool will use these keywords to search for specific POIs and query their detailed data, such as latitude and longitude, location photos, etc. For example, ["西安钟楼", "西安大唐不夜城", "西安大雁塔"].
- `markerPopup` (object, optional): Marker type, one is simple mode, which is just an icon and does not require `markerPopup` configuration; the other is image mode, which displays location photos and requires `markerPopup` configuration. Among them, `width`/`height`/`borderRadius` can be combined to realize rectangular photos and square photos. In addition, when `borderRadius` is half of the width and height, it can also be a circular photo.
- `markerPopup.type` (string, optional): Must be "image".
- `markerPopup.width` (number, optional): Width of the photo.
- `markerPopup.height` (number, optional): Height of the photo.
- `markerPopup.borderRadius` (number, optional): Border radius of the photo.
- `width` (number, optional): Set the width of map, default is 1600.
- `height` (number, optional): Set the height of map, default is 1000.
### `generate_radar_chart`
Generate a radar chart to display multidimensional data (four dimensions or more), such as, evaluate Huawei and Apple phones in terms of five dimensions: ease of use, functionality, camera, benchmark scores, and battery life.

Parameters:
- `data` (array of object, required): Data for radar chart, it should be an array of objects, each object contains a `name` field and a `value` field, such as, [{ name: 'Design', value: 70 }], when the data is grouped by `group`, the `group` field is required, such as, [{ name: 'Design', value: 70, group: 'Huawei' }].
- `data[].name` (string, required):
- `data[].value` (number, required):
- `data[].group` (string, optional):
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.palette` (array of string, optional): Color palette for the chart, it is a collection of colors.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `style.lineWidth` (number, optional): Line width for the lines of chart, such as 4.
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
### `generate_sankey_chart`
Generate a sankey chart to visualize the flow of data between different stages or categories, such as, the user journey from landing on a page to completing a purchase.

Parameters:
- `data` (array of object, required): Date for sankey chart, such as, [{ source: 'Landing Page', target: 'Product Page', value: 50000 }, { source: 'Product Page', target: 'Add to Cart', value: 35000 }, { source: 'Add to Cart', target: 'Checkout', value: 25000 }, { source: 'Checkout', target: 'Payment', value: 15000 }, { source: 'Payment', target: 'Purchase Completed', value: 8000 }].
- `data[].source` (string, required):
- `data[].target` (string, required):
- `data[].value` (number, required):
- `nodeAlign` (string, optional): Alignment of nodes in the sankey chart, such as, 'left', 'right', 'justify', or 'center'. Values: left, right, justify, center
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.palette` (array of string, optional): Color palette for the chart, it is a collection of colors.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
### `generate_scatter_chart`
Generate a scatter chart to show the relationship between two variables, helps discover their relationship or trends, such as, the strength of correlation, data distribution patterns.

Parameters:
- `data` (array of object, required): Data for scatter chart, such as, [{ x: 10, y: 15 }], when the data is grouped, the group name can be specified in the `group` field, such as, [{ x: 10, y: 15, group: 'Group A' }].
- `data[].x` (number, required):
- `data[].y` (number, required):
- `data[].group` (string, optional): Group name for the data point.
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.palette` (array of string, optional): Color palette for the chart, it is a collection of colors.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
- `axisXTitle` (string, optional): Set the x-axis title of chart.
- `axisYTitle` (string, optional): Set the y-axis title of chart.
### `generate_treemap_chart`
Generate a treemap chart to display hierarchical data and can intuitively show comparisons between items at the same level, such as, show disk space usage with treemap.

Parameters:
- `data` (array of object, required): Data for treemap chart which is a hierarchical structure, such as, [{ name: 'Design', value: 70, children: [{ name: 'Tech', value: 20 }] }], and the maximum depth is 3.
- `data[].name` (string, required):
- `data[].value` (number, required):
- `data[].children` (array of object, optional):
- `data[].children[].name` (string, required):
- `data[].children[].value` (number, required):
- `data[].children[].children` (array of object, optional):
- `data[].children[].children[].name` (string, required):
- `data[].children[].children[].value` (number, required):
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.palette` (array of string, optional): Color palette for the chart, it is a collection of colors.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
### `generate_venn_chart`
Generate a Venn diagram to visualize the relationships between different sets, showing how they intersect and overlap, such as the commonalities and differences between various groups.

Parameters:
- `data` (array of object, required): Data for venn chart, such as, [{ label: 'A', value: 10, sets: ['A'] }, { label: 'B', value: 20, sets: ['B'] }, { label: 'C', value: 30, sets: ['C'] }, { label: 'AB', value: 5, sets: ['A', 'B'] }].
- `data[].label` (string, optional): Label for the venn chart segment, such as 'A', 'B', or 'C'.
- `data[].value` (number, required): Value for the venn chart segment, such as 10, 20, or 30.
- `data[].sets` (array of string, required): Array of set names that this segment belongs to, such as ['A', 'B'] for an intersection between sets A and B.
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.palette` (array of string, optional): Color palette for the chart, it is a collection of colors.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
### `generate_violin_chart`
Generate a violin chart to show data for statistical summaries among different categories, such as, comparing the distribution of data points across categories.

Parameters:
- `data` (array of object, required): Data for violin chart, such as, [{ category: 'Category A', value: 10 }], when the data is grouped, the 'group' field is required, such as, [{ category: 'Category B', value: 20, group: 'Group A' }].
- `data[].category` (string, required): Category of the data point, such as '分类一'.
- `data[].value` (number, required): Value of the data point, such as 10.
- `data[].group` (string, optional): Optional group for the data point, used for grouping in the violin chart.
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.palette` (array of string, optional): Color palette for the chart, it is a collection of colors.
- `style.startAtZero` (boolean, optional): Whether to start the axis at zero, optional, default is false.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
- `axisXTitle` (string, optional): Set the x-axis title of chart.
- `axisYTitle` (string, optional): Set the y-axis title of chart.
### `generate_waterfall_chart`
Generate a waterfall chart to visualize the cumulative effect of sequentially introduced positive or negative values, such as showing how an initial value is affected by a series of intermediate positive or negative values leading to a final result. Waterfall charts are ideal for financial analysis, budget tracking, profit and loss statements, and understanding the composition of changes over time or categories.

Parameters:
- `data` (array of object, required): Data for waterfall chart, it should be an array of objects. Each object must contain a `category` field. For regular items, a `value` field is also required. The `isIntermediateTotal` field marks intermediate subtotals, and the `isTotal` field marks the final total. For example, [{ category: 'Initial', value: 100 }, { category: 'Increase', value: 50 }, { category: 'Subtotal', isIntermediateTotal: true }, { category: 'Decrease', value: -30 }, { category: 'Total', isTotal: true }].
- `data[].category` (string, required):
- `data[].value` (number, optional):
- `data[].isIntermediateTotal` (boolean, optional):
- `data[].isTotal` (boolean, optional):
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `style.palette` (object, optional):
- `style.palette.positiveColor` (string, optional): Color for positive values (increases). Default is '#FF4D4F'.
- `style.palette.negativeColor` (string, optional): Color for negative values (decreases). Default is '#2EBB59'.
- `style.palette.totalColor` (string, optional): Color for total and intermediate total bars. Default is '#1783FF'.
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
- `axisXTitle` (string, optional): Set the x-axis title of chart.
- `axisYTitle` (string, optional): Set the y-axis title of chart.
### `generate_word_cloud_chart`
Generate a word cloud chart to show word frequency or weight through text size variation, such as, analyzing common words in social media, reviews, or feedback.

Parameters:
- `data` (array of object, required): Data for word cloud chart, it should be an array of objects, each object contains a `text` field and a `value` field, such as, [{ value: 4.272, text: '形成' }].
- `data[].text` (string, required):
- `data[].value` (number, required):
- `style` (object, optional): Style configuration for the chart with a JSON object, optional.
- `style.backgroundColor` (string, optional): Background color of the chart, such as, '#fff'.
- `style.palette` (array of string, optional): Color palette for the chart, it is a collection of colors.
- `style.texture` (string, optional): Set the texture for the chart, optional, default is 'default'. 'rough' refers to hand-drawn style. Values: default, rough
- `theme` (string, optional): Set the theme for the chart, optional, default is 'default'. Values: default, academy, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.
- `title` (string, optional): Set the title of chart.
### `generate_spreadsheet`
Generate a spreadsheet or pivot table for displaying tabular data. When 'rows' or 'values' fields are provided, it renders as a pivot table (cross-tabulation); otherwise, it renders as a regular table. Useful for displaying structured data, comparing values across categories, and creating data summaries.

Parameters:
- `data` (array of object, required): Data for spreadsheet, an array of objects where each object represents a row. Keys are column names and values can be string, number, or null. Such as, [{ name: 'John', age: 30 }, { name: 'Jane', age: 25 }].
- `rows` (array of string, optional): Row header fields for pivot table. When 'rows' or 'values' is provided, the spreadsheet will be rendered as a pivot table.
- `columns` (array of string, optional): Column header fields, used to specify the order of columns. For regular tables, this determines column order; for pivot tables, this is used for column grouping.
- `values` (array of string, optional): Value fields for pivot table. When 'rows' or 'values' is provided, the spreadsheet will be rendered as a pivot table.
- `theme` (string, optional): Set the theme for the spreadsheet, optional, default is 'default'. Values: default, dark
- `width` (number, optional): Set the width of chart, default is 600.
- `height` (number, optional): Set the height of chart, default is 400.

# Usage
## CLI

### generate_area_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_area_chart '{}'
```

### generate_bar_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_bar_chart '{}'
```

### generate_boxplot_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_boxplot_chart '{}'
```

### generate_column_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_column_chart '{}'
```

### generate_district_map
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_district_map '{}'
```

### generate_dual_axes_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_dual_axes_chart '{}'
```

### generate_fishbone_diagram
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_fishbone_diagram '{}'
```

### generate_flow_diagram
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_flow_diagram '{}'
```

### generate_funnel_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_funnel_chart '{}'
```

### generate_histogram_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_histogram_chart '{}'
```

### generate_line_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_line_chart '{}'
```

### generate_liquid_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_liquid_chart '{}'
```

### generate_mind_map
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_mind_map '{}'
```

### generate_network_graph
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_network_graph '{}'
```

### generate_organization_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_organization_chart '{}'
```

### generate_path_map
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_path_map '{}'
```

### generate_pie_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_pie_chart '{}'
```

### generate_pin_map
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_pin_map '{}'
```

### generate_radar_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_radar_chart '{}'
```

### generate_sankey_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_sankey_chart '{}'
```

### generate_scatter_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_scatter_chart '{}'
```

### generate_treemap_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_treemap_chart '{}'
```

### generate_venn_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_venn_chart '{}'
```

### generate_violin_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_violin_chart '{}'
```

### generate_waterfall_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_waterfall_chart '{}'
```

### generate_word_cloud_chart
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_word_cloud_chart '{}'
```

### generate_spreadsheet
```shell
npx onekey agent mcp-server-chart/mcp-server-chart generate_spreadsheet '{}'
```

## Scripts
Each tool has a dedicated script in this folder:
- `skills/mcp-server-chart/scripts/generate_area_chart.py`
- `skills/mcp-server-chart/scripts/generate_bar_chart.py`
- `skills/mcp-server-chart/scripts/generate_boxplot_chart.py`
- `skills/mcp-server-chart/scripts/generate_column_chart.py`
- `skills/mcp-server-chart/scripts/generate_district_map.py`
- `skills/mcp-server-chart/scripts/generate_dual_axes_chart.py`
- `skills/mcp-server-chart/scripts/generate_fishbone_diagram.py`
- `skills/mcp-server-chart/scripts/generate_flow_diagram.py`
- `skills/mcp-server-chart/scripts/generate_funnel_chart.py`
- `skills/mcp-server-chart/scripts/generate_histogram_chart.py`
- `skills/mcp-server-chart/scripts/generate_line_chart.py`
- `skills/mcp-server-chart/scripts/generate_liquid_chart.py`
- `skills/mcp-server-chart/scripts/generate_mind_map.py`
- `skills/mcp-server-chart/scripts/generate_network_graph.py`
- `skills/mcp-server-chart/scripts/generate_organization_chart.py`
- `skills/mcp-server-chart/scripts/generate_path_map.py`
- `skills/mcp-server-chart/scripts/generate_pie_chart.py`
- `skills/mcp-server-chart/scripts/generate_pin_map.py`
- `skills/mcp-server-chart/scripts/generate_radar_chart.py`
- `skills/mcp-server-chart/scripts/generate_sankey_chart.py`
- `skills/mcp-server-chart/scripts/generate_scatter_chart.py`
- `skills/mcp-server-chart/scripts/generate_treemap_chart.py`
- `skills/mcp-server-chart/scripts/generate_venn_chart.py`
- `skills/mcp-server-chart/scripts/generate_violin_chart.py`
- `skills/mcp-server-chart/scripts/generate_waterfall_chart.py`
- `skills/mcp-server-chart/scripts/generate_word_cloud_chart.py`
- `skills/mcp-server-chart/scripts/generate_spreadsheet.py`
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
