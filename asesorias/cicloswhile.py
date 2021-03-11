dinero = 1000
while (dinero<1002):
    print(dinero)
    dinero +=1
preguntaNumero ='''
        1-saludo
        2-te pregunto como vas
        3-me despido
'''
numeroEntrada = int(input(preguntaNumero))

isOne = numeroEntrada == 1
isTwo = numeroEntrada == 2
if (isOne):
    print('hola!!!')
elif (isTwo):
    print('como vamos?')
else:
    print('chaooo') 

while (numeroEntrada !=3):
    numeroEntrada = int(input(preguntaNumero))
    isOne = numeroEntrada == 1
    isTwo = numeroEntrada == 2
    isDifferent = numeroEntrada !=3
    if (isOne):
        print('hola!!!')
    elif (isTwo):
        print('como vamos?')
    elif(isDifferent):
        print('recuerda ingresar algo valido')



print ('hello', dinero)
print ('chao que te vaya bien')



