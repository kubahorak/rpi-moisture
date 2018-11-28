#!/usr/bin/python

# Start by importing the libraries we want to use

import RPi.GPIO as GPIO # This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import urllib2 # To send GET request
import time
import datetime

# This is our submitValue function

def submitValue(name, base_url, value):
    try:
        url = base_url + "&field1=" + str(value)
        response = urllib2.urlopen(url)
        print "{}: Successfully submitted value. Response: {}".format(name, response.read())
    except urllib2.URLError as e:
        print "{}: Error: unable to submit value to URL: {}, {}".format(name, url, e)

# This is our check function, this function will be called to check the specific channel

def check(name, channel, url):
    print datetime.datetime.now()
    if GPIO.input(channel):
        print "{}: LED off".format(name)
        submitValue(name, url, 1)
        pumpWater(name)
    else:
        print "{}: LED on".format(name)
        submitValue(name, url, 0)

# This is our watering function, it triggers the pump

def pumpWater(name):
    (channel, durationSeconds) = pumps[name]
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(durationSeconds)
    GPIO.output(channel, GPIO.HIGH)
    print "{}: watered for {} seconds".format(name, delay)


# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that we have our digital output from our sensor connected to
# and URL which to call on sensor state change
sensors = {
        "peace_lily": (17, "https://api.thingspeak.com/update?api_key=3YJ24WQGWH6XG358"),
        "parsley": (23, "https://api.thingspeak.com/update?api_key=CYABHN6FCS9JL5YH")
        }

# Define the GPIO pin that we have our digital input to the respective relay connected to
# and number of seconds to pump each time
pumps = {
        "parsley": (27, 1)
        }

for name, (channel, url) in sensors.iteritems():
    # Set the GPIO pin to an input
    GPIO.setup(channel, GPIO.IN)

    check(name, channel, url)
