import socketserver
import http.server

server = socketserver.TCPServer(('0.0.0.0', 80), http.server.SimpleHTTPRequestHandler)
print('Start web using port 80')
server.serve_forever()
