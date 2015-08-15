from printer import PrinterResponse
import socket

# hostname = 'robostorm-toshiba.local'
# ip = socket.gethostbyname(hostname)
ip = '127.0.0.1'
port = 8080
page = '/NameTag/ntap/response'

response = PrinterResponse(ip, port, page)
response.send()