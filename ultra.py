import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
TRIG=16
ECHO=18

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

print("ultrasonic measurement")


GPIO.output(TRIG,False)
time.sleep(0.5)


while True:
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    
    while GPIO.input(ECHO)==True:
        start=time.time()
        
    while GPIO.input(ECHO)==False:
        stop=time.time()
        
    elapsed = stop-start
    distance = (elapsed*34300)/2
    print('distance:',round(distance,2),'cm')
    time.sleep(1)