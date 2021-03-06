#!/usr/bin/env python3

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

pin = 4 # The pin ID, edit here to change it
maxTMP = 60 # The maximum temperature in Celsius after which we trigger the fan

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setwarnings(False)
    return()

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    # print("temp is {0}".format(temp)) #Uncomment here for testing

    return temp
def fanON():
    setPin(True)
    return()
def fanOFF():
    setPin(False)
    return()
def getTEMP():
    CPU_temp = round(float(getCPUtemperature()))
    print(CPU_temp)
    if CPU_temp>maxTMP:
        fanON()
    else:
        fanOFF()
    return()
def setPin(mode): # A little redundant function but useful if you want to add logging
    GPIO.output(pin, mode)
    return()

try:
    setup()
    while True:
        getTEMP()
        sleep(60) # Read the temperature every 5 sec, increase or decrease this limit if you want
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    GPIO.cleanup() # resets all GPIO ports used by this program
    
    #This was one of my first projects on the pi and I no longer have the source of the code I used, therefore I do not claim this entire snippet of code is mine
