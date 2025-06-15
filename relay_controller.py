import requests

class RelayController():
    BASE_URL = "http://192.168.1.4/30000/"

    # will be only using the first 6 relays
    # all on "45" and all off "44" feature will not be used
    # last two relays can be used for something else.
    RELAY_CONTROLS = { 
        0: {
            "on": "01",
            "off": "00"
        }, 
        1: {
            "on": "03",
            "off": "02"
        },
        2: {
            "on": "05",
            "off": "04"
        },
        3: {
            "on": "07",
            "off": "06"
        },
        4: {
            "on": "09",
            "off": "08"
        },
        5: {
            "on": "11",
            "off": "10"
        }
    }
    # common kwargs
    kwargs = {
        "timeout": 10,
        "verify": False  # Disable SSL verification if needed
    }
    def turn_on_relay(self, relay):
        url = self.BASE_URL + self.RELAY_CONTROLS[relay]["on"]
        try:
            requests.get(url, **self.kwargs)
        except Exception as e:
            print(f"Error turning on relay {relay}: {e}")
    
    def turn_off_relay(self, relay):
        url = self.BASE_URL + self.RELAY_CONTROLS[relay]["off"]
        try:
            requests.get(url, **self.kwargs)
        except Exception as e:
            print(f"Error turning off relay {relay}: {e}")



