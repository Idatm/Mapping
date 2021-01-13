#!/usr/bin/env pybricks-micropython
#from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
#from ev3dev2.sensor import INPUT_1
#from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
#from ev3dev2.led import Leds
from time import *
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor, TouchSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import  Port, Stop, Direction, Button, Color
import os

import array
from math import *
#from matplotlib import pyplot

nb_mesures = 16                 # nb de mesures. Le robot tourne sur lui-même à chaque mesure de 2pi/nb_mesures

motor_rotation = 360           # à définir avec les tests
motor_speed = 50              # idem

ev3 = EV3Brick()

sens = UltrasonicSensor(Port.S1)
gyro = GyroSensor(Port.S4)

LeftMotor = Motor(Port.A)
RightMotor = Motor(Port.B)

#gyro.calibrate()

vectorx = []
vectory = []
ggr = []
results = []

for i in range(0,nb_mesures):
    result = sens.distance()
    results.append(int(result))
    a = result*cos((2*pi*i)/nb_mesures)
    b = result*sin((2*pi*i)/nb_mesures)
    vectorx.append(int(a))
    vectory.append(int(b))
    #LeftMotor.run_angle(motor_speed, int(motor_rotation/nb_mesures), wait=False)      # On fait tourner les moteurs. A changer en fonction de la structure du véhicule
    #RightMotor.run_angle(-motor_speed, int(motor_rotation/nb_mesures), wait=True)
    LeftMotor.run(motor_speed) #, wait=False)
    RightMotor.run(-motor_speed)  #, wait=False)
    while(gyro.angle() < (360/nb_mesures)):
        res = sens.distance()

    LeftMotor.stop()
    ggr.append(gyro.angle())
    RightMotor.stop()
    gyro.reset_angle(0)


LeftMotor.run(motor_speed) #, wait=False)
RightMotor.run(-motor_speed) #, wait=False)
while(gyro.angle() < (360*(results.index(max(results)))/nb_mesures) ):
    res = sens.distance()
LeftMotor.run(-500)
RightMotor.run(-500)
distance1 = sens.distance()
while(sens.distance() > 1000):
    res= sens.distance()
LeftMotor.stop()
RightMotor.stop()
distance2 = sens.distance()
x1 = (distance1-distance2)*cos(gyro.angle())
y1 = (distance1-distance2)*sin(gyro.angle())

while(gyro.angle() < 360):
    LeftMotor.run(motor_speed)
    RightMotor.run(-motor_speed)
LeftMotor.stop()
RightMotor.stop()

for i in range(0,nb_mesures):

    result = sens.distance()
    a = result*cos((2*pi*i)/nb_mesures) + x1
    b = result*sin((2*pi*i)/nb_mesures) + y1
    vectorx.append(int(a))
    vectory.append(int(b))
    results.append(int(result))
    #LeftMotor.run_angle(motor_speed, int(motor_rotation/nb_mesures), wait=False)      # On fait tourner les moteurs. A changer en fonction de la structure du véhicule
    #RightMotor.run_angle(-motor_speed, int(motor_rotation/nb_mesures), wait=True)
    LeftMotor.run(motor_speed) #, wait=False)
    RightMotor.run(-motor_speed) #, wait=False)
    while(gyro.angle() < 360/nb_mesures):
        res = sens.distance()
    LeftMotor.stop()
    RightMotor.stop()
    gyro.reset_angle(0)

os.system("echo "+str(results)+" > raw_data.log")
os.system("echo "+str(ggr)+" > gyro.log")
os.system("echo "+str(vectorx)+" "+str(vectory)+" > results.log")

#pyplot.scatter(vectorx, vectory)
#pyplot.savefig('mapping.png')
#pyplot.show()
