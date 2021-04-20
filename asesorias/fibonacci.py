#numero1 = 0
#numero2 = 1
#numero3 = 1
#numero4 = 2
#numero5 = 3
#numero6 = 5
#numero7 = 8
#numero8 = 13
#numero9 = 21
#numero10 = 34
def sucesionFibonacci(numeroSuc):
    numeroSuc -=1
    valorMostrar = 0
    numeroActual = 1
    numeroAnterior = 0
    if numeroSuc <= 1:
        valorMostrar = numeroSuc
    else:
        print('calcular sucesión')
        for i in range(numeroSuc-1):
            auxiliar = numeroActual
            nuevoNumero = numeroActual + numeroAnterior
            numeroActual = nuevoNumero
            numeroAnterior = auxiliar
        valorMostrar = numeroActual
    return valorMostrar

print(sucesionFibonacci(1))
print(sucesionFibonacci(3))
print(sucesionFibonacci(10))
print(sucesionFibonacci(14))
print(sucesionFibonacci(100))





