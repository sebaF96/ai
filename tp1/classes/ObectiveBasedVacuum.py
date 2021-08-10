from .ModelBasedVacuum import ModelBasedVacuum


class ObjectiveBasedVacuum(ModelBasedVacuum):
    def __init__(self, floor: list, starting_position: int):
        super().__init__(floor, starting_position)
        self.set_starting_direction(self.starting_position, len(self.floor))

    def set_starting_direction(self, position, size):
        self.direction = "left" if abs(size - position) > abs(0 - position) else "right"
