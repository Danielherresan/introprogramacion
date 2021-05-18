
isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        edad = int (input('ingrese su edad :'))
        isCorrectInfo = True
    except ValueError:
        print('ingresaste un dato no válido')
nombreArchivo = input('Ingrese el nombre del archivo que desea encontrar: ')
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    print(f'El archivo {nombreArchivo} no se ha encontrado')

base = 4
divisor = 0
try:
    dividir = base/divisor
except ZeroDivisionError:
    print('El divisor ingresado es igual a 0 por lo tanto es imposible dividir')

nombre = 'Daniel'
print(nombre.isalpha())
assert (nombre.isalpha())


isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        nombre = input('ingrese su Nombre :')
        assert (nombre.isalpha())
        isCorrectInfo = True
    except AssertionError:
        print('ingresaste un dato no válido')

isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        edad = int(input('ingrese su Edad :'))
        assert (edad >= 18)
        isCorrectInfo = True
    except AssertionError:
        print('Los menores de edad no pueden acceder')
    except ValueError:
        print('las edades son números enteros')

listas = [2,43,42,4]
try:
    listas[5]
except IndexError:
    print('El indice es mayor al tamaño de la lista')

