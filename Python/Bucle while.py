import math
#Es indeterminado

"""
EJEMPLO 1
i = 1
while i<=10:
	print("Ejecución " + str(i))
	i=i+1

print("Termino la ejecución")
"""
"""
EJEMPLO 2
edad = int(input("Ingresa tu edad: "))
while edad<3 or edad>100:
	print("Edad incorrecta. Vuleve a intentarlo")
	edad = int(input("Ingresa tu edad: "))

print("Adelante")
print("Tu edad es "+str(edad)+ " años")
"""

#EJEMPLO 3
print ("Calcula raíz cuadrada")
numero = int(input("Ingresa un número: "))
intentos = 0

while numero<0:
	print("No se puede calcular la raíz de un número negativo")
	if intentos==2:
		print("Lo sentimos, intenta mas tarde")
		break; #Sale y continúa con la ejecución
	numero = int(input("Ingresa un número: "))
	if numero<0:
		intentos=intentos+1
if intentos<2:
	solucion=math.sqrt(numero)
	print("La raíz cuadrada de "+str(numero) + " es: " +str(solucion))


