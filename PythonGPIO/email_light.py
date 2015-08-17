
import RPi.GPIO as GPIO, feedparser, time, os.path

USERNAME = "dannyvanstemp@gmail.com"   
PASSWORD = "asdfadsf!"     

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LIGHTS = 18
GPIO.setup(7, GPIO.OUT)



cur_mails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
       
print("You have " + str(cur_mails) + " emails in your inbox.")

if os.path.isfile("emails.txt") == False: #create the file if it doesnt exist
    f = open('emails.txt', 'w')
    f.write('1'); #The interpreter doesn't like reading from an empty file
    f.close

f = open('emails.txt', 'r')
last_mails = int(f.read())
f.close()

print("Last known number of emails is " + str(last_mails))


if  cur_mails < last_mails:
    last_mails = cur_mails
    f = open('emails.txt', 'w')
    f.write(str(last_mails))

if  cur_mails > last_mails:
    last_mails = cur_mails
    f = open('emails.txt', 'w')
    f.write(str(last_mails))

    GPIO.output(7, True) #flash the leds a couple times
    time.sleep(0.4) #in seconds
    GPIO.output(7, False)
    time.sleep(0.1)
    GPIO.output(7, True)
    time.sleep(0.4)
    GPIO.output(7, False)
    time.sleep(0.4)
    GPIO.output(7, True)
    time.sleep(0.4)
    GPIO.output(7, False)
    time.sleep(0.4)
    GPIO.output(7, True)
    time.sleep(0.4)
    GPIO.output(7, False)

if cur_mails != 0:
    GPIO.output(7, True)

if cur_mails == 0:
    GPIO.output(7, False)


f.close()
