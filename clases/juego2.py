
import random
#-----Entradas----#
MENSAJE_SALUDAR = '''
    Bienvenido 
        a este programa, 
    !!!jueguemos!!'''
MENSAJE_SEGUNDO_NIVEL = 'Felicidades pasaste el primer nivel ahora ve por el último!!'
MENSAJE_CALIENTE = 'Estas caliente'
MENSAJE_FRIO = 'Estas Frio'
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
numeroOcultoDos = random.randint (1,10)
vidas = None


dificultad = int (input(PREGUNTA_DIFICULTAD))
while (dificultad !=1 and dificultad != 2 and dificultad !=3 ):
    print ('ingresa una opción válida')
    dificultad = int (input(PREGUNTA_DIFICULTAD))
    

if (dificultad == 1):
    print ('Modo fácil activado')
    vidas = 10
elif (dificultad == 2):
    print ('Modo moderado activado')
    vidas = 5
else :
    print ('Modo Difícil activado, sssss mucho cuidado')
    vidas = 2

numeroIngresado = int (input(PREGUNTAR_NUMERO))
while (numeroIngresado != numeroOculto and vidas>1):
    if (numeroIngresado> numeroOculto):
        print (MENSAJE_CALIENTE)
    else:
        print(MENSAJE_FRIO)
    vidas -=1
    print (f'te quedan {vidas} vidas')
    numeroIngresado =int(input(PREGUNTAR_FALLIDA))
if (vidas >= 0 and numeroIngresado == numeroOculto):
    print (MENSAJE_SEGUNDO_NIVEL)
    numeroIngresado = int (input(PREGUNTAR_NUMERO))
    while (numeroIngresado != numeroOcultoDos and vidas>1):
        if (numeroIngresado > numeroOcultoDos):
            print (MENSAJE_CALIENTE)
        else:
            print(MENSAJE_FRIO)
        vidas -=1
        print (f'te quedan {vidas} vidas')
        numeroIngresado =int(input(PREGUNTAR_FALLIDA))


if (vidas >= 0 and numeroIngresado == numeroOcultoDos ):
    print (MENSAJE_GANASTE)

else:
    print (MENSAJE_PERDISTE,
                            'El numero uno era el ', 
                            numeroOculto,
                            'El número dos era el',
                            numeroOcultoDos)