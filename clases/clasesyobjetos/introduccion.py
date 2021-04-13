class Humano():
    '''
        Esta es la clase Humano exige atributos
        nombreEntrada: Hace referencia al nombre del usuario
        edadEntrada: Hace referencia al edad del usuario
        estaturaEntrada: Hace referencia al estatura del usuario


        Tiene las siguientes acciones:


        *hablar(mensaje):
            dado un mensaje lo muestra en pantalla
        
        *mostrarAtributos()
            muestra los atributos del usuario
    '''
    def __init__(self, nombreEntrada, edadEntrada,estaturaEntrada):
        print('Hola soy un humano nuevo')
        self.edad = edadEntrada
        self.raza = 'Humano'
        self.nombre = nombreEntrada
        self.estatura = estaturaEntrada
        self.dinero = 0
    
    def hablar(self,mensaje):
        print(f'Hola soy {self.nombre} tengo un mensaje que decir ...', mensaje)
    
    def mostrarAtributos(self):
        print(f'''Mi nombre es {self.nombre}
                    Mi estatura es {self.estatura} metros
                    Mi edad es {self.edad} años
                    Tengo ahorrado {self.dinero} pesos
        ''')
    def recorrerDistancia(self,distanciaMetros):
        for i in range (distanciaMetros):
            print(f'Hola soy {self.nombre} y he recorrido {i+1} metros')

    def ahorraDinero(self):
        preguntaIngresarMontos = 'Ingrese S--> para continuar añadiendo montos y N--> para finalizar : '
        preguntaMonto = 'Cuanto vas a ingresar?: '
        ingresarMontos =input(preguntaIngresarMontos)
        while(ingresarMontos != 'N'):
            monto = float(input(preguntaMonto))
            self.dinero = self.dinero + monto
            print(f'Soy {self.nombre} y tengo {self.dinero} pesos')
            ingresarMontos =input(preguntaIngresarMontos)
        return self.dinero


humano1 = Humano('Daniel',27,1.67)
humano2 = Humano('Mafer',27,1.60)

humano1.hablar('Espero que esten muy bien')
humano2.hablar('chao')
print(humano1.nombre)
print(humano2.nombre)
print(humano2.edad)
humano1.mostrarAtributos()
humano1.recorrerDistancia(25)
humano2.mostrarAtributos()
totalAhorrado = humano2.ahorraDinero()
humano2.mostrarAtributos()
