from sympy import *
class MinimosCuadrados:

    def sumatoriaXi(self,xi,potencia):
        suma=0
        for i in range(0, n):
            suma+=(xi[i]**potencia)
        return suma


    def sumatoriaYi(self, yi, potencia):
        suma = 0
        for i in range(0, n):
            suma+=(yi[i]**potencia)
        return suma

    def sT(self, yi, ymedia,n):
        suma = 0
        for i in range(0, n):
            suma+=(yi[i]-ymedia)**2
        return suma


    def sR(self,funcion,xi):
        suma = 0
        for i in range(0, n):
            x = sympify(xi[i]);
            expr=sympify(funcion)
            b = expr.free_symbols  # recibe una ecuacion tipo string
            var = b.pop()
            reemplaza = expr.evalf(subs={var: x})  # Sustituye las x de la ecuacion por xo
            suma+=(yi[i]-reemplaza)**2
        return suma


    def sumatoriaXY(self,xi,yi,potx,poty): #pot=potencia
        suma = 0
        for i in range(0, n):
            suma += ((yi[i]**potx)*(xi[i]**poty))
        return suma

    def funcionLineal(self,n,xi,yi, retorno):
        #lineal = 2
        #cuadratica=4
        #cubica=6
        sumatoriax=[]
        sumatoriay = []
        resultados=[self.sumatoriaYi(yi, 1)]
        funcion1 = [n]
        funcion2 = []
        funcion3 = []
        funcion4 = []
        funcion5 = []
        funcion6 = []
        funcion7 = []
        for i in range(1,8,1):
            # print(i)
            # sumatoriax.append(self.sumatoriaXi(xi,i))
            # sumatoriay.append(self.sumatoriaYi(yi, i))
            resultados.append(self.sumatoriaXY(xi,yi,i,1))
            funcion1.append(self.sumatoriaXi(xi,i))
            funcion2.append(self.sumatoriaXi(xi,i))
            funcion3.append(self.sumatoriaXi(xi,i+1))
            funcion4.append(self.sumatoriaXi(xi, i + 2))
            funcion5.append(self.sumatoriaXi(xi, i + 3))
            funcion6.append(self.sumatoriaXi(xi, i + 4))
            funcion7.append(self.sumatoriaXi(xi, i + 5))
        funcion1.pop()
        print("lineal: ","F1: ",funcion1[0:2],"F2: ",funcion2[0:2],"R1:",resultados[0:2])
        print("cuadratica: ","F1: ",funcion1[0:3],"F2: ",funcion2[0:3],"f3: ",funcion3[0:3],"R2: ",resultados[0:3])
        print("cubica: ", "F1: ",funcion1[0:4], "F2: ",funcion2[0:4],"F3:",funcion3[0:4],"F4: ",funcion4[0:4],"R3: ",resultados[0:4])
        print("grado4: ", "F1: ",funcion1[0:5], "F2: ",funcion2[0:5],"F3:", funcion3[0:5],"F4: ", funcion4[0:5],"F5: ",funcion5[0:5],"R4: ",resultados[0:5])
        print("grado5: ","F1: ",funcion1[0:6],"F2: ", funcion2[0:6],"F3:", funcion3[0:6],"F4: ", funcion4[0:6],"F5: ",funcion5[0:6],"F6: ",funcion6[0:6],"R5: ",resultados[0:6])
        print("grado6: ","F1: ",funcion1[:],"F2: ", funcion2[:],"F3:", funcion3[:],"F4: ", funcion4[:],"F5: ", funcion5[:],"F6: ", funcion6[:],"R6: ",resultados[:])
        respuesta=1
        while(respuesta==1):
            print(self.r2(yi,xi, n))
            respuesta=int(input("Desea hallar de nuevo el R2: si(1) no(0)"))


    def r2(self,yi,xi, n):
        sumyi=self.sumatoriaYi(yi, 1)
        ymedia=(sumyi/n)
        sT=self.sT(yi,ymedia,n)
        funcion=input("ingrese la ecuacion para el coeficiente de correlacion")
        sR=self.sR(funcion,xi)
        r=sqrt((sT-sR)/sT)
        return r


    """
        dicc={"lineal":{"l1":funcion1[0:2],"l2":funcion2[0:2]},"R1":resultados[0:2],
              "cuadratica":{"c1":funcion1[0:3],"c2":funcion2[0:3],"c3":funcion3[0:3]},"R2":resultados[0:3],
              "cubica": {"cc1":funcion1[0:4], "cc2":funcion2[0:4], "cc3":funcion3[0:4],"cc4":funcion4[0:4]},"R3":resultados[0:4],
              "grado4": {funcion1[0:5], funcion2[0:5], funcion3[0:5], funcion4[0:5],funcion5[0:5]},"R4":resultados[0:5],
              "grado5": {"f1":funcion1[0:6],"f2": funcion2[0:6], funcion3[0:6], funcion4[0:6],funcion5[0:6],funcion6[0:6]},"R5":resultados[0:6],
              "grado6": {"f1":funcion1[:],"f2": funcion2[:], funcion3[:], funcion4[:], funcion5[:], funcion6[:]},"R6":resultados[:],
              }
        print(dicc["lineal"])
    """
"""  
       sxip=self.sumatoriaXi(xi,2)
       sxyp=self.sumatoriaXY(xi,yi,1,1)
       # funcion lineal
       f1=n,"a0+",sxi,"a1","=",syi
       f2=sxi,"a0+",sxi2,"a1","=",sxy
       coeficientes ={"R1":{n,sxi,syi},"R2":{sxi,sxi2,sxy}}
       funciones = {"f1": f1, "f2": f2}
       print(funciones)
       if retorno==0:
           return funciones
       elif retorno==1:
           return coeficientes

    def funcionCuadratica(self,n,xi,yi):
        sxi = self.sumatoriaXi(xi, 1)
        syi = self.sumatoriaYi(yi, 1)
        sxi2 = self.sumatoriaXi(xi, 2)
        sxy = self.sumatoriaXY(xi, yi, 1, 1)
        sxi3=self.sumatoriaXi(xi, 3)
        f1 = n,"a0+",sxi,"a1",sxi2,"a2","=",syi
        f2 = sxi,"a0+",sxi2,"a1",sxi3,"a2","=",sxy
        f3=
"""



mC=MinimosCuadrados()
n= int(input("ingrese el numero de valores de 'x', y de 'y'"))
xi=[]
yi=[]

for i in range(0,n):
    valor=float(input("x"))
    xi.append(valor)
for i in range(0,n):
    valor=float(input("y"))
    yi.append(valor)
mC.funcionLineal(n,xi,yi,0)