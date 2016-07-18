import time
import RPi.GPIO as GPIO
import os
import json
from pprint import pprint

# set the relay to true because the garage door circuit is normally open, the
# relay needs to be normally closed on the side of the raspberryPi
relay = True

# database to enter in all of the possible plates to check for a match against the candidate
platesDatabase = {"2PZ6", "2P28864", "2P26", "2P864", "2P28", "P28864", "2P2886", "15J8514", "2L3009", "2L30090", "2L3009I", "2L3009Q", "BDZ88", "BDZ886", "8BDZ886", "6MBV006"}

# setup GPIO for the Motion Sensor
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN)

# setup GPIO for the Relay
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, True)

# delay for about a minute for motion sensor initialization
# this avoids any false signals that would trigger the garage door prematurely
time.sleep(60)

# infinate loop polling the motion sensor
while True:
    # check for motion
    if GPIO.input(18) == True:
        # if there is motion, take a picture using this script
        os.system("/home/pi/webcam/webcam.sh")
        time.sleep(1)
        # save the candidate with the greatest confidence interval
        with open('/home/pi/webcam/results.json') as results:
            candidates = json.load(results)
        # compare the candidate to the database of possible plates
        for x in platesDatabase:
            # check the length of candidates, if there are no results, deny access
            if len(candidates['results']) != 0:
                # if there is a result and it matches a possible plate, grant access
                if x == candidates['results'][0]['plate']:
                    pprint("Access Granted!")
                    # set the relay to false to complete the garage door circuit
                    if relay:
                        relay = False
            else:
                pprint("Access Denied")
        # for testing purposes, this if statement displays the candidate that was processed by openALPR
        if len(candidates['results']) != 0:
            pprint(candidates['results'][0]['plate'])
        # since the garage door is normally an open circuit, when the variable relay is false it opens the
        # circuit connecting the raspberryPi and closes the garage door circuit. If "relay" is true there
        # was not a match between the candidate and the database
        if not relay:
            # this actually triggers the relay to open the garage door
            GPIO.output(17, False)
            time.sleep(1)
            GPIO.output(17, True)
            pprint("wait for open")
            # reset the relay to leave the garage door circuit open
            relay = True
            # this delay is needed so the relay won't be triggered while the garage door is opening
            # we also included a 17 second delay to automatically close the garage door after 30 seconds
            time.sleep(30)
            # trigger the close
            GPIO.output(17, False)
            time.sleep(1)
            GPIO.output(17, True)
            # delay while the garage door opens
            time.sleep(13)
