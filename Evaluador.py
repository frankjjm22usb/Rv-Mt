import sympy
from sympy import *     #init_session #Importa todos los modulos a la vez y la impresion de expresiones

class Evaluador:
    def ecuacion(self,str_ecuacion):
        expr = sympify(str_ecuacion)    #Simplifica la ecuacion, debe hacerse para que sympy reconozca el String como ecuacion
        return expr  #Retorna la ecuacion simplificada

    def evaluar(self,Xo,str_ecuacion):
        x = sympify(Xo);
        expr= self.ecuacion(str_ecuacion)
        b = expr.free_symbols  # recibe una ecuacion tipo string
        var = b.pop()
        reemplaza = expr.evalf(subs = {var: x})    #Sustituye las x de la ecuacion por xo
        return reemplaza


evaluador=Evaluador()

repetir = 0

while repetir == 0:
    str_ecuacion = input("Ingrese la ecuacion")
    Xo = sympify(input("Ingrese Xo"))
    resultado = evaluador.evaluar(Xo,str_ecuacion)
    print(resultado)
    repetir = int(input("Desea evaluar otra expresion (0)Si (1)No"))
