#----Preguntas
preguntaNumero = '''Ingrese alguna de estas opciones
    1.Hacer conversión de pesos a dolares o Euros
    2.Agrege un valor a la lista de pesos
    3.Mostrar valor más alto, más bajo y promedio
    4.Eliminar elemento de la lista
    5.Salir
'''
preguntaMoneda = '''
    C- Mostrar original en pesos colombiano
    D- Mostrar en Dolares
    E- Mostrar en Euros
'''
preguntarNumero = 'Ingrese un valor en COP :'
preguntaBorrarCoordenada = 'Ingrese la posición que desea borrar:'
#----Mensajes---#
mensajePesos = 'Mostrando lista original'
mensajeDolares = 'Mostran Lista en dolares'
mensajeEuros = 'Mostran Lista en euros'
mensajeMayor = 'El mayor numero ingresado es -->'
mensajeMenor = 'El menor numero ingresado es -->'
mensajePromedio = 'El promedio es -->'
mensajeDespedida ='☺Que tengas un feliz día ☺☻'
#----Error---#
mensajeErrorEntrada ='valor ingresado no valido'


listaPesos = [20000,30000,4000,2500,1000,7600]

#Conversion punto 1
listaEuros = []
for elemento in listaPesos:
    conversor = round (elemento*0.00023,2)
    listaEz)
listaDolares = []
for elemento in listaPesos:
    conversor = round (elemento*0.00028,2)
    listaDolares.append(conversor)


opcionEscogida = int(input(preguntaNumero))
while (opcionEscogida !=5):
    #---------Opcion1---------#
    if (opcionEscogida == 1):
        opcionMoneda = input(preguntaMoneda)
        if (opcionMoneda == 'C'):
            print(mensajePesos)
            print(listaPesos)
        elif (opcionMoneda == 'D'):
            print(mensajeDolares)
            print(listaDolares)
        elif (opcionMoneda == 'E'):
            print(mensajeEuros)
            print(listaEuros)
        else:
            print(mensajeErrorEntrada)
    #---------Opcion2---------#
    elif (opcionEscogida == 2):
        valorIngresado = float (input(preguntarNumero))
        listaPesos.append(valorIngresado)
        print(listaPesos)
    #---------Opcion3---------#
    elif(opcionEscogida == 3):
        print(mensajeMayor, max(listaPesos))
        print(mensajeMenor, min(listaPesos))
        print(mensajePromedio,sum(listaPesos)/len(listaPesos))
    #---------Opcion4---------#
    elif(opcionEscogida == 4):
        print (listaPesos)
        posicion = int(input(preguntaBorrarCoordenada)) - 1
        listaPesos.pop(posicion)
        print(listaPesos)
    #---------Opcion no valida---------#
    else:
        print(mensajeErrorEntrada)
    opcionEscogida = int(input(preguntaNumero))

print (mensajeDespedida)