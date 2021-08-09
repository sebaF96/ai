import random


def set_random_size():
    return random.randint(5, 30)

def set_random_starting(size):
    return random.randint(0, size - 1)

def generate_secuence(size):
    choices = [" ", "#", "+", "x"]
    return [random.choices(choices) for x in range(size)]

def change_dir(direction):
    if direction == 1:
        direction = -1
    else:
        direction = 1
    return direction




