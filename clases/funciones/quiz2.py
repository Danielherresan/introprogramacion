import conversorTemperaturas as ct
import funciones as fn
preguntaNumero = '''Ingrese alguna de estas opciones
    1.Convertir temperaturas
    2.Mostrar clasificación
    3.Mostrar topes
    4.salir
'''
preguntaTemperatura = '''
    K- Mostrar Kelvin
    F- Mostrar Fahrenheint
    C- Mostrar Celsius
'''

#----Mensajes---#
mensajeCelcius = 'Mostrando lista original'
mensajeKelvin = 'Mostran Lista en kelvin'
mensajeFahrenheit = 'Mostran Lista en Fahrenheit'
mensajeDespedida ='☺Que tengas un feliz día ☺☻'
#----Error---#
mensajeErrorEntrada ='valor ingresado no valido'

temperaturaCorporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

temperaturaCorporalFahrenheint = ct.conversionTemeperatura(temperaturaCorporal, 'F')
temperaturaCorporalKelvin = ct.conversionTemeperatura(temperaturaCorporal, 'K')
clasificacionTemperaturas = ct.clasificarTemperaturas(temperaturaCorporal)

opcionEscogida = int(input(preguntaNumero))
while (opcionEscogida !=4):
    #---------Opcion1---------#
    if (opcionEscogida == 1):
        opcionMoneda = input(preguntaTemperatura)
        if (opcionMoneda == 'C'):
            print('la conversión no era necesaria')
            print(mensajeCelcius)
            fn.mostrarLista(temperaturaCorporal)
        elif (opcionMoneda == 'F'):
            print(mensajeFahrenheit)
            fn.mostrarLista(temperaturaCorporalFahrenheint)
        elif (opcionMoneda == 'K'):
            print(mensajeKelvin)
            fn.mostrarLista(temperaturaCorporalKelvin)
        else:
            print(mensajeErrorEntrada)
    #---------Opcion2---------#
    elif (opcionEscogida == 2):
        print('Mostrando clasificación')
        print('°C','\t','Clasificacion')
        fn.mostrar2Lista(temperaturaCorporal, clasificacionTemperaturas)
    #---------Opcion3---------#
    elif(opcionEscogida == 3):
        ct.mostrarTopes(temperaturaCorporal)
    #---------Opcion no valida---------#
    else:
        print(mensajeErrorEntrada)
    opcionEscogida = int(input(preguntaNumero))
print(mensajeDespedida)
