class Vehiculos():

	def __init__ (self,marca,modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ",self.marca,
			"\nModelo: ",self.modelo,
			"\nEn marcha: ",self.enmarcha,
			"\nAcelerando: ",self.acelera,
			"\nFrenando: ",self.frena)


class Furgoneta(Vehiculos):
	def carga(self, cargar):
		self.cargado=cargar
		if (self.cargado):
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"

class Moto(Vehiculos):
	hcaballito=""
	def caballito(self):
		self.hcaballito="Estoy haciendo el caballito"
	#Sobre escritura de método
	def estado(self):
		print("Marca: ",self.marca,
			"\nModelo: ",self.modelo,
			"\nEn marcha: ",self.enmarcha,
			"\nAcelerando: ",self.acelera,
			"\nFrenando: ",self.frena,
			"\n",self.hcaballito)

class VElectricos(Vehiculos):
	def __init__(self,marca,modelo):
		super().__init__(marca,modelo)
		self.autonomia=100

	def cargar(self):
		self.cargando=True

miMoto=Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

#Herencia múltiple
class BiciElectrica(VElectricos,Vehiculos):
	pass

miBici=BiciElectrica("Benoto", 334)







"""
#Super()
#is instance()
class Persona():
	def __init__(self,nombre,edad,lugar):
		self.nombre=nombre
		self.edad=edad
		self.lugar=lugar

	def descripcion(self):
		print("Nombre: ", self.nombre,
			"\nEdad: ", self.edad,
			"\nLugar de residencia: ",self.lugar)
	
class Empleado(Persona):
	def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,lugar_empleado):
		super().__init__(nombre_empleado,edad_empleado,lugar_empleado)
		self.salario=salario
		self.antiguedad=antiguedad

	def descripcion(self):
		super().descripcion()
		print("Salario: ",self.salario,
			"\nAntiguedad:",self.antiguedad)

Luis=Empleado(3400, 12, "Luis", 34, "Perú")
Luis.descripcion()

print(isinstance(Luis, Persona))
"""