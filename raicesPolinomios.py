from math import *
from sympy import*

def poliRoots(f):
    respuesta=[N(places)for places in solve(f)]

    return respuesta
#"3*x**3+2*x+5"
str_ecuacion = str(input("Ingrese la ecuacion"))
print (poliRoots(sympify(str_ecuacion)))


