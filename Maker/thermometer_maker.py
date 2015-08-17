#!/usr/bin/env python

import pycurl, json
from w1thermsensor import W1ThermSensor
import time

sensor = W1ThermSensor()



c = pycurl.Curl()

temperature_in_celsius = sensor.get_temperature()
print("Aquired Temperature")

print("Sending request...")

url="https://maker.ifttt.com/trigger/templog/with/key/mS0iVg2H24gBSRVCLxBt2APtRT4vPcUp5XU_bVr7xaP"

data = json.dumps({"value1" : temperature_in_celsius})

c.setopt(c.URL, url)
c.setopt(c.HTTPHEADER, ['Content-Type: application/json'])
c.setopt(pycurl.POST,1)
c.setopt(pycurl.POSTFIELDS,data)


c.perform()
c.close()

print("Sent request")
