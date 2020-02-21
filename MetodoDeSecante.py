from builtins import input, print

import numpy as np
import matplotlib.pyplot as plt
from sympy import *


def numpyf(m):
    x, y, z = symbols("x y z")
    expr = sympify(str_ecuacion)
    reemplaza = lambdify(x, expr, "numpy")
    return reemplaza(m)

def ecuacion(str_ecuacion):
    expr = sympify(str_ecuacion)    #Simplifica la ecuacion, debe hacerse para que sympy reconozca el String como ecuacion
    return expr  #Retorna la ecuacion simplificada

def f(Xo):
        expr= ecuacion(str_ecuacion)
        b = expr.free_symbols  # recibe una ecuacion tipo string
        var = b.pop()
        reemplaza = expr.evalf(subs = {var: Xo})    #Sustituye las x de la ecuacion por xo
        return reemplaza


def grafica():
    x = np.linspace(-5,4, 100)  # linspace(inicio de la grafica, fin de la grafica, numero de muestras:cambia la forma grafica)
    plt.plot(x, numpyf(x))
    plt.grid()
    plt.show()


def comprobacion():
    print("De acuerdo a la grafica digite los puntos X0 y X1")
    a = float(input("X0: "))      # Xn-2
    b = float(input("X1: "))      # Xn-1
    errorTolerable = float(input("Escriba el error de tolerancia: "))
    # Define el orden de los puntos asignando a X0 el menor y a X1 el mayor
    if a < b:
        x0 = a
        x1 = b
    else:
        x0 = a
        x1 = b
    error = 1
    i = 0
    while error > errorTolerable and i <= 100:       #parará cuando el error sea menor al tolerable
         i += 1
         print("iteracion ", i)
         fx1 = f(x1)  # Evalúa la función con el valor de a
         fx0 = f(x0)  # Evalúa la función con el valor de r
         x2 = x1- ((x1 - x0)*fx1 / (fx1 - fx0))     #Ecuacion del método de la secante
         error = abs((x2 - x1) / x2)        #v.absoulto de(actual-anterior)/actual
         x0=x1
         x1=x2
         print("r= ", x2)
         print("error relativo", error)
         print("---------------------------------------")
    if i < 100:
         print("Raiz final mas aproximada ", x2,"\n",
         "Total de Iteraciones: ", i, "\n" ,
         "Error relativo: ", error)
    else:
         print("No se encontró en el instervalo definido la raiz de la función en 100 iteraciones")



str_ecuacion = str(input("Ingrese la ecuacion"))
grafica()
comprobacion()

