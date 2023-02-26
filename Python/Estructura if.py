"""
Crear un programa que indique si el alumno esta aprobado oreprobado
(Tomar en cuenta que en un principio todos están aprobados
por el covid-19)
"""

#Con parámtros
def evaluacion(calificacion):
	resultado="Aprobado :)"
	if calificacion<=70:
		resultado="Reprobado :("
	return resultado
print(evaluacion(70))

#Por teclado
print("Evaluacion 2° semestre")
calificacion_alumno=input("Ingrese calificación: ")

def evaluacion(calificación):
	resultado="Aprobado :)"
	if calificación<=70:
		resultado="Reprobado :("
	return resultado

print(evaluacion(int(calificacion_alumno)))






