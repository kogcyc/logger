from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

    def _set_headers(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()
        return

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data)
            print("📥 Received payload:", data)

            self._set_headers()
            response = {"status": "success", "message": "Payload received"}
            self.wfile.write(json.dumps(response).encode('utf-8'))

        except json.JSONDecodeError:
            self._set_headers(status=400)
            response = {"status": "error", "message": "Invalid JSON"}
            self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_GET(self):
        self._set_headers(content_type="text/plain")
        self.wfile.write("Hello from Python API with CORS!".encode("utf-8"))
