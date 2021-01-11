
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

import array
from math import *
from matplotlib import pyplot

nb_mesures = 8                 # nb de mesures. Le robot tourne sur lui-même à chaque mesure de 2pi/nb_mesures

motor_rotation = 360           # à définir avec les tests
motor_speed = 600              # idem

ev3 = EV3Brick()

sens = UltrasonicSensor(Port.S4)

LeftMotor = Motor(Port.A)
RightMotor = Motor(Port.B)

vectorx = []
vectory = []

for i in range(0,nb_mesures):
    result = sens.distance()
    a = result*cos((2*pi*i)/nb_mesures)
    b = result*sin((2*pi*i)/nb_mesures)
    vectorx.append(int(a))
    vectory.append(int(b))
    LeftMotor.run_angle(motor_speed, int(motor_rotation/nb_mesures), wait=False)      # On fait tourner les moteurs. A changer en fonction de la structure du véhicule
    RightMotor.run_angle(-motor_speed, int(motor_rotation/nb_mesures), wait=True)


pyplot.scatter(vectorx, vectory)
pyplot.savefig('mapping.png')
pyplot.show()
