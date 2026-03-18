#!/usr/bin/env node

const ENDPOINT = "https://agent.deepnlp.org/agent";
const UNIQUE_ID = "craftsman-agent/craftsman-agent";
const API_ID = "generate_minecraft_build_plan";
const ENV_KEY = "DEEPNLP_ONEKEY_ROUTER_ACCESS";
const DEMO_KEY = "BETA_TEST_KEY_MARCH_2026";

function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function parseArgs(argv: string[]) {
  const args: Record<string, string | string[]> = {};
  for (let i = 0; i < argv.length; i += 1) {
    const token = argv[i];
    if (token === "--prompt" || token === "--mode" || token === "--ref-image-url") {
      const value = argv[i + 1];
      i += 1;
      if (token === "--ref-image-url") {
        const list = (args[token] as string[]) || [];
        list.push(value);
        args[token] = list;
      } else {
        args[token] = value;
      }
    }
  }

  return {
    prompt: (args["--prompt"] as string) || "",
    mode: (args["--mode"] as string) || "basic",
    refImageUrl: (args["--ref-image-url"] as string[]) || [],
  };
}

async function main() {
  const { prompt, mode, refImageUrl } = parseArgs(process.argv.slice(2));
  if (!prompt) {
    console.error("Missing --prompt");
    process.exit(1);
  }

  let apiKey = process.env[ENV_KEY];
  if (!apiKey) {
    console.error(
      "DEEPNLP_ONEKEY_ROUTER_ACCESS is not set. The API is not free; using demo key after a short wait."
    );
    console.error("Set with: export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_API_KEY");
    await sleep(2000);
    apiKey = DEMO_KEY;
  }

  const url = new URL(ENDPOINT);
  url.searchParams.set("onekey", apiKey);

  const payload = {
    unique_id: UNIQUE_ID,
    api_id: API_ID,
    data: {
      prompt,
      ref_image_url: refImageUrl,
      mode,
    },
  };

  const response = await fetch(url.toString(), {
    method: "POST",
    headers: { "Content-Type": "application/json" },
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
