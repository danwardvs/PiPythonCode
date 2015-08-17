#!/usr/bin/python

# googletts
# Created by Matt Dyson (mattdyson.org)
# http://mattdyson.org/blog/2014/07/text-to-speech-on-a-raspberry-pi-using-google-translate/
# Some inspiration taken from http://danfountain.com/2013/03/raspberry-pi-text-to-speech/

# Version 1.0 (12/07/14)

# Process some text input from our arguments, and then pass them to the Google translate engine
# for Text-To-Speech translation in nicely formatted chunks (the API cannot handle more than 100
# characters at a time).
# Splitting is done first by any punctuation (.,;:) and then by splitting by the MAX_LEN defined
# below.
# mpg123 is required for playing the resultant MP3 file that is returned by Google TTS
from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)



from subprocess import call
import sys
import re

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        sensor = W1ThermSensor()

        temperature_in_celsius = sensor.get_temperature()
        MAX_LEN = 100 # Maximum length of a segment to send to Google for TTS
        LANGUAGE = "en" # Language to use with TTS - this won't do any translation, just the voice it's spoken with

        print(temperature_in_celsius)
        
        fullMsg = str(temperature_in_celsius) +"degrees celsius"
        i = 1

        # Read our system arguments and add them into a single string
        while i<len(sys.argv):
           fullMsg += sys.argv[i] + " "
           i+=1

        # Split our full text by any available punctuation
        parts = re.split("[\,\;\:]", fullMsg)

        # The final list of parts to send to Google TTS
        processedParts = []

        while len(parts)>0: # While we have parts to process
           part = parts.pop(0) # Get first entry from our list

           if len(part)>MAX_LEN:
              # We need to do some cutting
              cutAt = part.rfind(" ",0,MAX_LEN) # Find the last space within the bounds of our MAX_LEN

              cut = part[:cutAt]

              # We need to process the remainder of this part next
              # Reverse our queue, add our remainder to the end, then reverse again
              parts.reverse()
              parts.append(part[cutAt:])
              parts.reverse()
           else:
              # No cutting needed
              cut = part

           cut = cut.strip() # Strip any whitespace
           if cut is not "": # Make sure there's something left to read
              # Add into our final list
              processedParts.append(cut.strip())

        for part in processedParts:
           # Use mpg123 to play the resultant MP3 file from Google TTS
           call(["mpg123","-q","http://translate.google.com/translate_tts?tl=%s&q=%s" % (LANGUAGE,part)])



