"""
Método constructor(Sintaxis)
Encapsulamiento de variables(__)
"""
class Coche():

	def __init__(self):		
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enmarcha=False

	def arrancar(self, arrancamos):
		self.__enmarcha=arrancamos
		if(self.__enmarcha):
			return "El coche está en marcha"
		else:
			return "El coche está parado"

	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, 
		".Y un largo de ", self.__largoChasis)
	

miCoche=Coche() #Instancia de clase
print(miCoche.arrancar(True))
miCoche.estado()

print(".......A continuación se crea el segundo objeto........")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()

