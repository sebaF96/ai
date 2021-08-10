import random


def get_random_floor() -> list:
    size = random.randint(5, 30)
    possible_values = ["", "#", "+", "x"]
    return [random.choice(possible_values) for i in range(size)]


def get_starting_position(floor_size) -> int:
    return random.randint(0, floor_size - 1)
