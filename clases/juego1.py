#-----Entradas----#
MENSAJE_SALUDAR = '''
    Bienvenido 
        a este programa, 
    !!!jueguemos!!'''
PREGUNTAR_NUMERO = '''
        En este juego debes asetar un número entero
        que va desde el 1-10, la idea es que 
        lo puedes intentar las veces que 
        quieras...
        Muchos éxitos, ingresa tu numero
'''
PREGUNTAR_FALLIDA = 'Aaaaah! Fallaste ☻☺☻♥♦♣♠• ingresa otro número :'
MENSAJE_GANASTE = 'Felicidades ganaste!!'
MENSAJE_PERDISTE = 'Perdiste D: "vuelve" a intentarlo!!'
#---Entrada al código---#
numeroOculto = 7
vidas = 5
print(MENSAJE_SALUDAR)
numeroIngresado = int(input(PREGUNTAR_NUMERO))
if (numeroIngresado != numeroOculto):
    vidas-=1
while (numeroOculto != numeroIngresado and vidas >0) :
    numeroIngresado = int(input(PREGUNTAR_FALLIDA))
    vidas -=1 

if (vidas >0):
    print (MENSAJE_GANASTE)
    print (vidas)
else:
    print (MENSAJE_PERDISTE, 'EL numero era el ', numeroOculto)