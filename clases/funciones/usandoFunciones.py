import funciones as fn
import random as rd
def sumar (a,b):
    return a+b
print(sumar(2,6))
print(fn.sumar(2,4))
print(fn.calcular(sumar,2,4))
print(fn.calcular(fn.sumar,2,4))

print(rd.randint(2,6))