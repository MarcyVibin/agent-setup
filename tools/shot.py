#!/usr/bin/env python3
"""Screenshot a page at several widths and report what broke.

Usage:
  python3 tools/shot.py <folder-or-url> [--page index.html] [--widths 375,1280]
    [--out /tmp/shots] [--name rev-1] [--wait 4] [--viewport-only]
    [--crop SELECTOR ...] [--visible SELECTOR ...] [--hidden SELECTOR ...]

A folder is served on a free local port; a URL is opened as it is.
Prints a JSON summary and exits 1 if any check fails.
"""
import argparse
import functools
import http.server
import json
import os
import sys
import threading

from playwright.sync_api import sync_playwright

GL_ARGS = ["--use-gl=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"]


def serve(folder):
  handler = functools.partial(QuietHandler, directory=folder)
  server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
  threading.Thread(target=server.serve_forever, daemon=True).start()
  return server


class QuietHandler(http.server.SimpleHTTPRequestHandler):
  def log_message(self, *args):
    pass


def launch(p):
  chrome = "/usr/bin/google-chrome"
  if os.path.exists(chrome):
    return p.chromium.launch(executable_path=chrome, args=GL_ARGS)
  return p.chromium.launch(args=GL_ARGS)


def shoot(url, args):
  os.makedirs(args.out, exist_ok=True)
  results = []
  with sync_playwright() as p:
    browser = launch(p)
    for width in args.widths:
      height = 812 if width < 800 else 800
      page = browser.new_page(viewport={"width": width, "height": height})
      problems = []
      page.on("console", lambda m: m.type == "error" and problems.append("console: " + m.text))
      page.on("pageerror", lambda e: problems.append("pageerror: " + str(e)))
      page.on("requestfailed", lambda r: problems.append("failed: " + r.url))
      page.on("response", lambda r: r.status >= 400 and problems.append(f"http {r.status}: {r.url}"))
      page.goto(url, wait_until="load")
      page.wait_for_timeout(args.wait * 1000)

      shot = os.path.join(args.out, f"{args.name}-{width}.png")
      page.screenshot(path=shot, full_page=not args.viewport_only)
      crops = []
      for i, sel in enumerate(args.crop):
        el = page.query_selector(sel)
        if el is None:
          problems.append(f"crop selector not found: {sel}")
          continue
        path = os.path.join(args.out, f"{args.name}-{width}-crop{i + 1}.png")
        el.screenshot(path=path)
        crops.append(path)

      scroll_width = page.evaluate("document.documentElement.scrollWidth")
      if scroll_width > width:
        problems.append(f"horizontal overflow: scrollWidth {scroll_width} > {width}")
      for sel in args.visible:
        if not page.is_visible(sel):
          problems.append(f"expected visible: {sel}")
      for sel in args.hidden:
        if page.is_visible(sel):
          problems.append(f"expected hidden: {sel}")

      results.append({"width": width, "screenshot": shot, "crops": crops, "problems": problems})
      page.close()
    browser.close()
  return results


def main(argv=None):
  ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
  ap.add_argument("target")
  ap.add_argument("--page", default="index.html")
  ap.add_argument("--widths", default="375,1280", type=lambda s: [int(w) for w in s.split(",")])
  ap.add_argument("--out", default="/tmp/shots")
  ap.add_argument("--name", default="shot")
  ap.add_argument("--wait", default=4, type=float)
  ap.add_argument("--viewport-only", action="store_true")
  ap.add_argument("--crop", action="append", default=[])
  ap.add_argument("--visible", action="append", default=[])
  ap.add_argument("--hidden", action="append", default=[])
  args = ap.parse_args(argv)

  server = None
  if args.target.startswith(("http://", "https://")):
    url = args.target
  else:
    server = serve(os.path.abspath(args.target))
    url = f"http://127.0.0.1:{server.server_address[1]}/{args.page}"
  try:
    results = shoot(url, args)
  finally:
    if server:
      server.shutdown()

  ok = not any(r["problems"] for r in results)
  print(json.dumps({"ok": ok, "url": url, "results": results}, indent=2))
  return 0 if ok else 1


if __name__ == "__main__":
  sys.exit(main())
