from printer import PrinterResponse
import RPi.GPIO as GPIO
import os
import sys
import time
import datetime
import socket

def start():
    GPIO.setmode(GPIO.BOARD)

    hostname = 'robostorm-toshiba.local'
    ip = socket.gethostbyname(hostname)
    # ip = '192.168.1.5'
    port = 80
    page = '/NameTag/ntap/response'

    buttonPin = 24
    shutDown = 26
    pressed = False

    GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(shutDown, GPIO.IN, pull_up_down = GPIO.PUD_UP)

    response = PrinterResponse(ip, port, page)

    while True:
        if not GPIO.input(buttonPin) and not pressed:
            print(datetime.datetime.now().strftime("\n%I:%M:%S%p on %B %d, %Y"))
            pressed = True
            print("Done Printing")
            response.send()
            time.sleep(1)
        # elif not GPIO.input(shutDown) and not pressed:
        #     pressed = True
        #     print("Shutdown")
        #     os.system("shutdown now -h")
        #     sys.exit(0)
        elif GPIO.input(buttonPin)and pressed:
            pressed = False
            time.sleep(1)
            #print "Button: ", GPIO.input(buttonPin), "Pressed: ", pressed
