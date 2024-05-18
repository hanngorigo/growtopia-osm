import socketserver
import http.server

server = socketserver.TCPServer(('0.0.0.0', 8080), http.server.SimpleHTTPRequestHandler)
print('Start web using port 8080')
server.serve_forever()
