import numpy as np
import matplotlib.pyplot as plt
from sympy import *

class MetodoRectangulos:
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


    def grafica(self, li, ls):
        a=int(sympify(li).evalf())
        b=int(sympify(ls).evalf())
        x = np.linspace(a, b, 100)        # linspace(inicio de la grafica, fin de la grafica,
        #  numero de muestras:cambia la forma grafica)
        plt.plot(x, self.numpyf(x))
        plt.grid()
        plt.show()
        plt.xlabel('X')
        plt.ylabel('f(x)')


    def metodo(self, n, li, ls):      # parametros(numero de particiones, limite inferior,limite superior)
        # hallar el ancho de los rectangulos
        a=sympify(li).evalf()
        b=sympify(ls).evalf()
        print(a)
        print(b)
        h = (b-a)/n
        print(h)
        # POR IZQUIERDA
        contador = 1
        xo = a
        suma = self.f(xo)*h
        for i in range(0, n-1):
            xi = xo + (contador*h)
            suma += self.f(xi)*h
            contador += 1
        porIzquierda = suma
        xo = a+h
        suma = self.f(xo)*h
        contador = 1
        # POR DERECHA
        for i in range(1, n):
            xi = xo + (contador*h)
            suma += self.f(xi)*h
            contador += 1
        porDerecha = suma
        contador = 1
        xo = a
        x1 = a+h
        suma = 0
        # POR MITAD
        for i in range(0, n):
            xi = (xo + x1)/2    # halla el punto de la mitad del ancho del rectangulo
            xo = x1
            x1 = xo + h
            suma += self.f(xi)*h     # suma las alturas y las multiplica por el ancho
        porMitad = suma
        print("Resultados:\n" + "Por Izquierda: ", porIzquierda, "\nPor Derecha: ",
              porDerecha, "\nPunto Medio: ", porMitad)


print("METODO DE LOS RECTANGULOS")
str_ecuacion = input("Digite la función sin la integral")
print("Digite los limites inferior(a) y superior (b)")
a = input("a: ")
b = input("b: ")
print("Digite el numero de particiones")
n = int(input("n: "))
metodoDeRect=MetodoRectangulos()
metodoDeRect.ecuacion(str_ecuacion)
metodoDeRect.grafica(a, b)
metodoDeRect.metodo(n, a, b)
