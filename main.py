import printer

ip = 'localhost'
port = 8080
page = '/ntap/response'

response = printer.PrinterResponse(ip, port, page)

response.send()
# response.asyncSend()
