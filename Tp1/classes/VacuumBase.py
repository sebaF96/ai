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
        last_operation = self.last_movement if self.last_movement != "Clear" else f"Clear index {self.current_position}"
        print(f"\nMovements: {self.movements}")
        print(f"Last operation: {last_operation}")
        print(f"Current position: {self.current_position}")
        print(f"Floor status:")
        print(self.floor)

    def move(self):
        if self.is_dirty(self.floor[self.current_position]) and self.last_movement != "Clear":
            # Position dirty and didn't clean in last movement
            self.clear_current_position()
            self.last_movement = f"Clear"
        elif self.current_position != 0 and self.direction == "left":
            # Moving left and can keep moving
            self.last_movement = "Move left"
            self.current_position -= 1
        elif self.current_position + 1 <= len(self.floor) - 1 and self.direction == "right":
            # Moving right and can keep moving
            self.last_movement = "Move right"
            self.current_position += 1
        elif self.current_position + 1 == len(self.floor):
            # Moving right and reach last index
            self.direction = "left"
            self.last_movement = "Move left"
            self.current_position -= 1
        elif self.current_position == 0 and self.direction == "left":
            # Moving left and reach index 0
            self.direction = "right"
            self.last_movement = "Move right"
            self.current_position += 1
        self.__movements += 1
        self.log()

    def clear_current_position(self):
        if self.floor[self.current_position] == "#":
            return
        elif self.floor[self.current_position] == "x":
            self.floor[self.current_position] = "+"
        else:
            self.floor[self.current_position] = ""

    def is_dirty(self, cell_value):
        return cell_value in ["#", "+", "x"]

    @property
    def floor(self):
        return self.__floor

    @property
    def starting_position(self):
        return self.__starting_position

    @property
    def last_movement(self):
        return self.__last_movement

    @last_movement.setter
    def last_movement(self, value):
        self.__last_movement = value

    @property
    def current_position(self):
        return self.__current_position

    @current_position.setter
    def current_position(self, value):
        self.__current_position = value

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value):
        self.__direction = value

    @property
    def movements(self):
        return self.__movements
