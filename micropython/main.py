from machine import SPI, Pin
import tinypico as TinyPICO
from functions import *
# from micropython_dotstar import DotStar
import time, random, micropython

import machine
from ustruct import pack
from math import pi
import math as m
import ulab as u


print("starting")
servo = my_i2c()
# angle = m.sin(i / 10)
# print(angle * 180/m.pi)
i = 0
while True:
    i = i+1
    angle = m.sin(i/100)*80
    if (i%100 == 0):
        print(angle)
    time.sleep_ms(5)
    servo.set_servo(deg2rad(angle), 0)

# Configure SPI for controlling the DotStar
# Internally we are using software SPI for this as the pins being used are not hardware SPI pins
spi = SPI(
    sck=Pin(TinyPICO.DOTSTAR_CLK),
    mosi=Pin(TinyPICO.DOTSTAR_DATA),
    miso=Pin(TinyPICO.SPI_MISO),
)

# Say hello
print("\nHello from TinyPICO!")
print("--------------------\n")

# Show some info on boot
print("Battery Voltage is {}V".format(TinyPICO.get_battery_voltage()))
print("Battery Charge State is {}\n".format(TinyPICO.get_battery_charging()))

# Show available memory
print("Memory Info - micropython.mem_info()")
print("------------------------------------")
