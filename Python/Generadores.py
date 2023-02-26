"""
Generadores.
Estructuras que extraen valores de una función y se almacenan en objetos iterables
Se almacenan de uno en uno
Son más eficientes que las funciones tradicionales
_Sintaxis_
Def nombre():
    yield numeros
"""
"""
Función tradicional
def generaPare(limite):
	num = 1
	miLista=[]
	while num<limite:
		miLista.append(num*2)
		num+=1
	return miLista
print(generaPare(10))
"""

#Generador
def generaPare(limite):
	num = 1
	while num<limite:
		yield num*2
		num+=1
devuelvePares = generaPare(10)
"""for i in devuelvePares:
	print(i)
"""
print(next(devuelvePares)) #Imprime el primer valor
print("Aquí podría ir más código...")
print(next(devuelvePares))
print("Aquí podría ir más código...")
print(next(devuelvePares))
