from machine import SPI, Pin, PWM
import tinypico as TinyPICO
from functions import *
# from micropython_dotstar import DotStar
import time, random, micropython

from machine import PWM, Pin

from ustruct import pack
from math import pi
import math as m
import ulab as u


print("starting")

# servo = my_i2c()

# ik = Leg_IK([0.03375, 0.065, 0.1])
ik = IK([0.03375, 0.065, 0.1], [0.4513422, 1.570796, 2.690251, -2.690251, -1.570796, -0.4513422])
xyz = u.array([[0.13, 0, 0],[0.1, 0, 0],[0.1, 0, -0.04],[0.1, 0, -0.04],[0.1, 0, -0.04],[0.1, 0, -0.04]])
xyz = u.array([[0.1, 0.05, -0.04],[0.1, 0.05, -0.04],[0.1, 0.05, -0.04],[0.1, 0.05, -0.04],[0.1, 0.05, -0.04],[0.1, 0.05, -0.04]])

ik.calc(xyz)
R_off = [0.05112, 0.04069, 0.05112, 0.05112, 0.04069, 0.05112]
theta_off = [0.4513422, 1.570796, 2.690251, -2.690251, -1.570796, -0.4513422]

neutral_pos = [0.1, 0, -0.05]
s1 = servo(4)
s2 = servo(14)
for i in range(100000):
    h = m.sin(m.pi*i/50)*0.04
    xyz[0] = u.array([0.15+h, 0, 0])
    angles = ik.calc(xyz)
    s1.set_servo(-angles[0][1])
    s2.set_servo(-m.pi/4-angles[0][2])


# while True:
    
#     i = i+1
#     # angle = m.sin(i/100)*80
#     pos = m.sin(i/60)*0.06 - 0.04
#     # if (i%100 == 0):
#     #     print(angle)
#     time.sleep_ms(1)

    
#     thetas = ik.calc([0.15, 0, pos])
#     thetas[2] = thetas[2]+pi/4
#     servo.set_servo(thetas[0], 0)
#     servo.set_servo(thetas[1]+0.2, 1)
#     servo.set_servo(thetas[2]-0.1, 2)

#     print(rad2deg(thetas[0]), rad2deg(thetas[1]), rad2deg(thetas[2]))
#     # servo.set_servo(deg2rad(angle), 0)
#     # servo.set_servo(deg2rad(angle), 1)





angle = deg2rad(80)
while True:
    angle = angle*-1
    # for i in range(16):
    #     servo.set_servo(angle, i)
    for i in range(3):
        servo.set_servo(deg2rad(0), i)
    # time.sleep_ms(500)


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
