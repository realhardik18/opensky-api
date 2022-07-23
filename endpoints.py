from opensky_api import OpenSkyApi
import random
api = OpenSkyApi()

states = api.get_states()
'''
flight_choosen = states.states[random.randint(0, len(states.states))]
flight_choosen_str = str(flight_choosen)
'''
print(states.states[0])
