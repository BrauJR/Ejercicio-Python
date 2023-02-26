"""
-continue.-Ignora la siguiente instrucción
-pass.-Devuelve un null
-else.-Se ejecuta siempre y cuando esté vacío
"""

"""
EJEMPLO 1
nombre ="Hola a todos"
contador = 0
for i in nombre:
	if i==" ":
		continue
	contador+=1
print(contador)
"""

"""
EJEMPLO 2
class MiClase:
	pass #Para implementar más tarde
"""

#EJEMPLO 3
email = input("Ingesa tu correo: ")
for i in email:
	if i=="@":
		arroba = True
		break;
else:
	arroba = False

print(arroba)


