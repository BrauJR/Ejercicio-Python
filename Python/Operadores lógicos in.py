"""
"in"
Escoger una asignatura optativa de acuerdo a un listado
Funciones: "upper()" , "lower()"
"""

print("Carga de materia optativa \n1.IA \n2.Big Data \n3.Desarrollo de videojuegos")
"""
print("Carga de materia optativa")
print("IA")
print("Big Data")
print("Desarrollo de videojuegos")
"""

opcion=input("Escribe la asignatura escogida: ")
asignatura=opcion.lower()
if asignatura in("ia", "big data", "desarrollo de videojuegos"): 
	print("Materia seleccionada  🏆")
else:
	print("No existe esa materia")

