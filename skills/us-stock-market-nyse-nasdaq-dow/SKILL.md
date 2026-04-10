---
name: us-stock-market-nyse-nasdaq-dow
description: Get US stock market data (NYSE, NASDAQ, and major indices) via FinanceAgent on OneKey Gateway.
env:
  DEEPNLP_ONEKEY_ROUTER_ACCESS:
    required: true
    description: OneKey Gateway API key
dependencies:
  npm:
    - "@aiagenta2z/onekey-gateway"
installation:
  npm: npm -g install @aiagenta2z/onekey-gateway
---

# OneKey Gateway

Use one access key to connect to various commercial APIs via the DeepNLP OneKey Agent Router.

## Quick Start

### Set your OneKey Access Key

```shell
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
```

Common settings:

- `unique_id`: `aiagenta2z/financeagent`
- `api_id`: `get_us_stock_market_nyse_nasdaq_dow`

## Tool

### `get_us_stock_market_nyse_nasdaq_dow`

Get US stock market data (NYSE, NASDAQ, DOW).

Parameters:
- `symbol_list` (array of string, required): Stock symbols to query.
  - Use standard US tickers, e.g. `"TSLA"`, `"MSFT"`, `"GOOG"`.
  - Example: `["TSLA", "MSFT", "GOOG"]`

Response (JSON):
- `success` (boolean): Whether the request succeeded.
- `data` (array): List of stock quote objects (fields depend on the upstream data source).
- `message` (string, optional): Error message when `success=false`.

# Usage

## CLI Usage

```shell
## install onekey agent gateway
npm install @aiagenta2z/onekey-gateway

## CLI to Call API and Symbol List
npx onekey agent aiagenta2z/financeagent get_us_stock_market_nyse_nasdaq_dow '{"symbol_list": ["TSLA", "MSFT", "GOOG"]}'
```

## HTTP (curl) Usage

```shell
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key

curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{
    "unique_id": "aiagenta2z/financeagent",
    "api_id": "get_us_stock_market_nyse_nasdaq_dow",
    "data": {
      "symbol_list": ["TSLA", "MSFT", "GOOG"]
    }
  }'
```

