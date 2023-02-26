"""
Crea un programa que pida dos números por teclado
para que el programa imprima en pantalla cual es 
el número mayor
"""
print("Comparación de números")
num1=int(input("Ingresa número 1: "))
num2=int(input("Ingresa número 2: "))
if num1<num2:
	print("El número mayor es: "+str(num2))
else:
	print("El número mayor es: "+str(num1))
