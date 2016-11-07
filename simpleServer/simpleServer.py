import socketserver
import http.server

httpServer = SocketServer.TCPServer(('', 1337), SimpleHTTPAServer.SimpleHTTPRequestHandler)
httpServer.serve_forever()
