from io import open 


archivo_texto=open("Archivo.txt","a")
archivo_texto.write("\nEsta es la tercera línea")
archivo_texto.close()




"""
MODO LECTURA EN FORMA DE LISTA
lineas_texto=archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto)
"""

"""
MODO LECTURA
texto=archivo_texto.read()
archivo_texto.close()
print(texto)
"""

"""
MODO ESCRITURA
archivo_texto=open("Archivo.txt","w")
frase="Que cool está esto\nEs más fácil que en java"
archivo_texto.write(frase)
archivo_texto.close()
"""

