---
name: gemini-nano-banana
description: Auto-generated skill for gemini tools via OneKey Gateway.
env_vars:
  - name: DEEPNLP_ONEKEY_ROUTER_ACCESS
    description: OneKey Gateway API key
    required: true
dependencies:
  npm:
    - "@aiagenta2z/onekey-gateway"
  python:
    - "ai-agent-marketplace"
---

### OneKey Gateway
Use One Access Key to connect to various commercial APIs. Please visit the [OneKey Gateway Keys](https://www.deepnlp.org/workspace/keys) and read the docs [OneKey MCP Router Doc](https://www.deepnlp.org/doc/onekey_mcp_router) and [OneKey Gateway Doc](https://deepnlp.org/doc/onekey_agent_router).


# gemini Skill
Use the OneKey Gateway to access tools for this server via a unified access key.
## Quick Start
Set your OneKey access key:
```bash
export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_API_KEY
```
Common settings:
- `unique_id`: `gemini/gemini`
- `api_id`: one of the tools listed below
## Tools
### `generate_image_gemini`
Generates an image using the Gemini Image API.
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

Parameters:
- `model` (string, optional):
- `prompt` (string, optional):
- `image_name` (string, optional):
- `output_folder` (object, optional):
- `aspect_ratio` (string, optional):
- `image_size` (string, optional):
### `generate_image_nano_banana`
Generate Image With Nano Banana

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

Parameters:
- `model` (string, optional):
- `prompt` (string, optional):
- `image_name` (string, optional):
- `output_folder` (object, optional):
- `aspect_ratio` (string, optional):
- `image_size` (string, optional):

# Usage
## CLI

### generate_image_gemini
```shell
npx onekey agent gemini-nano-banana/gemini-nano-banana generate_image_gemini '{"model": "gemini-2.5-flash-image", "prompt": "sunrise over mountains", "aspect_ratio": "16:9", "image_size": "1K"}'
```

### generate_image_nano_banana
```shell
npx onekey agent gemini-nano-banana/gemini-nano-banana generate_image_nano_banana '{"model": "gemini-2.5-flash-image", "prompt": "robot reading book", "aspect_ratio": "16:9", "image_size": "1K"}'
```

### generate_image_nano_banana_with_reference
```shell
npx onekey agent gemini-nano-banana/gemini-nano-banana generate_image_nano_banana_with_reference '{"model": "gemini-3-pro-image-preview", "prompt": "winter coat style", "images": ["https://avatars.githubusercontent.com/u/242328252"], "aspect_ratio": "1:1"}'
```

### ocr_extract_text_from_image
```shell
npx onekey agent gemini-nano-banana/gemini-nano-banana ocr_extract_text_from_image '{"images": ["https://avatars.githubusercontent.com/u/242328252"], "model": "gemini-3-flash-preview"}'
```

### list_items_from_image
```shell
npx onekey agent gemini-nano-banana/gemini-nano-banana list_items_from_image '{"images": ["https://avatars.githubusercontent.com/u/242328252"], "model": "gemini-3-flash-preview", "output_json": true}'
```

## Scripts
Each tool has a dedicated script in this folder:
- `skills/gemini/scripts/generate_image_gemini.py`
- `skills/gemini/scripts/generate_image_nano_banana.py`
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
