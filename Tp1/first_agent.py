from tools import get_random_floor, get_starting_position
from time import sleep


def log(last_operation, current_position, floor_status, movements):
    if last_operation == "Clear":
        last_operation = f"Clear index {current_position}"
    print(f"\nMovements: {movements}")
    print(f"Last operation: {last_operation}")
    print(f"Current position: {current_position}")
    print(f"Floor status:")
    print(floor_status)


def is_dirty(value):
    return value in ["#", "+", "x"]


def clear(floor: list, position: int):
    if floor[position] == "#":
        return
    elif floor[position] == "x":
        floor[position] = "+"
    else:
        floor[position] = ""


def start(floor):
    position = get_starting_position(len(floor))
    direction = "right"
    last_movement = "Move right"
    movements = 0
    print(f"Starting index: {position}")
    print("Starting floor:")
    print(floor)
    while True:
        input()
        movements += 1
        if is_dirty(floor[position]) and last_movement != "Clear":
            clear(floor, position)
            last_movement = f"Clear"
        elif position != 0 and direction == "left":
            last_movement = "Move left"
            position -= 1
        elif position + 1 <= len(floor) - 1 and direction == "right":
            last_movement = "Move right"
            position += 1
        elif position + 1 == len(floor):
            direction = "left"
            last_movement = "Move left"
            position -= 1
        elif position == 0 and direction == "left":
            direction = "right"
            last_movement = "Move right"
            position += 1
        log(last_movement, position, floor, movements)


def main():
    floor = get_random_floor()
    start(floor)


if __name__ == '__main__':
    main()
