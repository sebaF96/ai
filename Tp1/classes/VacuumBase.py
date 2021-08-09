from abc import abstractmethod


class VacuumBase:
    def __init__(self, floor: list, starting_position: int):
        self.__floor = floor
        self.__starting_position = starting_position
        self.__current_position = starting_position
        self.__movements = 0
        self.__last_movement = "Move Right"
        self.__direction = "right"
        print(f"Starting index: {self.__starting_position}")
        print("Starting floor:")
        print(self.__floor)

    @abstractmethod
    def start(self):
        raise Exception("Method start not implemented")

    def log(self):
        last_operation = self.__last_movement if self.__last_movement != "Clear" else f"Clear index {self.__current_position}"
        print(f"\nMovements: {self.__movements}")
        print(f"Last operation: {last_operation}")
        print(f"Current position: {self.__current_position}")
        print(f"Floor status:")
        print(self.__floor)

    def move(self):
        if self.is_dirty(self.__floor[self.__current_position]) and self.__last_movement != "Clear":
            # Position dirty and didn't clean in last movement
            self.clear_current_position()
            self.__last_movement = f"Clear"
        elif self.__current_position != 0 and self.__direction == "left":
            # Moving left and can keep moving
            self.__last_movement = "Move left"
            self.__current_position -= 1
        elif self.__current_position + 1 <= len(self.__floor) - 1 and self.__direction == "right":
            # Moving right and can keep moving
            self.__last_movement = "Move right"
            self.__current_position += 1
        elif self.__current_position + 1 == len(self.__floor):
            # Moving right and reach last index
            self.__direction = "left"
            self.__last_movement = "Move left"
            self.__current_position -= 1
        elif self.__current_position == 0 and self.__direction == "left":
            # Moving left and reach index 0
            self.__direction = "right"
            self.__last_movement = "Move right"
            self.__current_position += 1
        self.__movements += 1
        self.log()


    def clear_current_position(self):
        if self.__floor[self.__current_position] == "#":
            return
        elif self.__floor[self.__current_position] == "x":
            self.__floor[self.__current_position] = "+"
        else:
            self.__floor[self.__current_position] = ""

    def is_dirty(self, cell_value):
        return cell_value in ["#", "+", "x"]

