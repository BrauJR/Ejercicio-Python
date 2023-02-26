"""
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
	try:
		return num1/num2
	except ZeroDivisionError:
		print("No se puede dividir entre cero")
		return "Operación errónea"	

while True:
	try:
		op1=(int(input("Ingresa el primer número: ")))
		op2=(int(input("Ingresa el primer número: ")))
		break
	except ValueError:
		print("Valores introducidos no validos. Intenta de nuevo.")
   

operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")
"""

def divide():
	try:
		op1=float(input("Ingresa el primer número: "))
		op2=float(input("Ingresa el segundo número: "))
		print("La división es: " + str(op1/op2))
	# except: ERROR GENÉRICO
	except ValueError:
		print("Valores invalidos")
	except ZeroDivisionError:
		print("No se puede dividir entre cero")

	finally:
		print("Fin del programa...")

divide()

"""
def divide():
	try:
		op1=float(input("Ingresa el primer número: "))
		op2=float(input("Ingresa el segundo número: "))
		print("La división es: " + str(op1/op2))
	finally:
		print("Fin del programa...")

divide()
"""
