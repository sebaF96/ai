import random


def get_random_floor() -> list:
    size = random.randint(5, 30)
    possible_values = ["", "#", "+", "x"]
    return [random.choice(possible_values) for i in range(size)]


def get_starting_position(floor_size) -> int:
    return random.randint(0, floor_size - 1)


def mess_cell_if_unlucky(floor: list, secured_pos: int):
    possibilities = [False, False, True]
    should_mess = random.choice(possibilities)
    random_position = random.randint(0, len(floor) - 1)
    if not should_mess or floor[random_position] in ["x", "#"] or random_position == secured_pos:
        return
    elif floor[random_position] == "+":
        floor[random_position] = "x"
    else:
        floor[random_position] = "+"

