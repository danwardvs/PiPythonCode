from w1thermsensor import W1ThermSensor
import time

sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "000006299d6b")
sensor_2 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "00000629d6f4")

while 1 < 2:
    try:
        temperature_in_celsius = sensor.get_temperature()
        print("1: " + str(temperature_in_celsius))
    except error as e:
        print("Sensor not yet ready.")

    try:
        temperature_in_celsius_2 = sensor_2.get_temperature()
        print("2: " + str(temperature_in_celsius_2))
    except error as e:
        print("Sensor not yet ready.")
        
    
    time.sleep(0.1)
