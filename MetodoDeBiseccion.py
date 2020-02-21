from builtins import input, print, list

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

class metodoBiseccion:
    def numpyf(self, m,str_ecuacion):
        x, y, z = symbols("x y z")
        expr = sympify(str_ecuacion)
        reemplaza = lambdify(x, expr, "numpy")
        return reemplaza(m)

    def ecuacion(self, str_ecuacion):
        expr = sympify(str_ecuacion)    # Simplifica la ecuacion, debe hacerse para que sympy reconozca el String como ecuacion
        return expr     # Retorna la ecuacion simplificada

    def f(self, Xo,str_ecuacion):
            expr= self.ecuacion(str_ecuacion)
            b = expr.free_symbols  # recibe una ecuacion tipo string
            var = b.pop()
            reemplaza = expr.evalf(subs = {var: Xo})    #Sustituye las x de la ecuacion por xo
            return reemplaza
    def grafica(self,str_ecuacion):

        x = np.linspace(-2, 2,  100)  # linspace(inicio de la grafica, fin de la grafica, numero de muestras:cambia la forma grafica)
        plt.plot(x, self.numpyf(x,str_ecuacion))
        plt.grid()
        plt.show()
        plt.xlabel('X')
        plt.ylabel('f(x)')


    def comprobacion(self,a,b,ec, erroTolerable):

        #Evalua si el intervalo está bien definido
        if a > b:
            raise ValueError("Intervalo mal definido, a debe ser menor que b")
        else:

            if self.f(a,ec) * self.f(b,ec) < 0:
                iteraciones = [["i", "raíz", "error"], ]
                error = 10
                i = 0
                while error > erroTolerable and i <= 100:       #parará cuando el error sea menor al tolerable
                    i += 1
                    #print("iteracion ", i)
                    r = (a+b) / 2
                    fa = self.f(a,ec)       # Evalúa la función con el valor de a
                    fr = self.f(r,ec)       # Evalúa la función con el valor de r
                    #print("f(a)= " , fa)
                    #print("f(b)= " , self.f(b,ec))
                    #print("f(r)= ", fr)

                    if fr == 0:
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
                    # print("r= ", raiz)
                    #if error != 10:

                       # print("error relativo", error)
                       # print("---------------------------------------")
                    iteraciones.append([i,raiz,error],)
                if i < 100:
                    lista= [raiz,error]
                    resultado= "Raiz final mas aproximada ", raiz,"\n","Total de Iteraciones: ", i,"\n Error relativo: ", error
                    for item in iteraciones:
                        print(":", str(item[0]), " " * (2 - len(str(item[0]))),
                              ":", str(item[1])," " * (16 - len(str(item[1]))),
                               ":", str(item[2])," " * (26 - len(str(item[2]))),":")
                    return iteraciones[:]

                else:
                     resultado="No se encontró en el instervalo definido la raiz de la función en 100 iteraciones"
                     return resultado
            else:
                resultado="No se puede iniciar el metodo con f(a) * f(b) > 0"
                return resultado



"""
str_ecuacion = str(input("Ingrese la ecuacion"))
biseccion = metodoBiseccion()
print("De acuerdo a la grafica digite el limite inferior (a) y superior (b)")
a = float(input("a: "))
b = float(input("b: "))
erroTolerable = float(input("Escriba el error de tolerancia: "))
biseccion.grafica(str_ecuacion)
print(biseccion.comprobacion(a,b,str_ecuacion,erroTolerable))

"""



