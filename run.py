import board
import digitalio
import time
import requests

# Set up C0 as an output
# c0 = digitalio.DigitalInOut(board.C0)
# c0.direction = digitalio.Direction.OUTPUT
# c0.value = True  # Sending voltage signal

# # Set up C1 as an input
# c1 = digitalio.DigitalInOut(board.C1)
# c1.direction = digitalio.Direction.INPUT

relay1_state = False
sensors = [
    digitalio.DigitalInOut(board.C0), 
    digitalio.DigitalInOut(board.C1),
    #digitalio.DigitalInOut(board.C2),
    digitalio.DigitalInOut(board.C3),
    digitalio.DigitalInOut(board.C4),
    #digitalio.DigitalInOut(board.C5)
]

SENSOR_COUNT = len(sensors)
for i, v in enumerate(sensors):
    sensors[i].direction = digitalio.Direction.OUTPUT
    sensors[i].value = True
relay_states = [False for i in range(0, SENSOR_COUNT)]
sensor_states = [0 for i in range(0,SENSOR_COUNT)]
queue = []

prev_sensor_state_id = ""
def print_relays():
    global prev_sensor_state_id
    sensor_state_id = "s" + "".join(list(map(lambda x: str(int(sensors[x[0]].value)), enumerate(sensors))))
    print("--" + sensor_state_id)
    for i in sensors: 
        print(int(i.value))
    if sensor_state_id == prev_sensor_state_id:
        return
    prev_sensor_state_id = sensor_state_id
    print("-------")
    print(sensor_state_id)
    
    print("-------")
    print("r", end="")
    for v in relay_states:
        print(int(v), end="")
    print("")

# Infinite loop
while True:
    time.sleep(1)  # Sleep for 1/10th of a second
    print_relays()



    # if sensors[0].value and relay_states[0]:
    #     #requests.get("http://192.168.1.4/30000/00")  # Turn relay 1 off
    #     relay_states[0] = False
    # elif not relay_states[0]:
    #     #requests.get("http://192.168.1.4/30000/01")  # Turn relay 1 on
    #     relay_states[0] = True
    # time.sleep(0.5)  # Sleep for 1/10th of a second
