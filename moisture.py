#!/usr/bin/python

# Start by importing the libraries we want to use

import RPi.GPIO as GPIO # This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import urllib2 # To send GET request
import datetime

# Define some variables to be used later on in our script

webhook_url = "https://api.thingspeak.com/update?api_key=3YJ24WQGWH6XG358"

# This is our submitValue function

def submitValue(value):
    try:
        response = urllib2.urlopen(webhook_url + "&field1=" + str(value))
        print "Successfully submitted value. Response:", response.read() 
    except urllib2.URLError:
        print "Error: unable to submit value: " + webhook_url + "&field1=" + str(value)

# This is our callback function, this function will be called every time there is a change on the specified GPIO channel, in this example we are using 17

def callback(channel):  
	if GPIO.input(channel):
		print "LED off"
		submitValue(1)
	else:
		print "LED on"
		submitValue(0)

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that we have our digital output from our sensor connected to
channel = 17
# Set the GPIO pin to an input
GPIO.setup(channel, GPIO.IN)

print datetime.datetime.now()
callback(channel)
