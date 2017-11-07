import time
import wiringpi
import sys

SPIchannel = 0
SPIspeed = 50  #Hz
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
writePins = [gpio0, gpio1, gpio2, gpio3, gpio6]
readPins = [gpio4, gpio5, gpio6]

#Test data
dataArray = [[1,0,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,1,1],[1,0,1,0,1,1]]
matrix = [[1,0,1,1,0,1,0,1],[0,0,0,1,1,0,1,0],[1,1,1,0,0,1,1,0]]
testData = [0x01, 0x01, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09]

#Constants
byteSize = 8  #size of the dataparts to be send
stuffing = 1

#global variables
socDatax = []
socDatay = []

#sending scheme
#2 1 0 | miso
#-------------------------
#0 0 1 | x size
#0 1 0 | y size
#0 1 1 | maze
#1 0 0 | start point x
#1 0 1 | end point x
#1 1 0 | start point y
#1 1 1 | end point y

#gpio 3
#0 -> 1 | soc can send
#1 -> 0 | pi won't receive

#receiving scheme
#6 5 4 |
#-------------------------
#0 0 1 | SOC is sending
#0 1 0 |
#0 1 1 |
#1 0 0 |
#1 0 1 |
#1 1 0 |
#1 1 1 |

def sendXSize(xSize): #xSize should be an integer
   pins = [gpio0]
   modulo = xSize%byteSize
   if modulo>0:
       xSize8 = xSize + (byteSize - modulo) #increase xSize to be the closest multiple of byteSize
   else:
       xSize8 = xSize

   sendData([xSize8], pins, True)

def sendYSize(ySize): #ySize should be an integer
   pins = [gpio1]
   modulo = ySize%byteSize
   if modulo>0:
       ySize8 = ySize + (byteSize - modulo) #increase ySize to be the closes$
   else:
       ySize8 = ySize

   sendData([ySize8], pins, True)

def sendMaze(mazeArray): #mazeArray should be an a 2 dimensional array
   """this funchtion will call convert on the array and then send the bytes
     of the array with sendData()"""
   pins = [gpio0, gpio1]
   sendArray = convert(mazeArray)
   sendData(sendArray, pins, False)

def sendStart(sP):
   """this function will send 2 values: the x and y coordinates of the startpoint of the maze"""
   sPX, sPY = sP

   xpins = [gpio2]
   sendData([sPX], xpins, True)

   ypins = [gpio2, gpio1]
   sendData([sPY], ypins, True)

def sendEnd(eP):
   ePX, ePY = eP

   xpins = [gpio2, gpio0]
   sendData([ePX], xpins, True)

   ypins = [gpio2, gpio1, gpio0]
   sendData([ePY], ypins, True)

def convert(bitArray): #Array is an array with data from the maze
   out = 0
   binArray = []
   i = 0
   for array in bitArray:
     for bit in array:
       out = (out << 1) | bit
       #if i == 7 has to be before i == len(x) as the size could be equal to 8.
       if i == (byteSize - 1):
         binArray.append(out)
         out = 0
       elif i == (len(array)-1):
         for bitX in range(byteSize-((i+1)%byteSize)):
           out = (out << 1) | stuffing
         binArray.append(out)
         out = 0
       i += 1
     i = 0
     print( "This was array:", array)
   return(binArray) 

def sendData(dataArray, gpios, maze): #dataArray is an array with the data to be send
   """This function will send the data that is entered in an array to the FPGA"""
   gpioOn(gpios)
   isInt = maze

   i = 0
   for x in dataArray:
     if isInt:
        x = x.to_bytes(1, 'big')
     else:
        x = x.to_bytes(2, 'big')
     print("Data", x, "is send")
     copy = x
     print("SEND")
     print(x) #bytes([x]))

   #  for y in range(2):
     recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, x) #bytes([x]))
     time.sleep(8*(1/SPIspeed))
     recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, x) #bytes([copy]))
     time.sleep(8*(1/SPIspeed))

     print("RECEIVED")
     print(recvData[1])

     i += 1

   gpioOff()

def readSoc():
    pins = [gpio3]
    gpioOn(pins)
    x = 0
    y = x.to_bytes(2, 'big')
    socDatax = []
    socDatay = []
    intToAdd = 0

 #   wiringpi.pinMode(gpio6, 1)
 #   wiringpi.digitalWrite(gpio6, 1)

#    y = 0
#    for x in testData:
#        recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, bytes([x]))  # for testing
#        if y == 1:
#            socDatay.append(int.from_bytes(recvData[1], byteorder=sys.byteorder))
#            y = 0
#        if y == 0:
#            socDatax.append(int.from_bytes(recvData[1], byteorder=sys.byteorder))
#            y = 1



   # recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, bytes([x])) NOT SURE IF NEEDED
   # try: 
    while (wiringpi.digitalRead(gpio6) != 1):
        c = 0
    while (wiringpi.digitalRead(gpio6)):
        recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, y)
        if wiringpi.digitalRead(gpio4):
    #       recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, y)
           print("got x coordinate")
           print("RECEIVED")
           print(recvData[1])
           socDatax.append(int.from_bytes(recvData[1], byteorder=sys.byteorder)) #check whether extra recvdata is needed
        elif wiringpi.digitalRead(gpio5):
           print("got y coordinate")
           print("RECEIVED")
           print(recvData[1])
           socDatay.append(int.from_bytes(recvData[1], byteorder=sys.byteorder))
        time.sleep(8 * (1 / SPIspeed))
    
  #  wiringpi.pinMode(gpio6, 0)
   # wiringpi.digitalWrite(gpio6, 0)
    #finally:
    gpioOff()
    return handleRecv(socDatax, socDatay)

def handleRecv(xCoords, yCoords):
    x = 0
    route = []
    for x in range(len(xCoords)-1):
        route.append((int.from_bytes(xCoords[x]), int.from_bytes(yCoords[x])))

    return route
    print("I am now handling")


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
     print("pin", gpio, "is turned off")
 #for gpio in readPins:


def mazeToSoc(xSize, ySize, maze, sP, eP):
   sendXSize(xSize)
   sendYSize(ySize)
   sendMaze(maze)
   sendStart(sP)
   sendEnd(eP)
   readSoc()
#READ FUNCTION THAT WILL GET THE DATA FROM SOC


