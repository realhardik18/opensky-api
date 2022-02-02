from opensky_api import OpenSkyApi
import random


def info():
    api = OpenSkyApi()
    states = api.get_states()
    flight_choosen = states.states[random.randint(0, len(states.states))]
    return type(flight_choosen)


print(info())
