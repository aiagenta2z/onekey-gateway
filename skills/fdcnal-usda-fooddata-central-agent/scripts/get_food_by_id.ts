/* eslint-disable */
import { spawnSync } from "node:child_process";
import * as path from "node:path";

const script = path.join(__dirname, "run_api.js");
const args = process.argv.slice(2);
const res = spawnSync(process.execPath, [script, "--api", "get_food_by_id", ...args], { stdio: "inherit" });
process.exit(typeof res.status === "number" ? res.status : 1);
