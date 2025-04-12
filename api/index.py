from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data)
            print("📥 Received payload:", data)

            # Do something with the payload, e.g., log to file or external service
            # For now, just acknowledge
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            response = {"status": "success", "message": "Payload received"}
            self.wfile.write(json.dumps(response).encode('utf-8'))

        except json.JSONDecodeError as e:
            self.send_response(400)
            self.send_header('Content-type','application/json')
            self.end_headers()
            response = {"status": "error", "message": "Invalid JSON"}
            self.wfile.write(json.dumps(response).encode('utf-8'))

        return
