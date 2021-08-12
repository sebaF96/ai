from classes.RandomVacuum import RandomVacuum
from tools import get_random_floor, get_starting_position

if __name__ == '__main__':
    floor = get_random_floor()
    random_position = get_starting_position(len(floor))
    vacuum = RandomVacuum(floor, random_position)
    vacuum.start()
