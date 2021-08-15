from tools import get_random_floor, get_starting_position
from classes import ObjectiveBasedVacuum
from command_argumentor import get_startup_arguments

if __name__ == '__main__':
    manual_steps, floor_size = get_startup_arguments()
    floor = get_random_floor(floor_size)
    random_position = get_starting_position(len(floor))
    vacuum = ObjectiveBasedVacuum(floor, random_position, manual_steps)
    vacuum.start()
