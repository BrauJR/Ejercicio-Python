"""
Concatenación de operadores de comparación
*No hay límite
"""
#Evaluar el salario de un grupo de trabajadores
#De forma jerárquica

salario_presi=int(input("Ingresa el salario del presidente:$ "))
print("El salario del presidente es:" + str(salario_presi))

salario_dire=int(input("Ingresa el salario del director:$ "))
print("El salario del director es:" + str(salario_dire))

salario_jefe=int(input("Ingresa el salario del jefe de departamento:$ "))
print("El salario del jefe de departamento es:" + str(salario_jefe))

salario_admon=int(input("Ingresa el salario del admon:$ "))
print("El salario del admon es:" + str(salario_admon))

if salario_admon<salario_jefe<salario_dire<salario_presi:
	print("Sueldos en orden 😎")
else:
	print("Algo anda mal 🐖")
