import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# Servo motor
GPIO.setup(7, GPIO.OUT)
# White LED
GPIO.setup(11, GPIO.OUT)
# Green LED
GPIO.setup(12, GPIO.OUT)
# Yellow LED
GPIO.setup(13, GPIO.OUT)
# Red LED
GPIO.setup(15, GPIO.OUT)
'''
p12 = GPIO.PWM(12, 50)
p12.start(0)

try:
	while True:
		for i in range(100):
			p12.ChangeDutyCycle(i)
			time.sleep(0.02)
		for i in range(100):
			p12.ChangeDutyCycle(100-i)
			time.sleep(0.02)


except KeyboardInterrupt:
	pass

p12.stop()
'''
GPIO.output(12, 1)
time.sleep(2)

GPIO.output(11, 1)
time.sleep(2)
GPIO.output(11, 0)
time.sleep(2)


GPIO.output(13, 1)
time.sleep(2)
GPIO.output(13, 0)
time.sleep(2)







p4 = GPIO.PWM(15, 50)
p4.start(0)

p5 = GPIO.PWM(7, 50)
p5.start(7.5)

try:
	while True:

		p4.ChangeDutyCycle(50)
		time.sleep(0.02)
		p4.ChangeDutyCycle(75)
		time.sleep(0.02)
		p5.ChangeDutyCycle(7.5)
		time.sleep(1)
		p5.ChangeDutyCycle(12.5)
		time.sleep(1)
		p5.ChangeDutyCycle(2.5)
		time.sleep(1)
		
except KeyboardInterrupt:
	pass


GPIO.output(12, 0)
p4.stop()
p5.stop()
p15.stop()
GPIO.cleanup()
