import RPi.GPIO as GPIO
import time
import sys
import signal 

# Set Broadcom mode so we can address GPIO pins by number.
GPIO.setmode(GPIO.BCM) 

# This is the GPIO pin number we have one of the door sensor
# wires attached to, the other should be attached to a ground pin.DOOR_SENSOR_PIN = 18
 
DOOR_SENSOR_PIN=18
# Initially we don't know if the door sensor is open or closed...
isOpen = None
oldIsOpen = None 


# Set up the door sensor pin.
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP) 





while True: 
    oldIsOpen = isOpen 
    isOpen = GPIO.input(DOOR_SENSOR_PIN)


    if (isOpen and (isOpen != oldIsOpen)):  
        print ("Door is open")   
    elif (isOpen != oldIsOpen):  
        print ("Door is closed")  


    time.sleep(0.1)