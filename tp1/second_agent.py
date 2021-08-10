from tools import get_random_floor, get_starting_position
from classes import ModelBasedVacuum

if __name__ == '__main__':
    floor = get_random_floor()
    random_position = get_starting_position(len(floor))
    vacuum = ModelBasedVacuum(floor, random_position)
    vacuum.start()
