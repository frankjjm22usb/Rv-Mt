import sympy
from sympy import *
import numpy as np


class DII:
    def ecuacion(self, str_ecuacion):
        expr = sympify(str_ecuacion)        # Simplifica la ecuacion,

        #  debe hacerse para que sympy reconozca el String como ecuacion
        return expr     # Retorna la ecuacion simplificada

    def Df(self,str_ecuacion):
        expr = self.ecuacion(str_ecuacion)
        b = expr.free_symbols  # recibe una ecuacion tipo string
        var = b.pop()
        print(expr)
        print(diff(expr, var,1))
        derivadaEvaluada = diff(expr, var,1).evalf(subs={var: x})
        return derivadaEvaluada


m=DII()
x=Symbol('a')
x=Symbol('x')
print(integrate(exp(-0.5*x)*(sin(x))**2,x))
print(diff(sin(2*x),x))

"""
# str_ecuacion= str(input("Ingrese la ecuacion"))
nivel=input("ingrese el grado de la derivada")
m.Df(5,nivel)
"""