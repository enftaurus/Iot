import sys
sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code-legacy/Adafruit_MCP230xx')
from Adafruit_MCP230XX import Adafruit_MCP230XX
mcp=Adafruit_MCP230XX(busnum=1,address=0x20,num_gpios=16)
mcp.config(0,mcp.input)
mcp.pullup(0,1)
while True:
    i = mcp.input(0)
    if i==1:
        print 'available'
    else:
        print 'not available'
    time.sleep(1)
    
