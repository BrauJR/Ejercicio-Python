"""
OPERADORES LÓGICOS "and" , "or"
Ejemplo:
Evaluar si un alumno tiene derecho a beca o no, de acuerdo a las siguientes categorias:
*Distancia>50Km
*Número hermanos>4
*Ingreso económico<=2000
"""
print("Becas Benito Juárez")
distancia=int(input("Ingresa la distancia de casa a escuela(km): "))
print("Distancia:" + str(distancia) + " km")
hermanos=int(input("Ingresa el número de hermanos(tomandote en cuenta): "))
print("N° hermanos:" + str(hermanos))
ingreso=int(input("Ingresa el ingreso mensual: "))
print("Ingreso mensual" + str(ingreso))

if (distancia>50) and (hermanos>4) or (ingreso<=2000):
	print("\nFelicidades tienes la beca")
else:
	print("\n¡Sigue participando!")