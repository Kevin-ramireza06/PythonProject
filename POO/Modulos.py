import random, sys, tkinter
#Podemos importar varios ficheros, solamente separandolos por comas

from random import shuffle,randint,  choice, sample
#De esta forma solo importamos una o varias funcion de una libreria o fichero

import math as mates
#DE esta forma le ponemos un alias para usarlos en nuestro fichero a una libreria
from  random import randint as azar #del mismo modo con funciones concretas

print(randint(3,5))
#Actualmente solo hemos importado las librerias, pero en realidad debemos de importarlas con la extencion .py

print(azar(3,8))

print(mates.pi)

"""
Modulos interesantes:

administracion de sistemas:
    sys
    os
    shutil
    subprocess
    platfrom
    
DAM,DAW:
    pandas
    pynum
    pyspark
    powerbi
    
Entornos graficos:
    tkinter
"""

