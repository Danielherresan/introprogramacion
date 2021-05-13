import matplotlib.pyplot as plt
def agregarElementos(pregunta1, pregunta2):
    lista1 = []
    lista2 = []
    for i in range(5):
        print (f'ingresando dato {i+1} de 5')
        lista1.append(input(pregunta1))
        lista2.append(float(input(pregunta2)))
    return lista1, lista2

#----------Punto1--------------#
preguntaSnack = 'ingrese su snack favorito: '
preguntaPrecio = 'ingrese el precio del snack: '
#listaSnaks, listaPrecios = agregarElementos(preguntaSnack,preguntaPrecio)
#print(listaSnaks, listaPrecios)
#plt.bar(listaSnaks, listaPrecios)
#plt.show()
#----------Punto2--------------#
preguntaCiudad = 'Ingrese su ciudad Favorita :'
preguntaPoblacion = 'Ingrese la poblacion : '

listaCiudades, listaPoblacion = agregarElementos(preguntaCiudad, preguntaPoblacion)
mayor= max(listaPoblacion)
ubicacion = listaPoblacion.index(mayor)
_explode = [0,0,0,0,0]
_explode[ubicacion] = 0.4

plt.pie(listaPoblacion, labels = listaCiudades, explode= _explode)
plt.show()
#
