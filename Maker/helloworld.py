import pycurl    

c = pycurl.Curl()

postfields = '"Hello World"'
c.setopt(c.URL, 'https://maker.ifttt.com/trigger/test/with/key/mS0iVg2H24gBSRVCLxBt2APtRT4vPcUp5XU_bVr7xaP')
# Here we set data for POST request
c.setopt(c.POSTFIELDS, postfields)

c.perform()
c.close()

print("Done!")
