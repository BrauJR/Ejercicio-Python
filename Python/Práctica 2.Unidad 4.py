from crypt.PublicKey import RSA #Se importa RSA de Crypto.PublicKey

llave = RSA.generate(2048) #Se crea la variable llave con la función RSA tomando como parámetros un número(cantidad de bites)

f = open("llaveprivada.pem", "w") #Se crea el archivo
f.write(llave.exportKey('PEM')) #Se escribe en el archivo
f.close #Se cierra el archivo
        

