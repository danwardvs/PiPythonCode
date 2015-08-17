import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT



##Define a function named Blink()
def toggle_power():
    
    GPIO.output(7,True)## Switch on pin 7
    time.sleep(0.5)
    GPIO.output(7,False)
    print ("Turning off.") ## When loop is complete, print "Done"
    GPIO.cleanup()

def force_power():
    
    GPIO.output(7,True)## Switch on pin 7
    time.sleep(8)
    GPIO.output(7,False)
    print ("Forcing off.") ## When loop is complete, print "Done"
    GPIO.cleanup()

## Ask user for total number of blinks and length of each blink
result = input("Toggle power? (yes/no/force): ")
if "yes" in result or "y" in result:
    toggle_power()

if "force" in result or "f" in result:
    force_power()




    
        
