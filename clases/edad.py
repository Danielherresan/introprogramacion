#----Constantes----#
MENSAJE_BIENVENIDA = "Bienvenido al código"
MENSAJE_MAYOR_EDAD = "Eres mayor de edad puedes seguir"
MENSAJE_MENOR_EDAD = "Eres menor de edad no puedes seguir"
PREGUNTA_EDAD = "Cuantos años tienes ? :"

#---Entrada al código---#
print (MENSAJE_BIENVENIDA)
edad = int (input(PREGUNTA_EDAD))
isMayor = edad >= 18
resultado = ""
if (isMayor):
    resultado = MENSAJE_MAYOR_EDAD
else :
    resultado = MENSAJE_MENOR_EDAD

print(resultado)

