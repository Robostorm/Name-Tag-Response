import printer

ip = '192.168.1.22'
port = 80
page = '/NameTag/ntap/response'

response = printer.PrinterResponse(ip, port, page)
response.send()
