from .VacuumBase import VacuumBase
from time import sleep


#si limpia una vez y hay suciedad
#vuelve a limpiar, aumenta el contador

#si la psocion tiene mas de 2 limpiezas skipear

#calve pos val cantidad de limpiezas

class ModelBasedVacuum(VacuumBase):
    def __init__(self, floor: list, starting_position: int):
        super().__init__(floor, starting_position)
        self.__cleans = {position: 0 for position in range(len(self.floor))}
        self.__cleaned_positions = set()

    def start(self):
        while len(self.floor) > len(self.__cleaned_positions):
            sleep(0.5)
            self.move()
        print(f"Finished in {self.movements} movements")

    def should_clean(self) -> bool:
        if self.is_dirty(self.floor[self.current_position]) and self.__cleans[self.current_position] < 3:
            self.__cleans[self.current_position] += 1
            return True
        else:
            self.__cleaned_positions.add(self.current_position)
            return False



