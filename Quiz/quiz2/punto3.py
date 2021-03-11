listaPesos = [20000,30000,4000,2500,1000,7600]
mensajeMayor = 'El mayor numero ingresado es -->'
mensajeMenor = 'El menor numero ingresado es -->'
mensajePromedio = 'El promedio es -->'
print(mensajeMayor, max(listaPesos))
print(mensajeMenor, min(listaPesos))
print(mensajePromedio,sum(listaPesos)/len(listaPesos))