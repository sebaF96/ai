from envirom import Enviroment
from tools import *


def first_agent(enviroment, generated_list):
    index = enviroment.starting
    clear = ["#", "+", "x"]
    print(f"Indicie {index}")

    for index, value in enumerate(generated_list):
        if value in clear:
           print("hola")

        print(index, value)






if __name__ == '__main__':
    enviroment = Enviroment()
    enviroment.floor_size = set_random_size()
    enviroment.starting = set_random_starting(enviroment.floor_size)
    generated_list = generate_secuence(enviroment.floor_size)
    enviroment.direction = "right"
    print(f"Mi tamaño es {enviroment.floor_size} empiezo en  {enviroment.starting} Estado: {generated_list[enviroment.starting]}")
    print(generated_list)

    first_agent(enviroment, generated_list)











