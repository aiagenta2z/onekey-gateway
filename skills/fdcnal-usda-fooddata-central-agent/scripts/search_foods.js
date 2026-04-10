#!/usr/bin/env node

const { spawnSync } = require("node:child_process");
const path = require("node:path");

const script = path.join(__dirname, "run_api.js");
const args = process.argv.slice(2);
const res = spawnSync(process.execPath, [script, "--api", "search_foods", ...args], { stdio: "inherit" });
process.exit(typeof res.status === "number" ? res.status : 1);
