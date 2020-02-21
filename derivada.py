from sympy import*
from scipy.misc import derivative
x=Symbol('x')
y=2*x**3
derivada=y.diff(x)
print(derivada)
f=lambda x:sin(x)
print(derivative(f,2,dx=1e-2))