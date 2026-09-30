import sys
sys.path.append('home/pi/Adafruit-Raspberry-Pi-Python-Code-legacy/Adafruit_MCP230xx')
from Adafruit_MCP230XX import Adafruit_MCP230XX

mcp = Adafruit_MCP230XX(busnum=1,address=0x20,num_gpios=16)
mcp.config(0,mcp.output)
mcp.config(4,mcp.output)
mcp.config(8,mcp.output)

while True:
    mcp.output(0,1)
    mcp.output(4,1)
    mcp.output(8,1)
    time.sleep(1)
    mcp.output(0,0)
    mcp.output(4,0)
    mcp.output(8,0)
    time.sleep(1)
    
    
     