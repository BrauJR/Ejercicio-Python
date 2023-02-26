"""
Crear un programa que indique el nivel de 
un alumno de acuerdo a su calificación en
la materia de POO. De la sig. manera:
<70   INSUFICIENTE
<80   SUFICIENTE
<90   BIEN
<100  NOTABLE
==100 EXCELENTE
"""
print("Calificaciones POO")
calificacion=int(input("Ingrese calificación del alumno: "))
if calificacion<70:
	print("INSUFICIENTE")
elif calificacion<80:
	print("SUFICIENTE")
elif calificacion<90:
	print("BIEN")
elif calificacion<100:
	print("NOTABLE")
else:
	print("EXCELENTE ")
#NOTA:Un "else" no puede ir sin su correspondiente "if"



