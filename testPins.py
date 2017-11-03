import wiringpi2 as wiringpi
import time

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(17,1)
wiringpi.digitalWrite(17,1)
time.sleep(4)
wiringpi.digitalWrite(17,0)
wiringpi.pinMode(17,0)
