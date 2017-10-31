import time
import wiringpi

SPIchannel = 0  # SPI Channel (CE0)
SPIspeed = 10  # Clock Speed in Hz
wiringpi.wiringPiSetupGpio()
wiringpi.wiringPiSPISetup(SPIchannel, SPIspeed)

count = 0

while (True):
    prefix = chr(63)   # 63 is send something back. 85 is only send.
    sendData = chr(85)  # will send ONE bytes, a byte 1
    recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, prefix + sendData)
    count = count + 1
    time.sleep(1)
    print(count)
    print('receiveddata =', recvData[1])

