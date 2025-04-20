import board
import digitalio
import time
import requests

# Set up C0 as an output
c0 = digitalio.DigitalInOut(board.C0)
c0.direction = digitalio.Direction.OUTPUT
c0.value = True  # Sending voltage signal

# Set up C1 as an input
c1 = digitalio.DigitalInOut(board.C1)
c1.direction = digitalio.Direction.INPUT

relay1_state = False

# Infinite loop
while True:
    if c1.value:  # If C1 reads HIGH
        if not relay1_state:
            print("Turning relay 1 off")
            requests.get("http://192.168.1.4/30000/00")  # Turn relay 1 off
            relay1_state = True
        print("1", end="", flush=True)
    else: 
        if relay1_state:
            print("Turning relay 1 on")
            requests.get("http://192.168.1.4/30000/01")  # Turn relay 1 on
            relay1_state = False
        print("0", end="", flush=True)
    time.sleep(0.1)  # Sleep for 1/10th of a second
