import httplib
import socket
import urllib
import thread

class PrinterResponse:

    ip = '127.0.0.1'
    port = 8080
    page = '/ntap/response'

    def __init__(self, ip, port, page):
        self.ip = ip
        self.port = port
        self.page = page

    def send(self):
        hostname = socket.gethostname()
        printer = socket.gethostbyname(hostname)

        print "printer IP: %s" % printer

        print self.ip, " : ", self.port, " : ", self.page
        connection = httplib.HTTPConnection(self.ip, self.port)
        connection.connect()

        params = urllib.urlencode({'printer': printer})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        connection.request('POST', self.page, params, headers)

        response = connection.getresponse()
        if response.status == httplib.OK:
            print response.read(), response.reason
        else:
            print response.status, response.reason

        connection.close()

    def asyncSend(self):
        try:
            thread.start_new_thread(self.send, ())
        except Exception:
            print "Error: unable to start thread"
