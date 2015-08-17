import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
import random


##GPIO,setwarning(False)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.setup(22, GPIO.OUT) ## Setup GPIO Pin 22 to OUT

##Define a function named Blink()
def blinkWrong(numTimes,speed):
    for i in range(0,numTimes):## Run loop numTimes
        GPIO.output(7,True)## Switch on pin 75
        time.sleep(speed)## Wait
        GPIO.output(7,False)## Switch off pin 7
        time.sleep(speed)## Wait

def blinkRight(numTimes,speed):
    for i in range(0,numTimes):## Run loop numTimes
       
        GPIO.output(22,True)## Switch on pin 7
        time.sleep(speed)## Wait
        GPIO.output(22,False)## Switch off pin 7
        time.sleep(speed)## Wait
    


def game():
    running = 0
    
    while running == 0:
        number1 = int(random.random()*100)
        number2 = int(random.random()*100)
        result = input("What is " + str(number1) + " + " + str(number2) + "?: " )
        if "exit" in result:
            running = 1
            GPIO.cleanup()
            
        elif int(result) == number1 + number2:
            blinkRight(int(10),float(0.07))

        elif int(result) != number1 + number2:
            blinkWrong(int(10),float(0.07))

        
        


## Ask user for total number of blinks and length of each blink

GPIO.output(22,False)
GPIO.output(7,False)
game()

## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters



    
        
