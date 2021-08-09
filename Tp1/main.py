from envirom import Enviroment
from tools import *


def first_agent(enviroment, generated_list):
    clear = ["#", "+", "x"]
    cleaned = [" "]
    for k, v in enumerate(generated_list):
        if v == generated_list[enviroment.starting]:
            if v in clear:
                print("Valor: ", v)

    # while True:
    #     if generated_list[index] in clear:
    #         generated_list[index] = " "
    #
    #     try:
    #         if enviroment.direction == "right":
    #             move = 1
    #         else:
    #             move = -1
    #         index = [enviroment.starting + move]
    #
    #         if (enviroment.starting + move) < 0:
    #             raise
    #         print("Moving to " + enviroment.direction)
    #         enviroment.movements += 1
    #         enviroment.starting = enviroment.starting + move
    #     except:
    #         if enviroment.direction == "right":
    #             enviroment.direction = "left"
    #         else:
    #             enviroment.direction = "right"
    #         print("Moving to: " + enviroment.direction)



if __name__ == '__main__':
    enviroment = Enviroment()
    enviroment.floor_size = set_random_size()
    enviroment.starting = set_random_starting(enviroment.floor_size)
    generated_list = generate_secuence(enviroment.floor_size).copy()
    enviroment.direction = choose_dir()
    print(f"Mi tamaño es {enviroment.floor_size} empiezo en  {enviroment.starting} Estado: {generated_list[enviroment.starting]} moviendo {enviroment.direction}")
    print(generated_list)

    first_agent(enviroment, generated_list)











