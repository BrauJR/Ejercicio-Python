"""
°Recorrer strings
°Tipo de dato range
°Notaciones especiales con print
"""

"""
EJEMPLO 1
for i in "Quiubo": #Imprime tantas veces como caracteres hay en la palabra
	print("Hola", end=" ") #Como queremos que imprima después de una vuelta(No salto de línea)
"""
"""
#EJEMPLO 2"
contador=0
correo=input("Ingresa correo electrónico: ")
for i in correo:
	if(i=="@" or i=="."):
		contador=contador+1
if contador==2:
  #correo:
	print("Correo correcto ✅ ")
else:
	print("Correo incorrecto ❌")
"""

#EJEMPLO 3
for i in range (5): #Crea una lista o serie de elemtnos de 0-4
	print("Mensaje " + str(i+1))
