"""
Yield from.-
Simplifica el código de los generadores en el caso de utilizar bucles anidados
"""

def devuelveCiudades(*ciudades): #Va a recibir un número indeterminado de elementos en forma de tupla
	for elemento in ciudades:
		#for subelemento in elemento:
			yield from elemento

ciudades_devueltas=devuelveCiudades("Madrid", "Barcelona", "Valladolid")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))





