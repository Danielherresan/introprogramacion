#-----constantes-----#
PREGUNTA_PESO = "Cuanto pesas en kg? :"
PREGUNTA_ESTATURA = "Cuanto mides en mts? :"
MENSAJE_BIENVENIDA = "Hola como estas? Voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "Tu IMC es ... "

#----Entrada código ----#
print(MENSAJE_BIENVENIDA)
peso = float (input(PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
imc = peso/(estatura**2)
print(MENSAJE_DESPEDIDA, imc)
isObeso = imc >= 30
print ("El resultado de la prueba de obecidad es ...", isObeso)
