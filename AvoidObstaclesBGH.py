# For the code to work - sudo pip install -U future
from __future__ import print_function
from __future__ import division
from builtins import input
# the aboe lines are meant for Python3 compatibility

# import BrickPi.py file to use BrickPi operations
from BrickPi import *

# setup the serial port for communication
BrickPiSetup()

# Constants
STATUS = 1
Velocity = 255
Motors = [PORT_A,PORT_B]

# Setup for ultrasonic sensor
# Define the port number here.
port1 = PORT_1
#Set the type of sensor at PORT_1
BrickPi.SensorType[port1] = TYPE_SENSOR_ULTRASONIC_CONT
print("Ultrasonic sensor set-up")

# Enable the Motors
BrickPi.MotorEnable[PORT_A] = 1 
BrickPi.MotorEnable[PORT_B] = 1
print("Motors enabled")

#Send the properties of sensors to BrickPi
BrickPiSetupSensors()
BrickPiUpdateValues()
print("Properties sent to BrickPi")
print("Robot ready to deploy")
print("STATUS = ", STATUS)
print("Velocity = ",Velocity)

# sleep for 5 seconds to read print statements
time.sleep(5)

# The following function moves robot in forward linear direction
def moveLinear(Velocity):
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[PORT_A] = Velocity
    BrickPi.MotorSpeed[PORT_B] = Velocity
    BrickPiUpdateValues()
    
# The following will slowdown robot while approaching obsticle
def slowDown(Velocity):
    BrickPiUpdateValues()
    moveLinear(Velocity//2)
    BrickPiUpdateValues()
        
# The following will stop robot prior to obsticle
def stopMoving():
    BrickPiUpdateValues()
    power = 0
    BrickPi.MotorSpeed[PORT_A] = power
    BrickPi.MotorSpeed[PORT_B] = power
    BrickPiUpdateValues()
    print ("Distance = ", stopDistance)

def changeDirection(STATUS):
    print ("STATUS = ",STATUS)
    # turn right
    BrickPiUpdateValues()
    
    
    print("Turned right")
    #get measurement
    BrickPiUpdateValues()
    
    #return to center
    BrickPiUpdateValues()
    
    #turn left
    BrickPiUpdateValues()

    #get measurement
    BrickPiUpdateValues()
    
    #return to center
    BrickPiUpdateValues()
    
    #return 1

def motorRotateDeg(power,deg,Motors,samplingTime=0.01,delyWhenStopping=0.05):
    initVal=[0]*Motors
    currVal=[0]*Motors
    finalVal=[0]*Motors
    lastEncod=[0]*Motors

    delta=0
    gain=0.005
    idelta=0.0
    alpha=10
    smulti=0
    BrickPiUpdateValues()
    WORKING on ADDING CODE

while STATUS == 1:
    # Ask BrickPi to update values for sensor / motors
    result = BrickPiUpdateValues()
    if not result:
        moveLinear(Velocity)
        stopDistance = BrickPi.Sensor[port1]
        print ("Distance = ",stopDistance)
        if stopDistance > 64:
            print("Distance > 64")
            Velocity = Velocity
        elif (stopDistance <= 64) and (stopDistance > 21):
            print("Distance < 64")
            slowDown(Velocity)
        elif stopDistance <= 21:
            STATUS = 2
            stopMoving()
            print("Stop Moving")
            STATUS = changeDirection(90,2)
            print ("STATUS = ", STATUS)
            
        # sleep for 10ms
        time.sleep(0.01)
