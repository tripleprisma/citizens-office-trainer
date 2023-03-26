from http.server import HTTPServer, SimpleHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
  print('🚀 Starting server at http://localhost:1234')
  print('You can stop it with Ctrl + C')

  server_address = ('192.168.0.239', 1234)
  httpd = server_class(server_address, handler_class)
  httpd.serve_forever()

run()