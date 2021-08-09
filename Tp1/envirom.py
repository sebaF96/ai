class Enviroment:
    def __init__(self, floor_size = 1,  starting = 1, movements = 0, direction = 0):
        self.__floor_size = floor_size
        self.__starting = starting
        self.__movements = movements
        self.__direction = direction

@property
def floor_size(self):
    return self.__floor_size

@property
def starting(self):
    return self.__starting

@property
def movements(self):
    return self.__movements

@property
def direction(self):
    return self.__direction

@floor_size.setter
def floor_size(self, value):
    self.__floor_size = value

@starting.setter
def starting(self, value):
    self.__starting = value

@movements.setter
def movements(self,value):
    self.__movements = value

@direction.setter
def direction(self,value):
    self.__movements = value