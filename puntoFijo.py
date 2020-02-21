import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import *
#from scipy.misc import derivative

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
    x = np.linspace(-2,2,100)
    plt.plot(x,numpyf(x))
    plt.grid()
    plt.show()
def puntoFijo():

    x=input("Ingrese primer valor:")
    if(abs(Df(x))<1):
        tol = (float(input('Ingrese tolerancia: ')))
        print("     n         x0         error")
        print("     0.0000     %7.4f       ---------\n",x)
        error=100
        n=0
        while(error>tol):
            ant = x
            x=f(x)
            if(n>=1):
                error=abs((x-ant)/x)
            else:
                error
            disp=[n,x,error]
            n = n + 1
            print(disp)
    else:
        print('Ingrese otra funcion g(x), pues en la actual el metodo diverge')
str_ecuacion = str(input("Ingrese la ecuacion :\n"))
grafica()
puntoFijo()