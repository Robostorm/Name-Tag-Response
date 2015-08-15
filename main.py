from printer import PrinterResponse
import RPi.GPIO as GPIO
import os
import sys
import time
import datetime
import socket

def start():
    # ============
    #   Settings
    # ============

    GPIO.setmode(GPIO.BOARD)

    ip = '192.168.1.22'
    port = 80
    page = '/NameTag/ntap/response'

    #Pre B+
    bDonePin = 24
    bHaltPin = 26

    #B+ and Pi 2
    pDonePin = 38
    pHaltPin = 40

    doneDelay = 0
    haltDelay = 1000

    # ================
    #   End Settings
    # ================

    # Setup

    donePin = bDonePin
    haltPin = bHaltPin

    # Get time in milliseconds
    def millis():
        return int(round(time.time()*1000))

    # Log a mesage
    def log(msg):
        print(datetime.datetime.now().strftime("%I:%M:%S:%f")+": "+msg)

    # Called when done button is pressed
    def done():
        log("Done")
    #response.send()

    # Called when halt button is pressed
    def halt():
        log("Halt")
        os.system("halt")

    if GPIO.RPI_REVISION >= 3:
        donePin = pDonePin
        haltPin = pHaltPin
        print("B+ or Pi 2")
    else:
        print("Pi 1 not +")

    donePressed = False
    haltPressed = False
    doneMillis = 0;
    haltMillis = 0;

    GPIO.setup(donePin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(haltPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

    GPIO.add_event_detect(donePin, GPIO.BOTH)
    GPIO.add_event_detect(haltPin, GPIO.BOTH)

    response = PrinterResponse(ip, port, page)

    # Main Loop

    while True:
        if GPIO.event_detected(donePin):
            if not GPIO.input(donePin):
                log("Done Pressed")
                doneMillis = millis()
                donePressed = True
            else:
                log("Done Released")
                donePressed = False

        if GPIO.event_detected(haltPin):
            if not GPIO.input(haltPin):
                log("Halt Pressed")
                haltMillis = millis()
                haltPressed = True
            else:
                log("Halt Released")
                haltPressed = False

        if donePressed:
            if millis() - doneMillis >= doneDelay:
                donePressed = False
                done()

        if haltPressed:
            if millis() - haltMillis >= haltDelay:
                haltPressed = False
                halt()
