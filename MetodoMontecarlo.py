import numpy as np
import matplotlib.pyplot as plt
from sympy import *


class MetodoMontecarlo:
    def numpyf(self, m):
        x, y, z = symbols("x y z")
        expr = sympify(str_ecuacion)
        reemplaza = lambdify(x, expr, "numpy")
        return reemplaza(m)

    def ecuacion(self, str_ecuacion):
        expr = sympify(str_ecuacion)  # Simplifica la ecuacion,
        #  debe hacerse para que sympy reconozca el String como ecuacion
        return expr  # Retorna la ecuacion simplificada

    def f(self, xo):
        expr = self.ecuacion(str_ecuacion)
        b = expr.free_symbols  # recibe una ecuacion tipo string
        var = b.pop()
        reemplaza = expr.evalf(subs={var: xo})  # Sustituye las x de la ecuacion por xo
        return reemplaza

    def grafica(self, li, ls):
        a = int(sympify(li).evalf())
        b = int(sympify(ls).evalf())
        x = np.linspace(a, b, 100)  # linspace(inicio de la grafica, fin de la grafica,
        #  numero de muestras:cambia la forma grafica)
        plt.plot(x, self.numpyf(x))
        plt.grid()
        plt.show()
        plt.xlabel('X')
        plt.ylabel('f(x)')

    def metodo(self, n, li, ls, mm):  # parametros(numero de puntos, limite inferior,limite superior)
        a = sympify(li).evalf()
        b = sympify(ls).evalf()
        m = sympify(mm).evalf()
        e=0     #puntos de exito
        # m=max(self.f(a),self.f(b))      #m es la cota superior de f(x) en el intervalo (a,b)
        # print("m",m)
        for i in range(0, n):
            random1 = np.random.rand()
            print("rand1",random1)
            xi = a+(b-a)*random1       # (b-a) es la base del rectangulo de la funcion limitada y m es la altura
            random2 = np.random.rand()
            print("rand2", random2)
            yi = m*random2
            if yi <= self.f(xi):
                e+=1
        areaMaxima=(b-a)*m
        area = (e/n)*areaMaxima  # (b-a)*m es el area del rectangulo maximo
        print("Área aproximada: ", area)

str_ecuacion = input("Digite la función sin la integral")
print("Digite los limites inferior(a) y superior (b)")
a = input("a: ")
b = input("b: ")
print("Digite el numero puntos")
n = int(input("n: "))
print("Digite la cota superior")
m = input("m: ")
montecarlo=MetodoMontecarlo()
montecarlo.ecuacion(str_ecuacion)
montecarlo.metodo(n, a, b, m)