from .VacuumBase import VacuumBase


class SimpleVacuum(VacuumBase):

    def start(self):
        while True:
            self.wait_between_steps()
            self.move()
