from .VacuumBase import VacuumBase
from time import sleep


class ModelBasedVacuum(VacuumBase):
    def __init__(self, floor: list, starting_position: int):
        super().__init__(floor, starting_position)
        self.__cleaned_positions = set()

    def start(self):
        while len(self.floor) > len(self.__cleaned_positions):
            if self.floor[self.current_position] in ("", "#"):
                # Nothing else to do here, we add the index to cleaned_positions
                self.__cleaned_positions.add(self.current_position)
            sleep(0.13)
            self.move()
        print(f"Finished in {self.movements} movements")
