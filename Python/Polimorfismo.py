class Coche():
	def desplazamiento(self):
		print("Me desplazo con 4 ruedas")

class Moto():
	def desplazamiento(self):
		print("Me desplazo con 2 ruedas")
		
class Camion():
	def desplazamiento(self):
		print("Me desplazo con 6 ruedas")


def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()

miVehiculo=Coche()
desplazamientoVehiculo(miVehiculo)