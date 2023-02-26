"""
TUPLA
Listas inmutables(que no se pueden modificar después de su creación)
-Son más rápidas
-Menos espacio
-Formatean Strings
-Pueden utilizarse como claves en un diccionario
Sintaxis nombreTupla=(elem1, elem2, elem3...)
"""
mi_tupla_unitaria=("Brau",) #Tupla unitaria

mi_tupla=("Fati", "Aida")
mi_lista=["Morita", "Ema"]

mi_tupla1=tuple(mi_lista) #Convierte una lista a tupla
mi_lista1=list(mi_tupla) #Convierte una tupla a lista

print(mi_tupla1) #Imprime con paréntesis
print(mi_lista1) #Impirme con corchetes

print("Luis" in mi_tupla) #Busca si se encuentra
print(mi_tupla.count(3)) #Cuenta el número de veces que se encuentra el elemento
print(len(mi_tupla)) #Indica el número total de elemntos

"""
Desempaquetado de tuplas
"""
tupla=("Pedro", 23, "M", 2001)
nombre,edad,sexo,año_nac=tupla
print("Desempaquetado de tuplas")
print("Nombre: "+nombre)
print("Edad: "+str(edad))
print("Sexo: "+sexo)
print("Año de nacimiento: "+str (año_nac))

