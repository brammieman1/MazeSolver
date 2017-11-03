import time
import wiringpi

SPIchannel = 0
SPIspeed = 10 #Hz
wiringpi.wiringPiSetupGpio()
wiringpi.wiringPiSPISetup(SPIchannel, SPIspeed)

#GPIO pins
gpio0 = 17
gpio1 = 18
gpio2 = 27
gpio3 = 22
gpio4 = 23
gpio5 = 24
gpio6 = 25
writePins = [gpio0, gpio1, gpio2]
readPins = [gpio3, gpio4, gpio5, gpio6]

#Test data
data = [1,0,1,0,1,1]
dataArray = [[1,0,1,0,1,1,0,1,1,1,0],[1,0,1,0,1,1,1,0],[1,0,1,0,1,1]]

#Constants
byteSize = 8  #size of the dataparts to be send

#sending scheme
#2 1 0 | miso
#-------------------------
#0 0 1 | x size
#0 1 0 | y size
#0 1 1 | maze
#1 0 0 | start point
#1 0 1 | end point

def sendXSize(xSize): #xSize should be an integer
   pins = [gpio0]
   xSize8 = xSize + (byteSize - xSize%byteSize) #increase xSize to be the closest multiple of byteSize
   data = [xSize8]
   sendData(data, pins)

def sendYSize(ySize): #ySize should be an integer
   pins = [gpio1]
   ySize8 = ySize + (byteSize - ySize%byteSize) #increase ySize to be the closest multiple of byteSize
   data = [ySize8]
   sendData(data, pins)

#def sendMaze(maze): #maze should be a 2 dimensional array
   #do nothing

def sendData(dataArray, gpios): #dataArray is an array with the data to be send
   """This function will send the data that is entered in an array to the FPGA"""
   gpioOn(gpios)

   i = 0
   for x in dataArray:
     print("Data", x, "is send")
     copy = x
     print("SEND")
     print(bytes([x]))

   #  for y in range(2):
     recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, bytes([x]))
     time.sleep(8*(1/SPIspeed))
     recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, bytes([copy]))
     time.sleep(8*(1/SPIspeed))

     print("RECEIVED")
     print(recvData[1])

     i += 1

   gpioOff()

def gpioOn(pins): #pins is an array of gpio pins
   for gpio in pins:
     print("pin", gpio, "is turned on")
     wiringpi.pinMode(gpio, 1)
     wiringpi.digitalWrite(gpio, 1)

def gpioOff(): 
 
 """Turn of all GPIO Pins"""

 for gpio in writePins:
   wiringpi.digitalWrite(gpio, 0)
   wiringpi.pinMode(gpio, 0)
   print("pin", gpio, "is turned on")
 #for gpio in readPins:
