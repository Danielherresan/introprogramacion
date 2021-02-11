# Estos son booleans que son variables que solo valen 
# verdadero o Falso
pruebaV = True
pruebaF = False
print (pruebaF)
print(pruebaV)
pruebaV = pruebaF
print (pruebaV)
edad = 27
estatura = 1.67
peso = 84
NOMBRE = "Daniel Herrera Sánchez"
print ("#"*15,"Mayor Edad", "#"*15)
isMayorEdad = edad >= 18
print (isMayorEdad)
print ("#"*15,"Bajo la Estatura promedio", "#"*15)
isMayorEstatura = estatura < 1.70
print(isMayorEstatura)
# Calculando si el peso es diferente de 84
print ("#"*15,"Peso diferente 84", "#"*15)
isPesoDiferente = peso != 84
print (isPesoDiferente)
# vamos ver si un apellido esta en el nombre completo
apellido = "Herrera"
isApellido = apellido in NOMBRE
print ("#"*15,"Esta apellido en el nombre?", "#"*15)
print (isApellido)


