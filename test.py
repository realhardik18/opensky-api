from opensky_api import OpenSkyApi
import random

api = OpenSkyApi()
states = api.get_states()
print(states.states[random.randint(0, len(states.states))])
