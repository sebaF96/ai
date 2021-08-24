# Inteligencia Artificial 

![flake workflow](https://github.com/sebaF96/ai/actions/workflows/flake8.yml/badge.svg)


Repositorio de la cátedra Inteligencia Artificial, Universidad de Mendoza, 2021


### Correr flake8 localmente

#### Install

1. Instalar flake8_nb en entorno de conda

`conda activate && pip install flake8-nb`

2. Agregar alias

`echo "alias flake='flake8_nb --count --filename \"*.ipynb\" --ignore E121,E501,F821' >> ~/.bash_aliases && source ~/.bash_aliases`

#### Correr

Hacer cd al repo, activar conda, y ejecutar `flake`

