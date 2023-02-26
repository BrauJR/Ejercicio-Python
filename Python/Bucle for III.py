"""
for i in range(5):
	print(f"Mensaje {i}") #Funciones fe tipo f=FORMATO
"""
"""
         #inicio, final, paso
for i in range(5, 10, 2): #Comienza desde el 5 hasta el 9
	print(f"Mensaje {i}")
"""

valido=False
correo=input("Ingresa correo: ")
for i in range(len(correo)):
	if correo[i]=="@":
		valido=True
if valido:
	print("Correo correcto")
else:
	print("Correo incorrecto")
