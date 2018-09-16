import RPi.GPIO as GPIO
import spidev
import time
import os
import sys
from datetime import datetime

spi = spidev.SpiDev()
spi.open(0,0)

# global variables
count = 1
frequ = 0.5
stop_pressed = True
play = True
clear_reset = False

def GetData(channel):
    spi.max_speed_hz = 1350000
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3)<<8)+adc[2]
    return data

def ConvertVolts(data,places):
    volts = (data*3.3)/float(1023)
    volts = round(volts,places)
    return volts

def PotVolts(data,places):
    v = ConvertVolts(data,places)
    return v

def ConvertTemp(data,places):
    volt = ConvertVolts(data,places)
    Temp = (volt-0.5)/0.01
    Temp = round(Temp,places)
    return Temp

def LightPercent(data,places):
    V = ConvertVolts(data,places)
    Percent = (V/3)*100
    return Percent
