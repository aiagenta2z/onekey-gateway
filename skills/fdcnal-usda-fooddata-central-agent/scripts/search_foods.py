#!/usr/bin/env python3

import os
import subprocess
import sys

def main():
    script = os.path.join(os.path.dirname(__file__), "run_api.py")
    args = [sys.executable, script, "--api", "search_foods"] + sys.argv[1:]
    res = subprocess.run(args)
    raise SystemExit(res.returncode)

if __name__ == "__main__":
    main()
