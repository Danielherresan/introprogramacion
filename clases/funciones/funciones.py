#----------Sumar dos números -----------#
def sumar (a = 0, b = 0):
    '''
        devuelve la suma de dos números a y b
        por defecto a vale cero al igual que b
    '''
    suma = a + b
    return suma

#----------Restar dos números -----------#
def restar (a = 0, b = 0):
    resta = a - b
    return resta
#----------Multiplicar dos números -----------#
def multiplicar (a = 0, b = 0):
    multiplica = a * b
    return multiplica
#----------dividir dos números -----------#
def dividir (a = 0, b = 1):
    dividi = a / b
    return dividi
#----------potenciar dos números -----------#
def potenciar (base = 0, exponente = 1):
    potencia = base ** exponente
    return potencia
#----------funciones dependientes de otras -----------#
def calcular (operacion, numeroA, numeroB):
    print(operacion(numeroA,numeroB))