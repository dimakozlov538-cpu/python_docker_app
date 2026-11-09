from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<h1>ABOBA.</h1>".encode("utf-8"))

server = HTTPServer(("0.0.0.0", 8000), MyHandler)
print("run 8000")
server.serve_forever()
