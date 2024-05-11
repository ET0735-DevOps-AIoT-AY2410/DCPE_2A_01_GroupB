import RPi.GPIO as GPIO
import threading
import time
from time import sleep

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

# Air Temperature Sensor = 3
# EC Sensor = 5
# Humidity Sensor = 12
# PH Sensor = 13

# UV Light (LED) = 22
# Exhaust Fan = 26
# Servo Motor = 37

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.input)
GPIO.setup(5, GPIO.input)
GPIO.setup(12, GPIO.input)
GPIO.setup(13, GPIO.input)

GPIO.setup(22, GPIO.output)
GPIO.setup(26, GPIO.output)
GPIO.setup(37, GPIO.output)

def maintain_airtemp():
    airtemp = GPIO.input(3)
    while airtemp>25:
        GPIO.output(26, GPIO.HIGH) # Turns on the Exhaust Fan
    else:
        GPIO.output(26, GPIO.LOW) # Turns off the Exhaust Fan

# Thread to monitor air temperature in background
airtemp_thread = threading.Thread(target=maintain_airtemp)
airtemp_thread.start()

def maintain_ec():
    ec_level = GPIO.input(5)
    ec_upperlimit = 1
    ec_lowerlimit = 2
    servo1 = GPIO.PWM(37, 50)
    while ec_level>ec_upperlimit:
        servo1.start(5)
        sleep(0.1)
        servo1.stop()
        sleep(0.1)
        












GPIO.cleanup