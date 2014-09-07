#!/bin/sh
echo usb plug add >>/tmp/nickel-hardware-status  # Simulate plugging in the usb
sleep 12 # Wait 12 sec for user to hit connect, and for any processes to run 
echo usb plug remove >>/tmp/nickel-hardware-status # Simulate the disconnect of our simulated usb, takes a few sec after the sleep for the change to show up on the device
# When the kobo detects USB connection, it seems to disable wifi, so only run the update after you are finished with uploading/downloading data