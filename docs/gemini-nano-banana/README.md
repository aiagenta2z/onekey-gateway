## Image Generation - gemini-nano-banana/gemini-nano-banana

### Skill: gemini-nano-banana
#### generate_image_gemini
Description: Generates an image using the Gemini Image API.
            Supported Models (aliases are internal):
            The model parameter allows selection between available image generation models.
            - "gemini-2.5-flash-image" (recommended default for stable, fast response).
            - "gemini-3-pro-image-preview".
            - "gemini-3-flash"

            Aliases for these models are 'nano-banana 2.5' and 'nano-banana 3 Pro' respectively.
            Please use 'gemini-2.5-flash-image' unless the user specifically requests the Gemini 3 model.

        Args:
            model: The image generation model to use (see supported models above). Defaults to "gemini-2.5-flash-image". Supports: 'gemini-3-flash', 'gemini-3-pro-image-preview', 'gemini-2.5-flash-image'
            prompt: A detailed text description for the image to be generated.
            image_name: The filename for the output image, can be a relative path. Defaults to "gemini_output_images.png".
            output_folder: The optional absolute folder path provided by the user where the image will be saved. Do not use default server locations.
            aspect_ratio: The aspect ratio of the generated image (e.g., '16:9', '1:1', '4:3'). Defaults to '16:9'.
            image_size: The size/resolution of the generated image (e.g., '1K', '2K', '4K'). Defaults to '1K'.

        Return:
            Dict: Result dictionary containing image path, message, and success status.
            output_result["image_path"]: str
            output_result["image_url"]: str
            output_result["message"]: str
            output_result["success"]: bool
## Parameters
- model: string (default: gemini-2.5-flash-image)
- prompt: string (default: A detailed, cinematic image of a futuristic city.)
- image_name: string (default: gemini_output_images.png)
- output_folder: string/null
- aspect_ratio: string (default: 16:9)
- image_size: string (default: 1K)
##### CLI
```
onekey agent gemini-nano-banana/gemini-nano-banana generate_image_gemini '{"model": "gemini-2.5-flash-image", "prompt": "sunrise over mountains", "aspect_ratio": "16:9", "image_size": "1K"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"gemini-nano-banana/gemini-nano-banana","api_id":"generate_image_gemini","data":{"model": "gemini-2.5-flash-image", "prompt": "sunrise over mountains", "aspect_ratio": "16:9", "image_size": "1K"}}'
```
##### MCP
```
onekey mcp gemini-nano-banana
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-gemini-nano-banana":{
      "url":"https://agent.deepnlp.org/mcp?server_name=gemini-nano-banana&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill gemini-nano-banana -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill gemini-nano-banana
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS'))
router.invoke(unique_id="gemini-nano-banana/gemini-nano-banana", api_id="generate_image_gemini", data={"model": "gemini-2.5-flash-image", "prompt": "sunrise over mountains", "aspect_ratio": "16:9", "image_size": "1K"})
```

#### generate_image_nano_banana
Description: Generate Image With Nano Banana

        Args:
            model: The image generation model to use. Defaults to "gemini-2.5-flash-image". Supported Models such as follows Google Gemini Doc, such as 'gemini-3-flash', "gemini-3-pro-image-preview", "gemini-2.5-flash-image", note that nano-banana is the alias name of the Gemini Image Model. Nano banana 3 Pro refers to Gemini 3 pro preview, and Nono Banana 2.5 refers to Gemini 2.5. Unless specified by user to use Gemini 3 model preview, general 'Neno Banana' image models, please use 'gemini-2.5-flash-image' for more stable and fast response.
            prompt: A detailed text description for the image to be generated.
            image_name: The filename for the output image, can be a relative path, such as "./new_gemini_image.png", etc. Defaults to "gemini_output_images.png".
            output_folder: The optional absolute folder path provided by the user where the image will be saved. Do not use default server locations.
            aspect_ratio: The aspect ratio of the generated image (e.g., '16:9', '1:1', '4:3'), defaults to '16:9'.
            image_size: The size/resolution of the generated image (e.g., '1K', '2K', '4K'), defaults to '1K'.

        Return:
            Dict:  output_result is the result dict of MCP returned
            output_result["image_path"] = full_path: str
            output_result["message"] = output_message: str
            output_result["success"] = success: bool
## Parameters
- model: string (default: gemini-2.5-flash-image)
- prompt: string (default: A detailed, cinematic image of a futuristic city.)
- image_name: string (default: gemini_output_images.png)
- output_folder: string/null
- aspect_ratio: string (default: 16:9)
- image_size: string (default: 1K)
##### CLI
```
onekey agent gemini-nano-banana/gemini-nano-banana generate_image_nano_banana '{"model": "gemini-2.5-flash-image", "prompt": "robot reading book", "aspect_ratio": "16:9", "image_size": "1K"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"gemini-nano-banana/gemini-nano-banana","api_id":"generate_image_nano_banana","data":{"model": "gemini-2.5-flash-image", "prompt": "robot reading book", "aspect_ratio": "16:9", "image_size": "1K"}}'
```
##### MCP
```
onekey mcp gemini-nano-banana
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-gemini-nano-banana":{
      "url":"https://agent.deepnlp.org/mcp?server_name=gemini-nano-banana&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill gemini-nano-banana -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill gemini-nano-banana
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS'))
router.invoke(unique_id="gemini-nano-banana/gemini-nano-banana", api_id="generate_image_nano_banana", data={"model": "gemini-2.5-flash-image", "prompt": "robot reading book", "aspect_ratio": "16:9", "image_size": "1K"})
```

#### generate_image_nano_banana_with_reference
Description: Generate Image With Nano Banana with Reference

        Args:
            model: The image generation model to use. Defaults to "gemini-2.5-flash-image". Supported Models such as follows Google Gemini Doc, such as "gemini-3-pro-image-preview", "gemini-2.5-flash-image", note that nano-banana is the alias name of the Gemini Image Model. Nano banana 3 Pro refers to Gemini 3 pro preview, and Nono Banana 2.5 refers to Gemini 2.5. Unless specified by user to use Gemini 3 model preview, general 'Neno Banana' image models, please use 'gemini-2.5-flash-image' for more stable and fast response.
            prompt: A detailed text description for the image to be generated.
            image_name: The filename for the output image, can be a relative path, such as "./new_gemini_image.png", etc. Defaults to "gemini_output_images.png".
            output_folder: The optional absolute folder path provided by the user where the image will be saved. Do not use default server locations.
            aspect_ratio: The aspect ratio of the generated image (e.g., '16:9', '1:1', '4:3'), defaults to '16:9'.
            image_size: The size/resolution of the generated image (e.g., '1K', '2K', '4K'), defaults to '1K'.

        Return:
            Dict:  output_result is the result dict of MCP returned
            output_result["image_path"] = full_path: str
            output_result["message"] = output_message: str
            output_result["success"] = success: bool
## Parameters
- model: string (default: gemini-3-pro-image-preview)
- prompt: string (default: Please change this image to a winter coat style)
- images: array
- image_name: string (default: output_winter_coat.jpg)
- output_folder: string (default: ./output)
- aspect_ratio: string (default: 1:1)
- image_size: string (default: 1K)
##### CLI
```
onekey agent gemini-nano-banana/gemini-nano-banana generate_image_nano_banana_with_reference '{"model": "gemini-3-pro-image-preview", "prompt": "winter coat style", "images": ["https://avatars.githubusercontent.com/u/242328252"], "aspect_ratio": "1:1"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"gemini-nano-banana/gemini-nano-banana","api_id":"generate_image_nano_banana_with_reference","data":{"model": "gemini-3-pro-image-preview", "prompt": "winter coat style", "images": ["https://avatars.githubusercontent.com/u/242328252"], "aspect_ratio": "1:1"}}'
```
##### MCP
```
onekey mcp gemini-nano-banana
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-gemini-nano-banana":{
      "url":"https://agent.deepnlp.org/mcp?server_name=gemini-nano-banana&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill gemini-nano-banana -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill gemini-nano-banana
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS'))
router.invoke(unique_id="gemini-nano-banana/gemini-nano-banana", api_id="generate_image_nano_banana_with_reference", data={"model": "gemini-3-pro-image-preview", "prompt": "winter coat style", "images": ["https://avatars.githubusercontent.com/u/242328252"], "aspect_ratio": "1:1"})
```

#### ocr_extract_text_from_image
Description: Perform Optical Character Recognition (OCR) to extract all text from a given image URL.

    Args:
        image_url: The public URL of the image containing text to be transcribed.
        model: The model used for vision analysis. Defaults to Gemini 3 Flash.
## Parameters
- model: string (default: gemini-3-flash-preview)
- images: array
##### CLI
```
onekey agent gemini-nano-banana/gemini-nano-banana ocr_extract_text_from_image '{"images": ["https://avatars.githubusercontent.com/u/242328252"], "model": "gemini-3-flash-preview"}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"gemini-nano-banana/gemini-nano-banana","api_id":"ocr_extract_text_from_image","data":{"images": ["https://avatars.githubusercontent.com/u/242328252"], "model": "gemini-3-flash-preview"}}'
```
##### MCP
```
onekey mcp gemini-nano-banana
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-gemini-nano-banana":{
      "url":"https://agent.deepnlp.org/mcp?server_name=gemini-nano-banana&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill gemini-nano-banana -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill gemini-nano-banana
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS'))
router.invoke(unique_id="gemini-nano-banana/gemini-nano-banana", api_id="ocr_extract_text_from_image", data={"images": ["https://avatars.githubusercontent.com/u/242328252"], "model": "gemini-3-flash-preview"})
```

#### list_items_from_image
Description: Analyze an image and return a list of all identified objects, items, or subjects.

    Args:
        image_url: The public URL of the image to analyze.
        model: The model used for object detection.
        output_json: If True, returns a structured list. If False, returns a text description.
## Parameters
- model: string (default: gemini-3-flash-preview)
- images: array
- output_json: boolean (default: True)
##### CLI
```
onekey agent gemini-nano-banana/gemini-nano-banana list_items_from_image '{"images": ["https://avatars.githubusercontent.com/u/242328252"], "model": "gemini-3-flash-preview", "output_json": true}'
```
##### RESTFUL
```
export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_access_key
curl -v -X POST "https://agent.deepnlp.org/agent_router" \
  -H "Content-Type: application/json" \
  -H "X-OneKey: $DEEPNLP_ONEKEY_ROUTER_ACCESS" \
  -d '{"unique_id":"gemini-nano-banana/gemini-nano-banana","api_id":"list_items_from_image","data":{"images": ["https://avatars.githubusercontent.com/u/242328252"], "model": "gemini-3-flash-preview", "output_json": true}}'
```
##### MCP
```
onekey mcp gemini-nano-banana
```
Add to client config
```
{
  "mcpServers":{
    "deepnlp-onekey-gemini-nano-banana":{
      "url":"https://agent.deepnlp.org/mcp?server_name=gemini-nano-banana&onekey=${DEEPNLP_ONEKEY_ROUTER_ACCESS}"
    }
  }
}
```
##### Skills
```
npx agtm add aiagenta2z/onekey-gateway --skill gemini-nano-banana -g
npx skills add https://github.com/aiagenta2z/onekey-gateway --skill gemini-nano-banana
```
##### python/typescript
```python
from ai_agent_marketplace import OneKeyAgentRouter
import os
router = OneKeyAgentRouter(onekey=os.getenv('DEEPNLP_ONEKEY_ROUTER_ACCESS'))
router.invoke(unique_id="gemini-nano-banana/gemini-nano-banana", api_id="list_items_from_image", data={"images": ["https://avatars.githubusercontent.com/u/242328252"], "model": "gemini-3-flash-preview", "output_json": true})
```
