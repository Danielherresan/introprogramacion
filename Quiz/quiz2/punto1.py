listaPesos = [20000,30000,4000,2500,1000,7600]
preguntaMoneda = '''
    C- Mostrar original en pesos colombiano
    D- Mostrar en Dolares
    E- Mostrar en Euros
'''
mensajePesos = 'Mostrando lista original'
mensajeDolares = 'Mostran Lista en dolares'
mensajeEuros = 'Mostran Lista en euros'
mensajeErrorEntrada ='valor ingresado no valido'

listaEuros = []
for elemento in listaPesos:
    conversor = round (elemento*0.00023,2)
    listaEuros.append(conversor)
listaDolares = []
for elemento in listaPesos:
    conversor = round (elemento*0.00028,2)
    listaDolares.append(conversor)

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
