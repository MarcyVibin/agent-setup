#!/usr/bin/env python3
"""Self-check for shot.py: one clean page must pass, one broken page must fail."""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CLEAN = "<!doctype html><title>ok</title><link rel=icon href='data:,'><h1 id=t>Hi</h1><p id=gone hidden>x</p>"
BROKEN = "<!doctype html><title>bad</title><div style='width:900px'>wide</div><script>console.error('boom')</script>"


def run(html, *extra):
  with tempfile.TemporaryDirectory() as site, tempfile.TemporaryDirectory() as out:
    with open(os.path.join(site, "index.html"), "w") as f:
      f.write(html)
    cmd = [sys.executable, os.path.join(HERE, "shot.py"), site, "--widths", "375", "--wait", "0.5", "--out", out, *extra]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout


code, out = run(CLEAN, "--visible", "#t", "--hidden", "#gone", "--crop", "#t")
assert code == 0, out
assert "crop1.png" in out, out

code, out = run(BROKEN)
assert code == 1, out
assert "horizontal overflow" in out and "boom" in out, out

print("shot.py self-check passed")
