from http.server import HTTPServer, BaseHTTPRequestHandler
import os
HOST = "127.0.0.1"
PORT = 8000

class Server(BaseHTTPRequestHandler):
   def do_GET(self):
       if self.path == '/':
           self.path = '/text.html'
       try:
        buka_file = open(self.path[1:]).read()
        self.send_response(200)
       except:
        buka_file = "404 Not Found"
        self.send_response(404)
       self.end_headers()
       self.wfile.write(bytes(buka_file, 'utf-8'))


server = HTTPServer((HOST, PORT), Server)
print ("Server is Running")
server.serve_forever()
server.server_close()

