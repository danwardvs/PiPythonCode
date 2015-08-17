import pycurl, json


c = pycurl.Curl()

message = raw_input('"Enter a message:')

print("Sending request...")

url="https://maker.ifttt.com/trigger/message/with/key/mS0iVg2H24gBSRVCLxBt2APtRT4vPcUp5XU_bVr7xaP"

data = json.dumps({"value1" : message})

c.setopt(c.URL, url)
c.setopt(c.HTTPHEADER, ['Content-Type: application/json'])
c.setopt(pycurl.POST,1)
c.setopt(pycurl.POSTFIELDS,data)


c.perform()
c.close()

print("Sent request")
