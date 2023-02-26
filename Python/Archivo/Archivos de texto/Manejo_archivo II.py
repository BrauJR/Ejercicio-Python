from io import open 

#seek() A partir de 
#read() Hasta 

archivo_texto=open("Archivo2.txt","r+") #Lectura y escritura
#print(archivo_texto.readlines())
lista_texto=archivo_texto.readlines()
lista_texto[1]=" Esta line ha sido incluida desde el exterior\n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()

"""archivo_texto.seek(11)
print(archivo_texto.read(11))
print(archivo_texto.read())
"""