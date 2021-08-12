from .ObectiveBasedVacuum import ObjectiveBasedVacuum
from time import sleep
from tools import mess_cell_if_unlucky


class RandomVacuum(ObjectiveBasedVacuum):
    def __init__(self, floor: list, starting_position: int):
        super().__init__(floor, starting_position)
        self.set_starting_direction(self.starting_position, len(self.floor))
        self.__absolute_mess = set()
        self.__current_cleans = 0

    def set_starting_direction(self, position, size):
        self.direction = "left" if abs(size - position) > abs(0 - position) else "right"

    def start(self):
        while True:
            mess_cell_if_unlucky(self.floor, self.current_position)
            sleep(0.5)
            self.move()

    def should_clean(self) -> bool:
        if self.__current_cleans == 3:
            self.__absolute_mess.add(self.current_position)
            self.__current_cleans = 0
            return False

        elif self.current_position in self.__absolute_mess:
            return False

        elif self.is_dirty(self.floor[self.current_position]):
            self.__current_cleans += 1
            return True
        else:
            return False
