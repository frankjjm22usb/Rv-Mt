# Area de un trapecio A= (B+b)h/2



import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from sympy.core import sympify


def numpyf(m):
    x, y, z = symbols("x y z")
    expr = sympify(str_ecuacion)
    reemplaza = lambdify(x, expr, "numpy")
    return reemplaza(m)


def ecuacion(str_ecuacion):
    expr = sympify(str_ecuacion)    
    return expr     


def f(xo):
        expr= ecuacion(str_ecuacion)
        b = expr.free_symbols   
        var = b.pop()
        reemplaza = expr.evalf(subs = {var: xo})
        return reemplaza

def grafica(li, ls):
    a = int(sympify(li).evalf())
    b = int(sympify(ls).evalf())
    x = np.linspace(a, b,  100)
    plt.plot(x, numpyf(x))
    plt.grid()
    plt.show()
    plt.xlabel('X')
    plt.ylabel('f(x)')

def derivada(a,b):
    ramdom1 = np.random.rand()
    print(ramdom1)
    aleatorio = a+(b-a)*ramdom1
    print(aleatorio)
    expr = ecuacion(str_ecuacion)
    b= expr.free_symbols
    var=b.pop()
    primeraDerivada = diff(expr,var,2)
    derivadaEvaluada = primeraDerivada.evalf(subs={var:0})
    print("derivada evaluada",derivadaEvaluada)
    return derivadaEvaluada

def metodo(n,li,ls):
    a = sympify(li).evalf()
    b = sympify(ls).evalf()
    print(a)
    print(b)
    suma = 0
    tempb=b
    tempa=a
    Dx = (b-a)/n
    for i in range(n):
        Area = (f(a)+ f(a+Dx)) * Dx /2
        suma = suma+Area
        a = a +Dx
    print("El area es aproximadamente ",suma)
    #VT = 9*np.pi /2
    segundaDerivada = derivada(tempa,tempb)
    error = abs((-1/12)*(tempb-tempa)**3)*segundaDerivada
    #print ("El error porcentual es de : ",abs(VT-suma)/ VT * 100,"%")
    print("El error porcentual es de : ", error ,"%")

print("metodo de Trapecios")
str_ecuacion = input("Digite la función sin la integral")
print("Digite los limites inferior(a) y superior (b)")
a = input("a: ")
b = input("b: ")
print("Digite el numero de particiones")
n = int(input("n: "))
ecuacion(str_ecuacion)
grafica(a, b)
metodo(n, a, b)

