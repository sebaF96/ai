from tools import get_random_floor, get_starting_position, is_dirty, clear, log


def start():
    floor = get_random_floor()
    position = get_starting_position(len(floor))
    direction = "right"
    last_movement = "Move right"
    movements = 0
    cleaned_pos = set()
    print(f"Starting index: {position}")
    print("Starting floor:")
    print(floor)
    while len(floor) > len(cleaned_pos):
        input()
        if (floor[position] in ("", "#")):
            cleaned_pos.add(position)
        movements += 1

        if is_dirty(floor[position]) and last_movement != "Clear":
            # Position dirty and didn't clean in last movement
            clear(floor, position)
            last_movement = f"Clear"
        elif position != 0 and direction == "left":
            # Moving left and can keep moving
            last_movement = "Move left"
            position -= 1
        elif position + 1 <= len(floor) - 1 and direction == "right":
            # Moving right and can keep moving
            last_movement = "Move right"
            position += 1
        elif position + 1 == len(floor):
            # Moving right and reach last index
            direction = "left"
            last_movement = "Move left"
            position -= 1
        elif position == 0 and direction == "left":
            # Moving left and reach index 0
            direction = "right"
            last_movement = "Move right"
            position += 1
        log(last_movement, position, floor, movements)

    print("All cleaned!")

if __name__ == '__main__':
    start()
