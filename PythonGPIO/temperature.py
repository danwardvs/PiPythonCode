from w1thermsensor import W1ThermSensor
import time

sensor = W1ThermSensor()

while 1 < 2:
    temperature_in_celsius = sensor.get_temperature()
    print(temperature_in_celsius)
    time.sleep(0.1)
