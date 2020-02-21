import numpy as np
import matplotlib.pyplot as plt
from sympy import *

class MetodoSimpsonTresOctavos:
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


    def grafica(self, li,ls):
        a = float(sympify(li).evalf())
        b = float(sympify(ls).evalf())
        print(a)
        print(b)
        x = np.linspace(-5, b, 100)        # linspace(inicio de la grafica, fin de la grafica,
        #  numero de muestras:cambia la forma grafica)
        plt.plot(x, self.numpyf(x))
        plt.grid()
        plt.xlabel('X')
        plt.ylabel('f(x)')
        plt.show()


    def calculate(self,li, ls, n):
        a = sympify(li).evalf()
        b = sympify(ls).evalf()
        if n%3==1:
            n+=2
        elif n%3==2:
            n+=1
        h = float((b - a) / n)
        print("h",h)
        sum=0
        xo=a
        n=int((n / 3))
        # Calculates value till integral limit
        for i in range(1, n+1):
            x1=xo+h
            x2=x1+h
            x3=x2+h
            #print("i",i,"0",xo,"1",x1,"2",x2,"3",x3)
            sum+=3/8*h*(self.f(xo)+3*self.f(x1)+3*self.f(x2)+self.f(x3))
            xo=x3

        return sum


    def error(self,li,ls,n):
        a = sympify(li).evalf()
        b = sympify(ls).evalf()
        h = (b-a)/n
        error = abs((n*(h ** 5) / 80) * self.Df((a + b) / 2))
        return error

tresOctavos=MetodoSimpsonTresOctavos()

print("METODO DE SIMPSON 3/8")
str_ecuacion = input("Digite la función sin la integral")
print("Digite los limites inferior(a) y superior (b)")
a =input("a: ")
b =input("b: ")
tresOctavos.grafica(a, b)
print("Digite el numero de particiones")
n = int(input("n: "))
print(tresOctavos.ecuacion(str_ecuacion))


print("Resultado",tresOctavos.calculate(a ,b,n))
print("Error",tresOctavos.error(a,b,n),"%")
