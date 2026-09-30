path = '/home/pi/ETS_IoT kit demo24/DemoCode/BME280'
import time
import sys
sys.path.append(path)
import BME280lib as b
while True:
    t,p,h = b.readBME280All()
    print 'temperature :',t
    print 'pressure:',p
    print 'humidity:',h
    time.sleep(1)
    
    
    
    
    