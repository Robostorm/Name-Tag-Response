import printer
import RPi.GPIO as GPIO
import os
import sys

GPIO.setmode(GPIO.BCM)

buttonPin = 7
shutDown = 8
ip = 'localhost'
port = 8080
page = '/ntap/response'

GPIO.setup(buttonPin, GPIO.IN, pull_up_up = GPIO.PUD_UP)
GPIO.setup(shutDown, GPIO.IN, pull_up_up = GPIO.PUD_UP)

response = printer.PrinterResponse(ip, port, page)

while True:
    if GPIO.input(buttonPin):
        print("Done Printing")
        response.send()
    if GPIO.input(shutDown):
        print("Shutdown")
        os.system("shutdown now -h")
        sys.exit(0)
