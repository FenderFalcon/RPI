 # Servo Control
import time
import wiringpi
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.1
pulse = 135

 while True:
 	if(GPIO.input(23) == False):
 		if(pulse <= 250):
 			pulse +=1
 	if(GPIO.input(24) == False):
 		if(pulse >= 20):
 			pulse -=1
 	wiringpi.pwmWrite(18, pulse)
    time.sleep(delay_period)