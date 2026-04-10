#!/usr/bin/env node

const ENDPOINT = "https://agent.deepnlp.org/agent_router";
const UNIQUE_ID = "craftsman-agent/craftsman-agent";
const API_ID = "generate_lego_build_plan";
const ENV_KEY = "DEEPNLP_ONEKEY_ROUTER_ACCESS";
const ONEKEY_HEADER = "X-OneKey";
const DEMO_KEY = "BETA_TEST_KEY_MARCH_2026";

function getApiKey(): string {
  const apiKey = process.env[ENV_KEY];
  if (apiKey) return apiKey;

  console.log("\n" + "=".repeat(60));
  console.log("WARNING: DEMO MODE — NO API KEY SET");
  console.log("Using default test key (BETA_TEST_KEY_MARCH_2026)");
  console.log("Results may be mocked or inaccurate");
  console.log("Set: export DEEPNLP_ONEKEY_ROUTER_ACCESS=your_key");
  console.log("=".repeat(60) + "\n");
  return DEMO_KEY;
}

function wrapUserText(text: string): string {
  return `USER_PROMPT_START\n${text}\nUSER_PROMPT_END`;
}

function validateRefImageUrls(urls: string[]) {
  for (const url of urls) {
    try {
      const parsed = new URL(url);
      if (parsed.protocol !== "http:" && parsed.protocol !== "https:") {
        throw new Error(`Invalid ref image URL scheme: ${url}`);
      }
    } catch (err) {
      throw new Error(`Invalid ref image URL: ${url}`);
    }
  }
}

function parseArgs(argv: string[]) {
  const args: Record<string, string | string[]> = {};
  for (let i = 0; i < argv.length; i += 1) {
    const token = argv[i];
    if (
      token === "--prompt" ||
      token === "--mode" ||
      token === "--images" ||
      token === "--ref-image-url"
    ) {
      const value = argv[i + 1];
      i += 1;
      if (token === "--images" || token === "--ref-image-url") {
        const list = (args["--images"] as string[]) || [];
        list.push(value);
        args["--images"] = list;
      } else {
        args[token] = value;
      }
    }
  }

  return {
    prompt: (args["--prompt"] as string) || "",
    mode: (args["--mode"] as string) || "basic",
    images: (args["--images"] as string[]) || [],
  };
}

async function main() {
  const { prompt, mode, images } = parseArgs(process.argv.slice(2));
  if (!prompt) {
    console.error("Missing --prompt");
    process.exit(1);
  }

  const apiKey = getApiKey();

  const url = new URL(ENDPOINT);
  validateRefImageUrls(images);

  const payload = {
    unique_id: UNIQUE_ID,
    api_id: API_ID,
    data: {
      prompt: wrapUserText(prompt),
      images: images,
      mode,
    },
  };

  const response = await fetch(url.toString(), {
    method: "POST",
    headers: { "Content-Type": "application/json", [ONEKEY_HEADER]: apiKey },
    body: JSON.stringify(payload),
  });

  const text = await response.text();
  if (!response.ok) {
    console.error(`HTTP ${response.status}: ${text}`);
    process.exit(1);
  }

  try {
    const json = JSON.parse(text);
    console.log(JSON.stringify(json, null, 2));
  } catch {
    console.log(text);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
