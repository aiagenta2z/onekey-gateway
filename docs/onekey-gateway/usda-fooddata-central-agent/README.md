---
name: "fdcnal-usda-fooddata-central-agent"
description: "The FoodData Central API provides REST access to FoodData Central (FDC), assisting developers in incorporating nutrient data into their applications. It provides access to Standard Reference (SR) Legacy data, USDA Global Branded Foods Database, Foundation Foods, and FNDDS."
env:
  DEEPNLP_ONEKEY_ROUTER_ACCESS:
    required: false
    description: Onekey Gateway Registerd API and Usage access key
dependencies:
  node: []
  python: []
---


# fdcnal-usda-fooddata-central-agent

Auto-generated skill for OneKey Agent Gateway registered agent `fdcnal/usda-fooddata-central-agent` based on its `api_list` from registered API metas. Available 
to use in CLIs, Skills, Rest APIs, and more agent preferred formats.


## Quick Start
Set the API providers access key `` or the registered OneKey Gateway access key DEEPNLP_ONEKEY_ROUTER_ACCESS from AI Agent Marketplace.

```bash
export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_REGISTRY_KEY
```
Run an API via scripts:
- Node (JS): `node scripts/<api_name>.js --data '{"key":"value"}'`
- Python: `python3 scripts/<api_name>.py --data '{"key":"value"}'`

## APIs
### `get_foods_multiple`
Fetches details for multiple food items using input FDC IDs

- Method: `GET,POST`
- Endpoint: `https://api.nal.usda.gov/fdc/v1/foods`

Parameters:
- `fdcIds`: `array[string]`
- `format`: `string=full`
- `nutrients`: `array[integer]`

#### Curl
```bash
curl -X GET,POST "https://api.nal.usda.gov/fdc/v1/foods" \
  -H "Content-Type: application/json" \
  -d '{}'
```

#### Scripts
```bash
node scripts/get_foods_multiple.js --data '{}'
python3 scripts/get_foods_multiple.py --data '{}'
```

### `get_food_by_id`
Fetches details for one food item by FDC ID

- Method: `GET`
- Endpoint: `https://api.nal.usda.gov/fdc/v1/food/{fdcId}`

Parameters:
- `fdcId`: `string`
- `format`: `string=full`
- `nutrients`: `array[integer]`

#### Curl
```bash
curl -X GET "https://api.nal.usda.gov/fdc/v1/food/{fdcId}"
```

#### Scripts
```bash
node scripts/get_food_by_id.js --data '{}'
python3 scripts/get_food_by_id.py --data '{}'
```

### `list_foods`
Returns a paged list of foods, in the 'abridged' format

- Method: `GET,POST`
- Endpoint: `https://api.nal.usda.gov/fdc/v1/foods/list`

Parameters:
- `dataType`: `array[string]`
- `pageSize`: `integer=50`
- `pageNumber`: `integer=1`
- `sortBy`: `string`
- `sortOrder`: `string`

#### Curl
```bash
curl -X GET,POST "https://api.nal.usda.gov/fdc/v1/foods/list" \
  -H "Content-Type: application/json" \
  -d '{}'
```

#### Scripts
```bash
node scripts/list_foods.js --data '{}'
python3 scripts/list_foods.py --data '{}'
```

### `search_foods`
Returns a list of foods that matched search (query) keywords

- Method: `GET,POST`
- Endpoint: `https://api.nal.usda.gov/fdc/v1/foods/search`

Parameters:
- `query`: `string`
- `dataType`: `array[string]`
- `pageSize`: `integer=50`
- `pageNumber`: `integer=1`
- `sortBy`: `string`
- `sortOrder`: `string`
- `brandOwner`: `string`

#### Curl
```bash
curl -X GET,POST "https://api.nal.usda.gov/fdc/v1/foods/search" \
  -H "Content-Type: application/json" \
  -d '{}'
```

#### Scripts
```bash
node scripts/search_foods.js --data '{}'
python3 scripts/search_foods.py --data '{}'
```


### Scripts

Each API has a dedicated script in `scripts/`:
```bash
node scripts/<api_name>.js --data '{"key":"value"}'
python3 scripts/<api_name>.py --data '{"key":"value"}'
```

### CLIs

```shell
npx onekey agent fdcnal/usda-fooddata-central-agent get_foods_multiple '{"fdcIds":[],"format":"value","nutrients":0}'
npx onekey agent fdcnal/usda-fooddata-central-agent get_food_by_id '{"fdcId":"value","format":"value","nutrients":0}'
npx onekey agent fdcnal/usda-fooddata-central-agent list_foods '{"dataType":[],"pageNumber":0,"pageSize":0,"sortBy":"value","sortOrder":"value"}'
npx onekey agent fdcnal/usda-fooddata-central-agent search_foods '{"brandOwner":"value","dataType":[],"pageNumber":0,"pageSize":0,"query":"value","sortBy":"value"}'
```



## References
- `reference/api_list.json`: original `api_list` payload
- `reference/api_meta.json`: normalized API metadata used by scripts
