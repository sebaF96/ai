from .ObectiveBasedVacuum import ObjectiveBasedVacuum
from tools import mess_cell_if_unlucky


class RandomVacuum(ObjectiveBasedVacuum):
    def __init__(self, floor: list, starting_position: int, manual_steps: bool = False):
        super().__init__(floor, starting_position, manual_steps)
        self.set_starting_direction(self.starting_position, len(self.floor))
        self.__absolute_mess = set()
        self.__current_cleans = 0

    def log(self):
        last_operation = self.last_movement if self.last_movement != "Clear" else f"Clear index {self.current_position}"
        print(f"\nMovements: {self.movements}")
        print(f"Last operation: {last_operation}")
        print(f"Current position: {self.current_position}")
        print(f"Known permanent marks: {sorted(list(self.__absolute_mess))}")
        print("Floor status:")
        print(self.floor)

    def start(self):
        while True:
            self.wait_between_steps()
            mess_cell_if_unlucky(self.floor, self.current_position)
            self.move()

    def should_clean(self) -> bool:
        if self.__current_cleans == 3:
            self.__absolute_mess.add(self.current_position)
            self.__current_cleans = 0
            return False
        elif self.is_dirty(self.floor[self.current_position]) and self.current_position not in self.__absolute_mess:
            self.__current_cleans += 1
            return True
        self.__current_cleans = 0
        return False
