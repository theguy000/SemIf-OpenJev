from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys
import os

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Referrer-Policy", "no-referrer")
        super().end_headers()

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    server = HTTPServer(("localhost", port), Handler)
    print(f"Serving WebGPU Lab on http://localhost:{port}")
    server.serve_forever()
