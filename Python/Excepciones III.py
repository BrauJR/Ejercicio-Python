import math 

def calcularaiz(num1):
	if num1<0:
		raise ValueError("No puede ser negativo")
	else:
		return math.sqrt(num1)

op1=int(input("Ingresa un número: "))
try:
	print(calcularaiz(op1))
except ValueError as ElCapo:
	print(ElCapo)

print("Programa terminado")
