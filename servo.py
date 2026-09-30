import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

SERVO = 22
GPIO.setup(SERVO, GPIO.OUT)

pwm = GPIO.PWM(SERVO, 100)
pwm.start(5)

for angle in range(10, 161, 10):

    duty = angle / 10 + 2.5

    pwm.ChangeDutyCycle(duty)
    time.sleep(0.8)

pwm.stop()
GPIO.cleanup()