import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import *
#from scipy.misc import derivative
from sympy import var

print("Metodo de Newton Raphson \n ")

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

def Df(x):
    expr = ecuacion(str_ecuacion)
    b = expr.free_symbols  # recibe una ecuacion tipo string
    var = b.pop()
    derivadaEvaluada = diff(expr,var).evalf(subs={var:x})
    return derivadaEvaluada

def grafica():
    x = np.linspace(-4,8,100)
    plt.plot(x,numpyf(x))
    plt.grid()
    plt.show()

def operaciones():
    x0 = float(input("Digitar el punto de inicio : \n"))
    errorTolerable =float(input("Digitar error tolerable : \n"))
    i=0
    error =9.5
    while error>errorTolerable:
        print("paso")
        i+=1
        temporal =x0
        print(f(x0))
        x1=x0-(f(x0)/Df(x0))
        print(x1)
        x0 = x1
        error=abs((temporal-x0)/x0)
        print("error: ", error)
        print ("Iteración ",i, ", raíz aproximada :",x0)

    print("Raíz final es : ")
    print (x0)
    print("error: ", error)

str_ecuacion = str(input("Ingrese la ecuacion : \n"))

grafica()
operaciones()
