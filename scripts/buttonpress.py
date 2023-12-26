# buttonpress.py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20,GPIO.IN)
GPIO.setup(21,GPIO.OUT)

while True:
    while GPIO.input(20) == GPIO.LOW:
        time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things
        print('Input is LOW')
        GPIO.output(21,GPIO.HIGH)
    print('Input is HIGH')
    GPIO.output(21,GPIO.LOW)
