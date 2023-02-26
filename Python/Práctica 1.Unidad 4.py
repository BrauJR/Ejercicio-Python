print("Tecnológico Nacional de México. Instituto Tecnológico de Puebla.")
print("Ingeniería en TICs. Matemáticas Discretas II.")
print("Unidad 4. Criptografía. Práctica 1. Cifrado Césas y RSA. 22 de Junio")
print("Jorge Braulio Romero Malcos")

abc = 'abcdefghijklmnopqrstuvwxyz'

def cifrar(cadena, clave):
    text_cifrado = ''
    for letra in cadena:
        suma = abc.find(letra) + clave
        modulo = int(suma) % len(abc)
        text_cifrado = text_cifrado + str(abc[modulo])

    return text_cifrado

def decifrar(cadena, clave):
    text_cifrado = ''
    for letra in cadena:
        suma = abc.find(letra) - clave
        modulo = int(suma) % len(abc)
        text_cifrado = text_cifrado + str(abc[modulo])

    return text_cifrado

def main():
    c = str(input('Cadena a cifrar: '))
    n = int(input('Clave numérica: '))
    print (cifrar(c,n))
    cc = str(input('Cadena a decifrar: '))
    cn = int(input('Clave numérica: '))
    print (decifrar(cc, cn))

if __name__ == '__main__':
	main()