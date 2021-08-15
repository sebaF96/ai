# TP 1


## Usage

Para lanzar alguna de las aspiradoras, se debe ejecutar con python alguno
de los archivos `first_agent.py`, `second_agent.py`, `third_agent.py` o `fourth_agent.py`

El tamaño del piso se definirá de manera aleatoria, siendo 5 el minimo y 30 el máximo. Si se deseara,
se puede especificar un tamaño a la hora de lanzar cualquiera de las aspiradoras, utilizando la opcion
de lanzamiento `-f` o `--floor-size`, con su respectivo valor.

Las aspiradoras comenzarán a moverse y/o limpiar cada 1 segundo, logueando información relevante en cada paso,
lo que permitirá seguir y entender su comportamiento. Si se deseara, se puede cambiar el comportamiento
para mover la aspiradora de manera manual, teniendo que apretar Enter para hacer cada movimiento.
Este modo lento o manual puede ser util si queremos seguir sus pasos mas detenidamente. Para lanzar una aspiradora
de manera manual, se debe utilizar la opcion de lanzamiento `-m` o `--manual`

