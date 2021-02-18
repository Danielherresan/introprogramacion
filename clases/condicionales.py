#-----constantes------#
MENSAJE_BIENVENIDA = "Hola espero que estes bien"
MENSAJE_MAYOR = "El número A es mayor que B"
MENSAJE_MENOR = "El número A es menor que B"
MENSAJE_IGUAL = "A y B son iguales"
PREGUNTA_NUMERO_A = "Ingrese un número A :"
PREGUNTA_NUMERO_B = "Ingrese un número B :"

#----Entrada al código---#
print (MENSAJE_BIENVENIDA)
numeroA = int (input(PREGUNTA_NUMERO_A))
numeroB = int (input(PREGUNTA_NUMERO_B))
isMayor = numeroA > numeroB
isMenor = numeroA < numeroB
resultado = ""
if (isMayor):
    resultado = MENSAJE_MAYOR
elif (isMenor) :
    resultado = MENSAJE_MENOR
else:
    resultado = MENSAJE_IGUAL

print(resultado)

