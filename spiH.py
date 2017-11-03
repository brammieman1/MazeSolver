import sys
import time 
import wiringpi

SPIchannel = 0  # SPI Channel (CE0)
SPIspeed = 10  # Clock Speed in Hz
wiringpi.wiringPiSetupGpio()
wiringpi.wiringPiSPISetup(SPIchannel, SPIspeed)

#   prefix = str(0)   # 63 is send something back. 85 is only send.
#   sendData = bytes([0b11010001]) # will send ONE bytes, a byte 1
#   random = bytes([0b11010001])

final = 0b111
setupdata = [0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01]
setup2 =[0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02]
setup123 = [0x01, 0x01, 0x01, 0x02, 0x02, 0x02, 0x03, 0x03, 0x03, 0x04, 0x04, 0x04]
data = [0b1, 0b10, 0b11, 0b100, 0b101, final]
data2 = [0b111]
copy = data
fillData = [0xab, 0xab, 0xff, 0xff, 0xff, 0xff,0xff,0xff, 0xff, 0xff, 0xff]
result = []

i = 0


for a in data:
   print("THIS IS ROUND", i)
   print("SEND")
   print(bin(int.from_bytes(bytes([a]), byteorder=sys.byteorder)))
   recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, bytes([a]))
   time.sleep(8*(1/SPIspeed))
 #  print("2 value of a")
#   print(x)
   print("RECEIVED")
   print(bin(int.from_bytes(recvData[1], byteorder=sys.byteorder)))
   i += 1

"""f
for x in data:
   print("Now you should receive the right data")
   print("THIS IS ROUND", i)
   print("SEND")
   print(bytes([x]))
   recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, bytes([x]))
   time.sleep(8*(1/SPIspeed))
 #  print("2 value of a")
#   print(x)
   print("RECEIVED")
   print(bin(int.from_bytes(recvData[1], byteorder=sys.byteorder)))
   i += 1

print("We are now waiting for received data")

#while True:
for z in fillData:
 #  numb = fillData
   print("THIS IS ROUND", i)
   print("SEND")
   print(bytes([z]))
   recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, bytes([z]))
   time.sleep(8*(1/SPIspeed))
#   print("2 value of a")
#   print(numb)
 #  print(type(recvData[1]))
   print("RECEIVED")
   print(bin(int.from_bytes(recvData[1], byteorder=sys.byteorder)))
   if recvData[1] == final:
      print("Yay we received the final value")
      printing()
      break
   i = i + 1

def printing():
   for y in range(len(copy)):
      print("This data was received:")
      print("Send:", copy[y], "Received:", data[y])

"""
