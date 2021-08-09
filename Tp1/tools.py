import random


def set_random_size():
    return random.randint(5, 30)


def set_random_starting(size):
    return random.randint(0, size - 1)


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




