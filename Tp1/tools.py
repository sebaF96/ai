import random


def set_random_size():
    return random.randint(5, 30)


def set_random_starting(size):
    return random.randint(0, size - 1)

def log(last_operation, current_position, floor_status, movements):
    if last_operation == "Clear":
        last_operation = f"Clear index {current_position}"
    print(f"\nMovements: {movements}")
    print(f"Last operation: {last_operation}")
    print(f"Current position: {current_position}")
    print(f"Floor status:")
    print(floor_status)

def generate_secuence(size):
    choices = [" ", "#", "+", "x"]
    generated = []
    for x in range(size):
        generated.append(random.choices(choices))
    return generated


def get_random_floor() -> list:
    size = random.randint(5, 30)
    possible_values = ["", "#", "+", "x"]
    return [random.choice(possible_values) for i in range(size)]


def get_starting_position(floor_size) -> int:
    return random.randint(0, floor_size - 1)


def choose_dir():
    directions = ["right", "left"]
    return random.choices(directions)


def change_dir(direction):
    if direction == 1:
        direction = -1
    else:
        direction = 1
    return direction

def get_direction(position, size):
    if abs(size - position) > abs(0 - position):
        direction = "left"
    else:
        direction = "right"
    return direction


def is_dirty(value):
    return value in ["#", "+", "x"]


def clear(floor: list, position: int):
    if floor[position] == "#":
        return
    elif floor[position] == "x":
        floor[position] = "+"
    else:
        floor[position] = ""


