import time 
import wiringpi

SPIchannel = 0  # SPI Channel (CE0)
SPIspeed = 1  # Clock Speed in Hz
wiringpi.wiringPiSetupGpio()
wiringpi.wiringPiSPISetup(SPIchannel, SPIspeed)

#   prefix = str(0)   # 63 is send something back. 85 is only send.
sendData = bytes([0b11010001]) # will send ONE bytes, a byte 1
random = bytes([0b11010001])
list = [0b1
i = 0
for x in list:
while i <= 10:
   print("1 value of a")
   print(random)
   recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, random)
   time.sleep(1)
   print("2 value of a")
   print(random)
   print(type(recvData[1]))
   print("received value:")
   print(recvData[1])
   i = i + 1
print(recvData[1])
