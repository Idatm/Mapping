#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *

# Connect infrared and touch sensors to any sensor ports
ir = InfraredSensor() 


for i in range(0,10):
    a = ir.proximity
    os.system("echo value "+i+" : "+a+" >> log.txt")
    sleep(5)
