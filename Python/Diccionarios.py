"""
Diccionarios
Asociación clave:valor
Es decir a cada valor se le asigna una clave única
"""
mi_diccionario={"Alemania":"Berlín","Francia":"París","Argentina":"Buenos Aires"}
mi_diccionario["Italia"]="Lisboa" #Agrega elementos al diccionario
mi_diccionario["Italia"]="Roma" #Modifica un elemento agregado
del mi_diccionario["Argentina"] #Elimina elementos

print(mi_diccionario["Alemania"]) #Busca por su clave 
print(mi_diccionario) #Imprime todo el diccionario

"""
MIX (Lista con diccionario)
"""
mi_lista=["Epaña","Francia", "Reino Unido", "Alemania"]
mi_diccionario1={mi_lista[0]:"Madrid", mi_lista[1]:"París", mi_lista[2]:"Londres", mi_lista[3]:"Berlín"}
print(mi_diccionario1["Francia"])

"""
MIX (Tupla con diccionario)
"""
mi_diccionario2={"Edad":32,"Nombre":"Messi","Champions":[2010,2011, 2013, 1015]}
print(mi_diccionario2["Champions"])

"""
MIX (diccionarios, diccionarios {Subdiccionario})
"""
mi_diccionario3={"Edad":32,"Nombre":"Messi","Champions":{"Temporada":[2010,2011, 2013, 1015]}}
print(mi_diccionario3.keys()) #Imprime claves
print(mi_diccionario3.values()) #Imprime contenido
print(len(mi_diccionario3)) #Longitud del diccionario
print(mi_diccionario3["Champions"])

