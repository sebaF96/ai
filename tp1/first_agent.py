from classes.SimpleVacuum import SimpleVacuum
from tools import get_random_floor, get_starting_position
from command_argumentor import get_startup_arguments

if __name__ == '__main__':
    manual_steps, floor_size = get_startup_arguments()
    floor = get_random_floor(floor_size)
    random_position = get_starting_position(len(floor))
    vacuum = SimpleVacuum(floor, random_position, manual_steps)
    vacuum.start()
