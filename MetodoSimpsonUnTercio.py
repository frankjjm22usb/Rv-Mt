import numpy as np
import matplotlib.pyplot as plt
from sympy import *

class MetodoSimpsonUnTercio:
    def numpyf(self, m):
        x, y, z = symbols("x y z")
        expr = sympify(str_ecuacion)
        reemplaza = lambdify(x, expr, "numpy")
        return reemplaza(m)


    def ecuacion(self, str_ecuacion):
        expr = sympify(str_ecuacion)        # Simplifica la ecuacion,
        #  debe hacerse para que sympy reconozca el String como ecuacion
        return expr     # Retorna la ecuacion simplificada


    def f(self, xo):
            expr= self.ecuacion(str_ecuacion)
            b = expr.free_symbols   # recibe una ecuacion tipo string
            var = b.pop()
            reemplaza = expr.evalf(subs = {var: xo})    #Sustituye las x de la ecuacion por xo
            return reemplaza


    def Df(self,x):
        expr = self.ecuacion(str_ecuacion)
        b = expr.free_symbols  # recibe una ecuacion tipo string
        var = b.pop()
        print(diff(expr, var,4))
        derivadaEvaluada = diff(expr, var,4).evalf(subs={var: x})
        return derivadaEvaluada


    def grafica(self, li, ls):
        a = float(sympify(li).evalf())
        b = float(sympify(ls).evalf())
        x = np.linspace(a,b, 100)        # linspace(inicio de la grafica, fin de la grafica,
        #  numero de muestras:cambia la forma grafica)
        plt.plot(x, self.numpyf(x))
        plt.grid()
        plt.show()
        plt.xlabel('X')
        plt.ylabel('f(x)')


    def metodo(self, n, li, ls):
        a = sympify(li).evalf()
        b = sympify(ls).evalf()
        if n % 2 != 0:
            n = int(n+1)      # El numero de particiones debe ser par entero positivo
        h = (b-a)/n
        sumaPares = 0
        sumaImpares = 0
        for i in range(1, n):     #si el n=6 iterará de 1 a 5=(n-1)
            if i % 2 == 0:
                sumaPares += self.f(a + h * i)
            if i % 2 != 0:
                sumaImpares += self.f(a + h * i)
        sumaTotal = (h/3)*(self.f(a)+(4*sumaImpares)+(2*sumaPares)+self.f(b))
        return sumaTotal


    def error(self,li,ls,n):
        a = float(sympify(li).evalf())
        b = float(sympify(ls).evalf())
        h = (b-a)/n
        error = abs((-h ** 5 / 90) * self.Df((a + b) / 2))
        return error

simpsonUnTercio = MetodoSimpsonUnTercio()
print("METODO DE SIMPSON 1/3")
str_ecuacion = input("Digite la función sin la integral")
print("Digite los limites inferior(a) y superior (b)")
a =input("a: ")
b =input("b: ")
simpsonUnTercio.grafica(a, b)
print("Digite el numero de particiones")
n = int(input("n: "))
print(simpsonUnTercio.ecuacion(str_ecuacion))

print("Resultado",simpsonUnTercio.metodo(n, a, b))
print("Error",simpsonUnTercio.error(a,b,n))