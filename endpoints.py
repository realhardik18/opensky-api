from opensky_api import OpenSkyApi
import random
import ast

api = OpenSkyApi()
states = api.get_states()


def available_states():
    return len(states.states)


def info():
    flight_choosen = states.states[random.randint(0, len(states.states))]
    flight_choosen_str = str(flight_choosen)
    result = ast.literal_eval(flight_choosen_str)
    return result


def test():
    return 'hello'

# print(available_states())
