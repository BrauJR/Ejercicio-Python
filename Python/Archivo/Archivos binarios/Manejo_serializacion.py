import pickle

fichero=open("Lista_nombres","rb")
lista=pickle.load(fichero)
print(lista)

"""
lista_nombres=["Ana","Abi","Fati","Luis"]

fichero_binario=open("Lista_nombres","wb")

pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()

del(fichero_binario)
"""