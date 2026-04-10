## 3D Generation - craftsman-agent/craftsman-agent

### Skill: craftsman-agent

#### generate_lego_build_plan
Description: Turn a text prompt (optionally with reference images) into a LEGO-style build plan, inventory list, and step images.
## Parameters
- prompt: string — What to build (e.g., "pink lego phone")
- images: array — Optional reference image URLs to guide style
- mode: string — Generation mode (e.g., "basic", "high") (default: basic)
##### CLI
```
npx onekey agent craftsman-agent/craftsman-agent generate_lego_build_plan '{"prompt":"pink lego phone","images":[],"mode":"basic"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"craftsman-agent/craftsman-agent","api_id":"generate_lego_build_plan","data":{"prompt":"pink lego phone","images":[],"mode":"basic"}}'
```
##### MCP
```
npx onekey mcp craftsman-agent
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-craftsman-agent":{
      "url":"https://agent.deepnlp.org/mcp?server_name=craftsman-agent&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill craftsman-agent -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill craftsman-agent
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(
    unique_id="craftsman-agent/craftsman-agent",
    api_id="generate_lego_build_plan",
    data={"prompt":"pink lego phone","images":[],"mode":"basic"}
)
```

#### generate_minecraft_build_plan
Description: Create a Minecraft-style build plan, inventory, and step images from a prompt and optional reference images.
## Parameters
- prompt: string — What to build (e.g., "minecraft pink castle")
- images: array — Optional reference images
- mode: string — Generation mode (e.g., "basic", "high") (default: basic)
##### CLI
```
npx onekey agent craftsman-agent/craftsman-agent generate_minecraft_build_plan '{"prompt":"minecraft pink castle","images":[],"mode":"basic"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"craftsman-agent/craftsman-agent","api_id":"generate_minecraft_build_plan","data":{"prompt":"minecraft pink castle","images":[],"mode":"basic"}}'
```
##### MCP
```
npx onekey mcp craftsman-agent
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-craftsman-agent":{
      "url":"https://agent.deepnlp.org/mcp?server_name=craftsman-agent&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill craftsman-agent -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill craftsman-agent
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS','BETA_TEST_KEY_MARCH_2026'))
router.invoke(
    unique_id="craftsman-agent/craftsman-agent",
    api_id="generate_minecraft_build_plan",
    data={"prompt":"minecraft pink castle","images":[],"mode":"basic"}
)
```
