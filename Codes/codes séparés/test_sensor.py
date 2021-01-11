#!/usr/bin/env pybricks-micropython
#from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
#from ev3dev2.sensor import INPUT_1
#from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
#from ev3dev2.led import Leds
from time import *
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor, TouchSensor, UltrasonicSensor
from pybricks.parameters import  Port, Stop, Direction, Button, Color
import os


ev3 = EV3Brick()

sens = UltrasonicSensor(Port.S4)

for i in range(0,10):
    #a = sens.proximity
    a = sens.distance()
    #os.system("echo value "+str(i)+" : "+str(a)+" >> ./log.txt")
    print(a)
    sleep(2)

