#!/usr/bin/env python3
"""Local preview that mirrors Vercel's cleanUrls, so /grooming resolves to
grooming.html the same way it will in production."""
import functools, http.server, os, socketserver, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5173


class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        full = super().translate_path(path)
        if not os.path.exists(full) and not full.endswith(("/", ".html")):
            if os.path.exists(full + ".html"):
                return full + ".html"
        return full


if __name__ == "__main__":
    os.chdir(ROOT)
    with socketserver.TCPServer(("", PORT), functools.partial(Handler, directory=ROOT)) as httpd:
        print(f"serving public/ on http://localhost:{PORT}  (clean URLs enabled)")
        httpd.serve_forever()
