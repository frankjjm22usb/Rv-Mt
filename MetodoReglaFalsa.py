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
    x = np.linspace(-1, 10,  100)  # linspace(inicio de la grafica, fin de la grafica, numero de muestras:cambia la forma grafica)
    plt.plot(x, numpyf(x))
    plt.grid()
    plt.show()


def comprobacion():
    print("De acuerdo a la grafica digite el limite inferior (a) y superior (b)")
    a = float(input("a: "))
    b = float(input("b: "))
    erroTolerable = float(input("Escriba el error de tolerancia: "))
    #Evalua si el intervalo está bien definido
    if a > b:
        raise ValueError("Intervalo mal definido, a debe ser menor que b")
    else:

        if (f(a) * f(b) < 0):
            error = 10
            i = 0
            while error > erroTolerable and i <= 100:       #parará cuando el error sea menor al tolerable
                i += 1
                print("iteracion ", i)
                fa = f(a)  # Evalúa la función con el valor de a
                fb= f(b)
                r = ((a * fb) - (b * fa)) / (fb - fa)
                fr = f(r)       # Evalúa la función con el valor de r
                if f(r) == 0:
                   raiz = r
                if fa * fr < 0:     # Verifica que las funciones cumplan con signos opuestos

                    if i > 1:
                        error = abs((b - r) / r)        #v.absoulto de(actual-anterior)/actual
                    b = r
                else:
                    if i > 1:
                        error = abs((a - r) / r)
                    a = r

                raiz = r
                print("r= ", raiz)
                if error != 10:
                   print("error relativo", error)
                   print("---------------------------------------")

            if i < 100:
                    print("Raiz final mas aproximada ", raiz,"\n",
                          "Total de Iteraciones: ", i, "\n" ,
                            "Error relativo: ", error)
            else:
                    print("No se encontró en el instervalo definido la raiz de la función en 100 iteraciones")
        else:
            print("No se puede iniciar el metodo con f(a) * f(b) > 0")

str_ecuacion = str(input("Ingrese la ecuacion"))
grafica()
comprobacion()

