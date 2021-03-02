
#----Entradas----#
MENSAJE_BIENVENIDA = 'Muy buenos días despierte que esta en clase de 6'
MENSAJE_ERROR = 'Por favor ingresa una opción válida'
PREGUNTA_MENU = ''' Ingrese 
    1- para mostrar los números del 1-5
    2- para preguntar tu nombre
    3- para mostrar el año en el que estamos
    4- salir

'''
PREGUNTA_NOMBRE = 'Ingrese su nombre por favor : '

#___
entrada = 1
while (entrada >=1 and entrada <=3):
    entrada = int(input(PREGUNTA_MENU))
    if (entrada == 1):
        print (1,2,3,4,5)
    elif (entrada == 2):
        nombre = input (PREGUNTA_NOMBRE)
        print (f'Bienvenido {nombre} a este menú emplea las otras opciones' )    
    elif (entrada == 3):
        print ('Estamos en el año 2021')
    elif (entrada == 4):
        print ('Muchas gracias por usar el programa feliz día')
    else:
        entrada = 1
        print(MENSAJE_ERROR)
