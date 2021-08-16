# 📖 TP 1 - Agentes Racionales

## 📢 Statement 
Se deberán crear 3 programas donde cada uno simule un agente, se debe tener en
cuenta que:
+ El tamaño inicial del suelo es aleatorio.
+ Tipo de suciedad en el piso aleatoria (limpio, poco sucio, sucio, permanente).
+ Posición de la aspiradora aleatoria.

Además cada uno de los programas debera mostrar:
+ El estado inicial de piso para cada movimiento.
+ Las acciones que realiza la aspiradora.
+ La cantidad de movimientos totales (mover, cambiar dirección, aspirar)
### 📦 Programs 

|   | Cant. Baldosas  | Historial de posiciones | Cant. limpiezas sobre baldozas | Ubicación dentro del piso | Tipos de manchas | Terminar Programa | Objetivo |
| --- | --- | --- |---| --- | --- | --- | --- |
| Reactivo Simple | NO | NO | NO | NO | SI | ? | NO |
| Basado en modelo | SI | SI | SI | SI | SI | No quedan baldosas que puedan ser limpiadas | NO |
| Basado en objetivos | SI | SI | SI | SI | SI | No quedan baldosas que puedan ser limpiadas | Limpiar las baldosas en la menor cantidad posible de movimientos|

## ⚙️ Usage

Para lanzar alguna de las aspiradoras, se debe ejecutar con python alguno
de los archivos `first_agent.py`, `second_agent.py`, `third_agent.py` o `fourth_agent.py`

El tamaño del piso se definirá de manera aleatoria, siendo 5 el minimo y 30 el máximo. Si se deseara,
se puede especificar un tamaño a la hora de lanzar cualquiera de las aspiradoras, utilizando la opcion
de lanzamiento `-f` o `--floor-size`, con su respectivo valor.

Las aspiradoras comenzarán a moverse y/o limpiar cada 1 segundo, logueando información relevante en cada paso,
lo que permitirá seguir y entender su comportamiento. Si se deseara, se puede cambiar el comportamiento
para mover la aspiradora de manera manual, teniendo que apretar Enter para hacer cada movimiento.
Este modo lento o manual puede ser util si queremos seguir sus pasos mas detenidamente. Para lanzar una aspiradora
de manera manual, se debe utilizar la opción de lanzamiento `-m` o `--manual`

