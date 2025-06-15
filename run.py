import board
import digitalio
import time
import requests
from sensor_queue import SensorQueue
from relay_controller import RelayController

# TODO: clear all relay states on toggle off switch on box


relay_controller = RelayController()

sensors = [
    digitalio.DigitalInOut(board.C0), 
    digitalio.DigitalInOut(board.C1),
    # bad solder, C2 does not work.
    #digitalio.DigitalInOut(board.C2),
    digitalio.DigitalInOut(board.C3),
    digitalio.DigitalInOut(board.C4),
    #digitalio.DigitalInOut(board.C5)
]

SENSOR_COUNT = len(sensors)
for i, v in enumerate(sensors):
    sensors[i].direction = digitalio.Direction.INPUT
relay_states = [False for i in range(0, SENSOR_COUNT)]
sensor_states = [0 for i in range(0,SENSOR_COUNT)]
queue = SensorQueue()

# print sensor id and relay id only on sensor state change.
# if sensor changes quickly within interval this will not detect the change
prev_sensor_state_id = ""
def print_relays():
    global prev_sensor_state_id
    sensor_state_id = "s" + "".join(list(map(lambda x: str(int(sensors[x[0]].value)), enumerate(sensors))))
    if sensor_state_id == prev_sensor_state_id:
        return
    prev_sensor_state_id = sensor_state_id
    relay_state_id = "r" + "".join(list(map(lambda x: str(int(x)), relay_states)))
    queue_state_id = "q" + "".join(list(map(lambda x: str(x), queue.items)))
    print("-------")
    print(sensor_state_id)
    print(relay_state_id)
    print(queue_state_id)
    print("-------")

# utility func that negates the value. When false its actually at low state
def low(sensor):
    return not sensor.value

# updates queue for empty buckets and removes
# already full buckets.
def update_empty_bucket_queue():
    global queue
    for stall, bucket in enumerate(sensors):
        if low(bucket) and not queue.has(stall):
            print("pushing stall " + str(stall))
            queue.push(stall)
        elif not low(bucket) and queue.has(stall):
            queue.remove(stall)

def turnoff_valve(stall):
    relay_states[stall] = False
    relay_controller.turn_off_relay(stall)

def turnon_valve(stall):
    relay_states[stall] = True
    relay_controller.turn_on_relay(stall)

def turnoff_all_other_valves():
    for stall, valve_is_on in enumerate(relay_states):
        if valve_is_on:
            turnoff_valve(stall)

def valve_is_on(stall):
    return relay_states[stall]


# checks to open next valve. If all buckets full, then do nothing
def check_open_next_valve():
    stall = queue.peek()
    if stall is None:
        turnoff_all_other_valves()
        return
    if not valve_is_on(stall):
        turnoff_all_other_valves()
        turnon_valve(stall)



# Infinite loop
while True:
    time.sleep(1)  # Sleep for 1/10th of a second
    update_empty_bucket_queue()
    check_open_next_valve()
    print_relays()




    # if sensors[0].value and relay_states[0]:
    #     #requests.get("http://192.168.1.4/30000/00")  # Turn relay 1 off
    #     relay_states[0] = False
    # elif not relay_states[0]:
    #     #requests.get("http://192.168.1.4/30000/01")  # Turn relay 1 on
    #     relay_states[0] = True
    # time.sleep(0.5)  # Sleep for 1/10th of a second
