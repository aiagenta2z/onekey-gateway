export type RouterResponse<T = unknown> = {
  success: boolean;
  data: T;
  error: string | null;
};

export type AgentRequest = {
  unique_id: string;
  api_id: string;
  data: unknown;
};

export type LlmMessage = {
  role: string;
  content: string;
};

export type LlmRequest = {
  provider: string;
  model: string;
  messages: LlmMessage[];
  temperature?: number;
  response_format?: string;
  [key: string]: unknown;
};

export type McpConfigOptions = {
  serverName: string;
  accessKey?: string;
  configName?: string;
};

const DEFAULT_ACCESS_KEY = "BETA_TEST_KEY_MARCH_2026";

const AGENT_ROUTER_URL = "https://agent.deepnlp.org/agent_router";
const MCP_ROUTER_BASE_URL = "https://agent.deepnlp.org/mcp";
const LLM_ROUTER_URL = "https://agent.deepnlp.org/llm";

function resolveAccessKey(accessKey?: string): string {
  return accessKey && accessKey.trim().length > 0 ? accessKey : DEFAULT_ACCESS_KEY;
}

async function postJson<T>(url: string, body: unknown, accessKey?: string): Promise<RouterResponse<T>> {
  const key = resolveAccessKey(accessKey);
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-OneKey": key
    },
    body: JSON.stringify(body)
  });

  const text = await response.text();
  try {
    return JSON.parse(text) as RouterResponse<T>;
  } catch {
    return {
      success: false,
      data: text as unknown as T,
      error: "Non-JSON response"
    };
  }
}

export async function agentRouter(request: AgentRequest, accessKey?: string): Promise<RouterResponse> {
  return postJson(AGENT_ROUTER_URL, request, accessKey);
}

export async function llmRouter(request: LlmRequest, accessKey?: string): Promise<RouterResponse> {
  return postJson(LLM_ROUTER_URL, request, accessKey);
}

export function buildMcpConfig(options: McpConfigOptions) {
  const key = resolveAccessKey(options.accessKey);
  const name = options.configName ?? `deepnlp-onekey-${options.serverName}`;
  const url = `${MCP_ROUTER_BASE_URL}?server_name=${encodeURIComponent(
    options.serverName
  )}&onekey=${encodeURIComponent(key)}`;

  return {
    mcpServers: {
      [name]: {
        url
      }
    }
  };
}

export const constants = {
  AGENT_ROUTER_URL,
  MCP_ROUTER_BASE_URL,
  LLM_ROUTER_URL,
  DEFAULT_ACCESS_KEY
};
