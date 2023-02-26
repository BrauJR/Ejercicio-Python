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

class VElectricos():
	def __init__(self):
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

miBici=BiciElectrica()
