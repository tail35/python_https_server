
from http.server import HTTPServer,SimpleHTTPRequestHandler
from socketserver import BaseServer
import ssl

httpd = HTTPServer(('my1.cow8.cn', 1443), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='certs/certificate.crt', keyfile='certs/private.key', server_side=True)
#httpd.socket = ssl.wrap_socket (httpd.socket, certfile='ssl/certificate.pem', keyfile='ssl/privatekey.pem', server_side=True)
httpd.serve_forever()