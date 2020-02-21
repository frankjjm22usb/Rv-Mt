
from builtins import input, print

import numpy as np
import matplotlib.pyplot as plt
from sympy import *


class graficador:

    def numpyf(self, m):
        x, y, z = symbols("x y z")
        expr = sympify(str_ecuacion)
        print(expr)
        reemplaza = lambdify(x, expr, "numpy")
        return reemplaza(m)

    def ecuacion(self, str_ecuacion):
        expr = sympify(str_ecuacion)    # Simplifica la ecuacion, debe hacerse para que sympy reconozca el String como ecuacion
        return expr     # Retorna la ecuacion simplificada


    def f(self, Xo):
            expr= self.ecuacion(str_ecuacion)
            b = expr.free_symbols  # recibe una ecuacion tipo string
            var = b.pop()
            reemplaza = expr.evalf(subs = {var: Xo})    #Sustituye las x de la ecuacion por xo
            return reemplaza


    def grafica(self,ec):
        x = np.linspace(-4,4,  100)  # linspace(inicio de la grafica, fin de la grafica, numero de muestras:cambia la forma grafica)
        fig,ax = plt.subplots()
        ax.plot(x, self.numpyf(x))
        #ax.set_aspect('equal')
        ax.grid(True, which='both')

        ax.axhline(y=0,color='k')
        ax.axvline(x=0, color='k')
        plt.show()
        plt.xlabel('X')
        plt.ylabel('f(x)')


str_ecuacion = sympify(str(input("Ingrese la ecuacion")))
print(str_ecuacion)
grafic=graficador()
grafic.grafica(str_ecuacion)