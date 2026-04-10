/* eslint-disable */
// TypeScript version of scripts/run_api.js (generated skills also include runnable .js).

import * as fs from "node:fs";
import * as path from "node:path";

type ApiMeta = {
  apis: Record<
    string,
    {
      endpoint: string;
      method?: string;
      headers?: Record<string, string>;
      auth?: { header?: string; env?: string; value?: string };
    }
  >;
};

function readJson<T>(filePath: string): T {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function loadPayload(args: string[]): any {
  const dataIndex = args.indexOf("--data");
  const dataFileIndex = args.indexOf("--data-file");
  if (dataIndex !== -1 && dataFileIndex !== -1) {
    throw new Error("Use only one of --data or --data-file.");
  }
  if (dataIndex !== -1) return JSON.parse(args[dataIndex + 1] || "{}");
  if (dataFileIndex !== -1) return readJson(args[dataFileIndex + 1]);
  return {};
}

function loadApiMeta(): ApiMeta {
  const referenceDir = path.join(__dirname, "..", "reference");
  const metaPath = path.join(referenceDir, "api_meta.json");
  return readJson<ApiMeta>(metaPath);
}

function normalizeHeaders(meta: any): Record<string, string> {
  const headers: Record<string, string> = { ...(meta.headers || {}) };
  if (meta.auth?.header) {
    const envName = meta.auth.env || meta.auth.value;
    const envValue = envName ? process.env[envName] : undefined;
    if (envValue) headers[meta.auth.header] = envValue;
  }
  return headers;
}

function applyQueryParams(url: string, payload: any): URL {
  const u = new URL(url);
  if (!payload || typeof payload !== "object") return u;
  for (const [key, value] of Object.entries(payload)) {
    if (value === undefined || value === null) continue;
    if (Array.isArray(value)) {
      for (const item of value) u.searchParams.append(key, String(item));
    } else {
      u.searchParams.set(key, String(value));
    }
  }
  return u;
}

async function main() {
  const args = process.argv.slice(2);
  const apiIndex = args.indexOf("--api");
  const api = apiIndex === -1 ? null : args[apiIndex + 1];
  if (!api) throw new Error("Missing --api <api_id>.");

  const meta = loadApiMeta();
  const apiInfo = meta.apis?.[api];
  if (!apiInfo) throw new Error(`Unknown api_id: ${api}`);

  const payload = loadPayload(args);
  const method = String(apiInfo.method || "GET").toUpperCase();
  const headers = normalizeHeaders(apiInfo);

  let url = apiInfo.endpoint;
  const init: RequestInit = { method, headers };
  if (method === "GET" || method === "DELETE") {
    url = applyQueryParams(url, payload).toString();
  } else {
    headers["Content-Type"] = headers["Content-Type"] || "application/json";
    init.body = JSON.stringify(payload || {});
  }

  const res = await fetch(url, init);
  const text = await res.text();
  let body: any = text;
  try {
    body = JSON.parse(text);
  } catch {}
  if (!res.ok) {
    console.error(JSON.stringify({ status: res.status, body }, null, 2));
    process.exit(1);
  }
  process.stdout.write(typeof body === "string" ? body : JSON.stringify(body, null, 2));
  process.stdout.write("\n");
}

main().catch((err) => {
  console.error(String((err as any)?.stack || err));
  process.exit(1);
});

