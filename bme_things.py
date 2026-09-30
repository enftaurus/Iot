path = '/home/pi/ETS_IoT kit demo24/DemoCode/BME280'
import time
import sys
import urllib.request as url
sys.path.append(path)
import BME280lib as b
while True:
    t,p,h = readBME280All()
    print 'temp:',t
    print 'pressure:',p
    print 'humidity:',h
    req_link = url.urlopen(link % (t,p,h))
    req_link.close()
    
    
    
    
    
    