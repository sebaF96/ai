from .VacuumBase import VacuumBase
from time import sleep


class SimpleVacuum(VacuumBase):

    def start(self):
        while True:
            sleep(1)
            self.move()
