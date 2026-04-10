# FinanceAgent package

This is the official github repo of pypi package FinanceAgent(https://pypi.org/project/FinanceAgent/). This repo is intended to provide common financial API interface
to help develop Finance related AI Agents workflows. Since getting realtime or near-realtime finance data is crucial for success of AI Agents, 
we are building a common interface of open API to get public available data from glocal Finance Market (US, Europe, Asia) with multiple finance investment choices such as Stock, Index, Option, etc.
Getting Realtime Data maybe blocked by website and this repo is not responsible for proxy or any data correctness related issues.

### Agent Skills Usage

```shell
npm install -g @aiagenta2z/agtm
npx agtm skills add https://github.com/aiagenta2z/onekey-gateway  ## add all onekey router skills
npx agtm skills add aiagenta2z/onekey-gateway --skill hk-stock-market-hkex -g  ## install to global path
```

```shell
npx skills add https://github.com/aiagenta2z/onekey-gateway  ## add all onekey router skills
npx skills add aiagenta2z/onekey-gateway --skill hk-stock-market-hkex -g  ## install to global path
```


| Skills                                                                                     | API ID                                                                 | Description                                          |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------|
| hk-stock-market-hkex [Doc](skills/hk-stock-market-hkex/SKILL.md)                           | get_hk_stock_market_hkex                                               | Get HKEX HongKong Stock Exchange Market data         |
| cn-stock-market-shanghai-shenzhen [Doc](skills/cn-stock-market-shanghai-shenzhen/SKILL.md) | get_cn_stock_market_shanghai_shenzhen                                  | Get China Stock Market Shanghai and Shenzhen data    |
| us-stock-market-nyse-nasdaq-dow  [Doc](skills/us-stock-market-nyse-nasdaq-dow/SKILL.md)    | get_us_stock_market_nyse_nasdaq_dow                                    | Get US Stock Market Data and Index NYSE, NASDAQ, DOW |
| uk-stock-market-lse [Doc](skills/uk-stock-market-lse/SKILL.md)                             | get_uk_stock_market_lse                                                | Get UK Stock Market Data LSE                         |
| india-stock-market-nse-india  [Doc](skills/india-stock-market-nse-india/SKILL.md)          | get_india_stock_market_nse_india | Get India Stock Market Data NSE India                |


```
Show Tencent Stock Price
```


***IMPORTANT LEGAL DISCLAIMER***

FinanceAgent is not affiliated, endorsed, or vetted by Financial Institutions. It's an open-source tool that uses finance APIs to get realtime finance data to help build 
AI Agents and Finance Larget Language Models. Please contact the repo owner email if your API or data source need to be removed from the repo.



|  REGION  | MARKET| INVESTMENT TYPE | API DATA SOURCE   |
|  ----  | ----  | ----  | ----  | 
|  United Status  | US (NASDAQ,NYSE,DOW) | STOCK  | morningstar.com |
|  United Status  | US (NASDAQ,NYSE,DOW)  | STOCK  | zacks.com |
|  United Status  | US (NASDAQ,NYSE,DOW)  | STOCK  | marketbeat.com |
|  Asia  | HK (HKEX) | STOCK  | hkex.com |
|  Asia  | CN_MAINLAND (SHANGHAI SH, SHENZHEN SZ) | STOCK  | xueqiu.com |
|  Asia  | India (NSE) | STOCK  |  moneycontrol.com  |
|  Europe  | London (LSE) | STOCK  | stockanalysis.com |
|  Asia  | Toyko (TSE) | STOCK  | NA |


## Install
```
pip install FinanceAgent
```

## Usage

### Python Usage
```
import FinanceAgent as fa

## Hongkong Stock Exchange Tencent: 700, Kuaishou: 1024
hk_stock_info_json = fa.api(symbol_list=['700', '1024'], market="HK")

## Shanghai and Shenzhen Stock Market: SH600519: 贵州茅台(Maotai), SH600036: 招商银行 (China Merchants Bank)
cn_stock_info_json = fa.api(symbol_list=['SH600519', 'SH600036'], market="CN_MAINLAND")

## US Stock Market: Tesla (TSLA), Microsoft(MSFT), Google (GOOG)
us_stock_info_json = fa.api(symbol_list=['TSLA', 'MSFT', 'GOOG'], market="US")

## UK Stock Market: London Stock Exchange Market, Shell (quote: SHEL), Unilever (quote: ULVR)
lse_stock_info_json = fa.api(symbol_list=['SHEL', 'ULVR'], market="LSE")

## India NSE National Stock Exchange, Tata Motor(TM03), Infosys(IT)
india_stock_info_json = fa.api(symbol_list=['TM03', 'IT'], market="NSE_INDIA")


```


## Sample Output
```

#### HK Stock Info
-----------------------------------
symbol|1024
avg_price|49.650 HKD
high|50.950 HKD
low|47.600 HKD
previous_close|50.850 HKD
update_time|14 Oct 2024 18:33
market_capitalization|214.06 B HKD
pe_ratio|31.15
source|HKEX, https://www.hkex.com.hk/Market-Data/Securities-Prices/Equities/Equities-Quote?sym=1024&sc_lang=en
data_source|hkex.com
-----------------------------------
symbol|700
avg_price|436.000 HKD
high|440.800 HKD
low|424.000 HKD
previous_close|438.800 HKD
update_time|14 Oct 2024 18:33
market_capitalization|4,045.91 B HKD
pe_ratio|33.32
source|HKEX, https://www.hkex.com.hk/Market-Data/Securities-Prices/Equities/Equities-Quote?sym=700&sc_lang=en
data_source|hkex.com
-----------------------------------


#### CN MAINLAND Stock Info
-----------------------------------
symbol|SH600036
avg_price|39.265919080336076 CNY
high|39.8 CNY
low|38.69 CNY
previous_close|38.43 CNY
update_time|2024-10-14 15:00:00
market_capitalization|9918.97 亿 CNY
pe_ratio|
source|XUEQIU.COM, https://xueqiu.com/S/SH600036
data_source|xueqiu.com
-----------------------------------

symbol|SH600519
avg_price|1602.5501242724608 CNY
high|1620.63 CNY
low|1581.17 CNY
previous_close|1604.99 CNY
update_time|2024-10-14 15:00:00
market_capitalization|20124.16 亿 CNY
pe_ratio|
source|XUEQIU.COM, https://xueqiu.com/S/SH600519
data_source|xueqiu.com
-----------------------------------

#### London Stock Exchange LSE
-----------------------------------

symbol|SHEL
avg_price|2,592.00 GBP
high|2,599.29 GBP
low|2,577.50 GBP
previous_close|2,592.00 GBP
update_time|
market_capitalization|161.18B GBP
pe_ratio|11.70
source|stockanalysis.com,https://stockanalysis.com/quote/lon/SHEL
data_source|stockanalysis.com
-----------------------------------

symbol|ULVR
avg_price|4,806.00 GBP
high|4,827.00 GBP
low|4,792.00 GBP
previous_close|4,806.00 GBP
update_time|
market_capitalization|119.19B GBP
pe_ratio|21.57
source|stockanalysis.com,https://stockanalysis.com/quote/lon/ULVR
data_source|stockanalysis.com
-----------------------------------

#### US Stock Info
-----------------------------------
symbol|TSLA
avg_price|217.80 USD
high|223.34 USD
low|214.38 USD
previous_close|238.77 USD
update_time|
market_capitalization|695.79 Bil USD
pe_ratio|87.78
source|
data_source|morningstar.com
-----------------------------------

#### India Stock Market Info
-----------------------------------
symbol|IT
avg_price|1,958.70 INR
high|1,958.70 INR
low|1,958.70 INR
previous_close|1,958.70 INR
update_time|
market_capitalization|813,281.00 INR
pe_ratio|
source|moneycontrol.com,https://www.moneycontrol.comhttps://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT
data_source|moneycontrol.com
-----------------------------------
symbol|TM03
avg_price|928.05 INR
high|928.05 INR
low|928.05 INR
previous_close|928.05 INR
update_time|
market_capitalization|341,604.45 INR
pe_ratio|
source|moneycontrol.com,https://www.moneycontrol.comhttps://www.moneycontrol.com/india/stockpricequote/auto-lcvs-hcvs/tatamotors/TM03
data_source|moneycontrol.com
-----------------------------------
```

### API Usage

Get OneKey Gateway [Access Key](https://deepnlp.org/workspace/keys) and [Docs](https://www.deepnlp.org/doc/onekey_gateway).

```shell
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key

curl -v -X POST "https://agent.deepnlp.org/agent_router" \
-H "Content-Type: application/json" \
-H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
-d '{
  "unique_id": "aiagenta2z/financeagent",
  "api_id": "get_cn_stock_market_shanghai_shenzhen",
  "data": {
    "symbol_list": ["SH600519", "SH600036"]
  }
}'

```


### CLI Usage

```shell
## install onekey agent gateway
npm install @aiagenta2z/onekey-gateway
## CLI to Call API and Symbol List
npx onekey agent aiagenta2z/financeagent get_cn_stock_market_shanghai_shenzhen '{"symbol_list": ["SH600519", "SH600036"]}'
```


### MCP Server Usage

Finance Agent to Get Free API of Global Financial Marketplace. Try MCP Server (https://github.com/AI-Hub-Admin/finance-agent-mcp-server) on the MCP Tool Use Agent (https://agent.deepnlp.org/agent/mcp_tool_use)



## Introduction to Available API and Data Source 

|  REGION  | MARKET| DATA SOURCE   |  API Example |  Robots Verification  |
|  ----  | ----  | ----  | ----  | ----  | 
|  United Status  | US | morningstar.com |  https://www.morningstar.com/stocks/xnas/aapl/quote | YES |
|  United Status  | US | zacks.com |  https://www.zacks.com/stock/quote/aapl | YES |
|  United Status  | US | marketbeat.com |  https://www.marketbeat.com/stocks/NASDAQ/AAPL | YES |
|  Asia  | HK (HKEX)  | hkex.com | https://www.hkex.com.hk/Market-Data/Securities-Prices/Equities/Equities-Quote?sym=700&sc_lang=en | YES |
|  Asia  | CN_MAINLAND(SH and SHENZHEN) | xueqiu.com | https://xueqiu.com/S/SH600519 | YES |
|  Asia  | India (NSE) | https://www.moneycontrol.com | https://www.moneycontrol.com/india/stockpricequote/auto-lcvshcvs/tatamotors/TM03 | YES |
|  Asia  | Japan (TSE) |   xxx |  |  |
|  Europe  | London (LSE) | stockanalysis.com | https://stockanalysis.com/stocks/shel/ | YES |


## Related

### Related Code and Docs
[OneKey Gateway GitHub](https://github.com/aiagenta2z/onekey-gateway)   
[OneKey Gateway Doc](https://www.deepnlp.org/doc/onekey_gateway)    
[Agtm GitHub](https://github.com/aiagenta2z/agtm)     
[AI Agent Marketplace](https://www.deepnlp.org/store/ai-agent)     
[MCP Marketplace](https://www.deepnlp.org/store/ai-agent/mcp-server)    
[Skills Marketplace](https://www.deepnlp.org/store/skills)    

## Related Blogs
[Introduction to multimodal generative models](http://www.deepnlp.org/blog/introduction-to-multimodal-generative-models) <br>
[Generative AI Search Engine Optimization](http://www.deepnlp.org/blog/generative-ai-search-engine-optimization-how-to-improve-your-content) <br>
[AI Image Generator User Reviews](http://www.deepnlp.org/store/image-generator) <br>
[AI Video Generator User Reviews](http://www.deepnlp.org/store/video-generator) <br>
[AI Chatbot & Assistant Reviews](http://www.deepnlp.org/store/chatbot-assistant) <br>
[AI Store-Best AI Tools User Reviews](http://www.deepnlp.org/store/pub/) <br>
[AI Store Use Cases-Best AI Tools Cases User Reviews](http://www.deepnlp.org/store) <br>
[4 ways to use ChatGPT Stock Chatbot for stock analysis of Global Stock Markets NASDAQ NYSE LSE HKEX TSE NSE SHANGHAI SHENZHEN](http://www.deepnlp.org/blog/chatgpt-stock-global-market) <br>
[How to write a Financial Chatbot First Part 3 steps to crawl Hong Kong Stock Market (HKEX) realtime stock quotes](http://www.deepnlp.org/blog/fin-chatbot-first-spider-hkex) <br>
[3 steps to create Financial Chatbot powered by ChatGPT Part 1](http://www.deepnlp.org/blog/financial-chatbot-chatgpt-1) <br>

