def conversionTemeperatura(temperaturas, unidad):
    '''Convierte una lista de temperaturas
    Entradas: 
        unidad :según la unidad ingresada, puede ser ...
                K--> Kelvin
                F--> fahrenheint
        temperaturas: lista temperaturas en grados centigrados
    Retorna:

        Si se ingresa un valor invalido devolvemos None
        Devuelve la lista convertida en las unidades deseadas
    '''
    listaConvertida = []
    for tempatura in temperaturas:
        conversion = None
        if unidad == 'F':
            conversion = tempatura *1.8 +32
        elif unidad == 'K':
            conversion = tempatura + 273.15
        else :
            listaConvertida = None
        listaConvertida.append(round(conversion,2))
    return listaConvertida
def clasificarTemperaturas (temperaturas):
    '''Retorna la clasificación de las temperaturas ingresadas
    deben estar en grados centigrados
    '''
    listaClasificacion = []
    estado = None
    for temperatura in temperaturas:
        if temperatura < 36:
            estado = 'Hipotermia'
        elif temperatura >= 36 and temperatura < 37.6:
            estado = 'Normal'
        else:
            estado = 'Fiebre'
        listaClasificacion.append(estado)
    return listaClasificacion
def mostrarTopes(lista):
    mayor =round(max(lista),2)
    menor =round(min(lista),2)
    periodoHoras =round(24/len(lista),2)
    print('La mayor temperatura es', mayor)
    print('La menor temperatura es', menor)
    print('El periodo de muestras es', periodoHoras)

