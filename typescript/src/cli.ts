#!/usr/bin/env node

import { agentRouter, buildMcpConfig, llmRouter, constants } from "./client";
import { readFileSync } from "fs";

type ParsedArgs = {
  command?: string;
  positionals: string[];
  flags: Record<string, string | boolean>;
};

function parseArgs(argv: string[]): ParsedArgs {
  const flags: Record<string, string | boolean> = {};
  const positionals: string[] = [];

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (!arg) continue;

    if (arg.startsWith("--")) {
      const [key, inlineValue] = arg.slice(2).split("=", 2);
      if (inlineValue !== undefined) {
        flags[key] = inlineValue;
        continue;
      }

      const next = argv[i + 1];
      if (!next || next.startsWith("-")) {
        flags[key] = true;
        continue;
      }

      flags[key] = next;
      i += 1;
      continue;
    }

    if (arg.startsWith("-")) {
      flags[arg.slice(1)] = true;
      continue;
    }

    positionals.push(arg);
  }

  return {
    command: positionals.shift(),
    positionals,
    flags
  };
}

function readMaybeFile(input: string): string {
  if (input.startsWith("@")) {
    const path = input.slice(1);
    return readFileSync(path, "utf-8");
  }
  return input;
}

function parseJsonInput(input: string, label: string): unknown {
  const raw = readMaybeFile(input);
  try {
    return JSON.parse(raw);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    throw new Error(`Failed to parse ${label} JSON: ${message}`);
  }
}

function resolveAccessKey(flags: Record<string, string | boolean>): string {
  const keyFlag = flags.key;
  if (typeof keyFlag === "string" && keyFlag.trim().length > 0) {
    return keyFlag;
  }

  const envKey = process.env.DEEPNLP_ONEKEY_ROUTER_ACCESS;
  if (envKey && envKey.trim().length > 0) {
    return envKey;
  }

  return constants.DEFAULT_ACCESS_KEY;
}

function warnIfUsingDefault(accessKey: string, flags: Record<string, string | boolean>) {
  const keyFlag = flags.key;
  const envKey = process.env.DEEPNLP_ONEKEY_ROUTER_ACCESS;
  if (!keyFlag && !envKey) {
    process.stderr.write(
      "Using default test key (BETA_TEST_KEY_MARCH_2026). Set DEEPNLP_ONEKEY_ROUTER_ACCESS or pass --key to override.\n"
    );
  }
}

function printHelp() {
  const text = `OneKey Gateway CLI

Usage:
    onekey agent <unique_id> <api_id> <data_json|@file>
    onekey mcp <server_name> [--name config_name]
    onekey llm --provider <provider> --model <model> --messages <json|@file> [--temperature <num>] [--response-format <format>] [--options <json|@file>]
    onekey llm --payload <json|@file>

Flags:
      --key <access_key>           Override DEEPNLP_ONEKEY_ROUTER_ACCESS
      --help                       Show help

Examples:
      onekey agent google-maps/google-maps maps_search_places '{"query":"New York City Italian Restaurants"}'
      onekey mcp google-maps
      onekey llm --provider gemini --model gemini-3-flash-preview --messages @messages.json --temperature 0.7 --response-format json
`;
  process.stdout.write(text);
}

async function runAgent(positionals: string[], flags: Record<string, string | boolean>) {
  const [uniqueId, apiId, dataInput] = positionals;
  if (!uniqueId || !apiId || !dataInput) {
    throw new Error("agent requires <unique_id> <api_id> <data_json|@file>");
  }

  const accessKey = resolveAccessKey(flags);
  warnIfUsingDefault(accessKey, flags);

  const data = parseJsonInput(dataInput, "data");
  const result = await agentRouter(
    {
      unique_id: uniqueId,
      api_id: apiId,
      data
    },
    accessKey
  );

  process.stdout.write(`${JSON.stringify(result)}\n`);
}

async function runMcp(positionals: string[], flags: Record<string, string | boolean>) {
  const [serverName] = positionals;
  if (!serverName) {
    throw new Error("mcp requires <server_name>");
  }

  const accessKey = resolveAccessKey(flags);
  warnIfUsingDefault(accessKey, flags);

  const configName = typeof flags.name === "string" ? flags.name : undefined;
  const config = buildMcpConfig({
    serverName,
    accessKey,
    configName
  });

  process.stdout.write(`${JSON.stringify(config, null, 2)}\n`);
}

async function runLlm(positionals: string[], flags: Record<string, string | boolean>) {
  // const [requestId] = positionals;
//   if (!requestId) {
//     throw new Error("llm requires <request_id>");
//   }

  const accessKey = resolveAccessKey(flags);
  warnIfUsingDefault(accessKey, flags);

  let payload: Record<string, unknown>;

  if (typeof flags.payload === "string") {
    payload = parseJsonInput(flags.payload, "payload") as Record<string, unknown>;
  } else {
    const provider = flags.provider;
    const model = flags.model;
    const messagesInput = flags.messages;

    if (typeof provider !== "string" || typeof model !== "string" || typeof messagesInput !== "string") {
      throw new Error("llm requires --provider, --model, and --messages unless --payload is provided");
    }

    const messages = parseJsonInput(messagesInput, "messages");
    payload = {
      provider,
      model,
      messages
    };

    if (typeof flags.temperature === "string") {
      const temp = Number(flags.temperature);
      if (Number.isNaN(temp)) {
        throw new Error("--temperature must be a number");
      }
      payload.temperature = temp;
    }

    if (typeof flags["response-format"] === "string") {
      payload.response_format = flags["response-format"];
    }

    if (typeof flags.response_format === "string") {
      payload.response_format = flags.response_format;
    }

    if (typeof flags.options === "string") {
      const options = parseJsonInput(flags.options, "options") as Record<string, unknown>;
      payload = {
        ...payload,
        ...options
      };
    }
  }

  // payload.request_id = requestId;

  const result = await llmRouter(payload as any, accessKey);
  process.stdout.write(`${JSON.stringify(result)}\n`);
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  const { command, positionals, flags } = parsed;

  if (!command || flags.help || flags.h) {
    printHelp();
    return;
  }

  try {
    switch (command) {
      case "agent":
        await runAgent(positionals, flags);
        return;
      case "mcp":
        await runMcp(positionals, flags);
        return;
      case "llm":
        await runLlm(positionals, flags);
        return;
      default:
        throw new Error(`Unknown command: ${command}`);
    }
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    process.stderr.write(`${message}\n`);
    process.exit(1);
  }
}

void main();
