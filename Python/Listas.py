'''
FUNCIONES LISTAS
'''
mi_lista=["Abi", "Ana", "Cristhian", "Brau", 10, True]
mi_lista.append("Ricardo") #Agrega al  final 
mi_lista.insert(1, "Jhovay") #Agrega con posición
mi_lista.extend(["Leidy","Laura"]) #Agrega o concatena otra lista
mi_lista.remove(10) #Elimina un elemento
mi_lista.pop() #Elimina el último elemento de la lista

#Concatenar listas con el oprador "+"
mi_lista2=["Luis", "Jimmy"]
mi_lista3=mi_lista+mi_lista2

print(mi_lista[:]) #Porción de lista
print(mi_lista.index("Abi")) #Devueleve el índice del elemento
print("Ana" in mi_lista) #Busca si el elemnto se encuentra dentro de la lista TRUE/FALSE
print(mi_lista3)