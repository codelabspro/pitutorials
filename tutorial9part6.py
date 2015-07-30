import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

GPIO.output(12, 1)
time.sleep(2)
GPIO.output(12, 0)
time.sleep(2)
GPIO.output(12, 1)
time.sleep(2)
GPIO.output(12, 0)

p = GPIO.PWM(7, 50)
p.start(0)

try:
	while True:
		p.ChangeDutyCycle(7.5)
		time.sleep(1)
		p.ChangeDutyCycle(12.5)
		time.sleep(1)
		p.ChangeDutyCycle(2.5)
		time.sleep(1)


except KeyboardInterrupt:
	p.stop()
    GPIO.cleanup()a

