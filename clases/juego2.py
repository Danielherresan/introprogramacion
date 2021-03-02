
import random
#-----Entradas----#
MENSAJE_SALUDAR = '''
    Bienvenido 
        a este programa, 
    !!!jueguemos!!'''
PREGUNTAR_NUMERO = '''
        En este juego debes asetar un número entero
        que va desde el 1-10, la idea es que 
        lo puedes intentar ante de que se te
        acaben las vidas...no existe vida 0
        Muchos éxitos, ingresa tu numero
'''
PREGUNTA_DIFICULTAD = '''
    1- Fácil
    2- Moderado
    3- Difícil
'''
PREGUNTAR_FALLIDA = 'Aaaaah! Fallaste ☻☺☻♥♦♣♠• ingresa otro número :'
MENSAJE_GANASTE = 'Felicidades ganaste!!'
MENSAJE_PERDISTE = 'Perdiste D: "vuelve" a intentarlo!!'
#---Entrada al código---#
numeroOculto = random.randint(1,10)
vidas = None


dificultad = int (input(PREGUNTA_DIFICULTAD))
while (dificultad !=1 and dificultad != 2 and dificultad !=3 ):
    print ('ingresa una opción válida')
    dificultad = int (input(PREGUNTA_DIFICULTAD))
    

if (dificultad == 1):
    print ('Modo fácil activado')
    vidas = 5
elif (dificultad == 2):
    print ('Modo moderado activado')
    vidas = 3
else :
    print ('Modo Difícil activado, sssss mucho cuidado')
    vidas = 1

numeroIngresado = int (input(PREGUNTAR_NUMERO))
while (numeroIngresado != numeroOculto and vidas>1):
    vidas -=1
    print (f'te quedan {vidas} vidas')
    numeroIngresado =int(input(PREGUNTAR_FALLIDA))

if (vidas >= 0 and numeroIngresado == numeroOculto):
    print (MENSAJE_GANASTE)
else:
    print (MENSAJE_PERDISTE,'El numero era el ', numeroOculto)