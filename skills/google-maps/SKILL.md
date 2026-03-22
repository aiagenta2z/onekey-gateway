---
name: google-maps
description: Google Maps tools via OneKey Gateway (geocode, places, distance matrix, elevation, directions).
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

# OneKey Gateway

Use One Access Key to connect to various commercial APIs. Please visit the [OneKey Gateway Keys](https://www.deepnlp.org/workspace/keys) and read the docs [OneKey MCP Router Doc](https://www.deepnlp.org/doc/onekey_mcp_router) and [OneKey Gateway Doc](https://deepnlp.org/doc/onekey_agent_router).

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
And please use the command line "onekey" as the preferred method to run the skills.

# Google Maps Skill

Use the OneKey Gateway to access Google Maps APIs through a unified access key.

## Quick Start

### Set your OneKey Access Key

In the .env file 
```shell
DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_API_KEY
```
or alternatively set via export. 
```bash
export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_API_KEY
```

If no key is provided, the scripts fall back to the demo key `BETA_TEST_KEY_MARCH_2026`.

Common settings:

- `unique_id`: `google-maps/google-maps`
- `api_id`: one of the tools listed below

## Tools

### `maps_geocode`
Convert an address into geographic coordinates.

Parameters:
- `address` (string, required): The address to geocode.

### `maps_reverse_geocode`
Convert coordinates into an address.

Parameters:
- `latitude` (number, required): Latitude coordinate.
- `longitude` (number, required): Longitude coordinate.

### `maps_search_places`
Search for places using Google Places API.

Parameters:
- `query` (string, required): Search query.
- `location` (object, optional): Optional center point for the search.
- `location.latitude` (number, optional): Latitude for the center point.
- `location.longitude` (number, optional): Longitude for the center point.
- `radius` (number, optional): Search radius in meters (max 50000).

### `maps_place_details`
Get detailed information about a specific place.

Parameters:
- `place_id` (string, required): The place ID to get details for.

### `maps_distance_matrix`
Calculate travel distance and time for multiple origins and destinations.

Parameters:
- `origins` (array of string, required): Array of origin addresses or coordinates.
- `destinations` (array of string, required): Array of destination addresses or coordinates.
- `mode` (string, optional): Travel mode (`driving`, `walking`, `bicycling`, `transit`).

### `maps_elevation`
Get elevation data for locations on the earth.

Parameters:
- `locations` (array of object, required): Array of locations to get elevation for.
- `locations[].latitude` (number, required): Latitude coordinate.
- `locations[].longitude` (number, required): Longitude coordinate.

### `maps_directions`
Get directions between two points.

Parameters:
- `origin` (string, required): Starting point address or coordinates.
- `destination` (string, required): Ending point address or coordinates.
- `mode` (string, optional): Travel mode (`driving`, `walking`, `bicycling`, `transit`).

# Usage
## CLI

### maps_geocode
```shell
npx onekey agent google-maps/google-maps maps_geocode '{"address": "Times Square, New York"}'
```

### maps_reverse_geocode
```shell
npx onekey agent google-maps/google-maps maps_reverse_geocode '{"latitude": 40.758, "longitude": -73.9855}'
```

### maps_search_places
```shell
npx onekey agent google-maps/google-maps maps_search_places '{"query": "Italian restaurants", "location": {"latitude": 40.758, "longitude": -73.9855}, "radius": 500}'
```

### maps_place_details
```shell
npx onekey agent google-maps/google-maps maps_place_details '{"place_id": "ChIJmQJIxlVYwokRLgeuocVOGVU"}'
```

### maps_distance_matrix
```shell
npx onekey agent google-maps/google-maps maps_distance_matrix '{"origins": ["Times Square, NY"], "destinations": ["Central Park, NY"], "mode": "driving"}'
```

### maps_elevation
```shell
npx onekey agent google-maps/google-maps maps_elevation '{"locations": [{"latitude": 36.057944, "longitude": -112.125168}]}'
```

### maps_directions
```shell
npx onekey agent google-maps/google-maps maps_directions '{"origin": "Golden Gate Bridge", "destination": "Ferry Building San Francisco", "mode": "driving"}'
```


## Scripts

Each tool has a dedicated script in `skills/google-maps/scripts/`:

- `skills/google-maps/scripts/maps_geocode.py`
- `skills/google-maps/scripts/maps_reverse_geocode.py`
- `skills/google-maps/scripts/maps_search_places.py`
- `skills/google-maps/scripts/maps_place_details.py`
- `skills/google-maps/scripts/maps_distance_matrix.py`
- `skills/google-maps/scripts/maps_elevation.py`
- `skills/google-maps/scripts/maps_directions.py`

### Examples

```bash
python3 skills/google-maps/scripts/maps_geocode.py --address "1600 Amphitheatre Parkway, Mountain View, CA"
```

```bash
python3 skills/google-maps/scripts/maps_reverse_geocode.py --latitude 37.422 --longitude -122.084
```

```bash
python3 skills/google-maps/scripts/maps_search_places.py --query "coffee" --location 37.422,-122.084 --radius 1500
```

```bash
python3 skills/google-maps/scripts/maps_place_details.py --place-id "ChIJ2eUgeAK6j4ARbn5u_wAGqWA"
```

```bash
python3 skills/google-maps/scripts/maps_distance_matrix.py --origins "Boston, MA" --destinations "New York, NY" --mode driving
```

```bash
python3 skills/google-maps/scripts/maps_elevation.py --locations "37.422,-122.084;37.427,-122.085"
```

```bash
python3 skills/google-maps/scripts/maps_directions.py --origin "Boston, MA" --destination "New York, NY" --mode driving
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
