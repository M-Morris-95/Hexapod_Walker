import ulab as u
import math as m
from machine import SPI, Pin
import tinypico as TinyPICO
import time, random, micropython
import machine
from ustruct import pack
from math import pi

class FK:
    def __init__(self, lengths, theta_off = 0, r_off = 0):
        self.L=lengths # lengths of leg at hip, thigh and shin
        self.alpha = u.array([0,deg2rad(90),0,0]) # DH params alpha
        self.r_off = r_off # offset from centre to start of hip (mm)
        self.theta_off = theta_off # offset from positive x of spider to positive x of hip

    def calc(self, theta):
        d = u.array([0,0,0,0])

        r = [self.r_off, self.L[0], self.L[1], self.L[2]]
        theta = [self.theta_off, theta[0], theta[1], theta[2]]
        pos = [self.DH(d[0], theta[0], self.alpha[0], r[0])]

        for i in range(1,4):
            pos.append(u.linalg.dot(pos[-1], self.DH(d[i], theta[i], self.alpha[i], r[i])))

        return pos

    def DH(self, d, theta, alpha, r):
        DH = u.array([
            [m.cos(theta), -m.sin(theta)*m.cos(alpha),  m.sin(theta)*m.sin(alpha), r*m.cos(theta)],
            [m.sin(theta),  m.cos(theta)*m.cos(alpha), -m.cos(theta)*m.sin(alpha), r*m.sin(theta)],
            [0,             m.sin(alpha)             ,  m.cos(alpha)             , d],
            [0,0,0,1]
        ]) 
        return DH

def deg2rad(input):
    return input*m.pi/180



class my_i2c:
    def __init__(self):
        self.i2c = machine.I2C(-1, machine.Pin(22), machine.Pin(21))
        self.slave = 0x40
        self.i2c.writeto_mem(self.slave, 0x00, b"\x10")  # set mode1 to sleep
        time.sleep_us(5)
        prescale = int((25000000 / (4096 * 50)) + 0.5)
        self.i2c.writeto_mem(self.slave, 0xFE, pack("B", prescale))  # setprescale
        self.i2c.writeto_mem(self.slave, 0x00, b"\xa1")  # set mode1
        time.sleep_us(5)
        self.step = 200 / (pi / 2)
        for servo in range(16):
            on_time = servo * 220
            off_time = on_time + 340
            self.i2c.writeto_mem(
                self.slave, 0x06 + (servo * 4), pack("<HH", on_time, off_time)
            )

    def set_servo(self, pos, servo):
        on_time = servo * 220
        off_time = on_time + 340 - int(pos * self.step)
        # self.i2c.writeto_mem(0x40, 0x06 + (servo*4), pack('<HH', on_time, off_time))
        self.i2c.writeto_mem(self.slave, 0x08 + (servo * 4), pack("<H", off_time))