from tools import get_random_floor, get_starting_position
from time import sleep


def log(last_operation, current_position, floor_status):
    if last_operation == "Clear":
        last_operation = f"Clear index {current_position}"
    print(f"\nLast operation: {last_operation}")
    print(f"Current position: {current_position}")
    print(f"Floor status:")
    print(floor_status)


def is_dirty(value):
    return value in ["#", "+", "x"]


def clear(floor: list, position: int):
    floor[position] = ""


def start(floor):
    position = get_starting_position(len(floor))
    last_movement = "Move right"
    print(f"Starting index: {position}")
    print("Starting floor:")
    print(floor)
    while True:
        sleep(2)
        if is_dirty(floor[position]):
            clear(floor, position)
            last_movement = f"Clear"
        elif position != 0 and last_movement in ("Move left", "Clear") or position == len(floor) - 1:
            last_movement = "Move left"
            position -= 1
        elif position + 1 <= len(floor) - 1:
            last_movement = "Move right"
            position += 1
        else:
            break
        log(last_movement, position, floor)


def main():
    floor = get_random_floor()
    start(floor)


if __name__ == '__main__':
    main()
