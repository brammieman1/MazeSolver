import spidev
import time
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1
while True:
	resp = spi.xfer2([0xDE])
        print resp[0]
	time.sleep(1)
