"""
upper()           Mayúsculas
lower()           Minúscula
capitalize()      Primera letra en mayúscula
count()           Cuenta las veces que aparece
find()            Representa la posición
isdigit()         Devuelve un booleano
isalum()          Comprueba si es alfanumérico
isalpha()         Comprueba si hay solo letras (No cuenta el espacio)
split()           Separa por palabras utilizando espacios
strip()           Borra espacios al principio o al final
replace()         Reemplaza
rfind()           Representa la posición desde atrás
"""

edad=input("Ingresa tu edad: ")
while(edad.isdigit()==False):
	print("Ingresa un valor numérico")
	edad=input("Ingrsa tu edad: ")
if (int(edad)<18):
	print("No puede pasar")
else:
	print("Puede pasar")