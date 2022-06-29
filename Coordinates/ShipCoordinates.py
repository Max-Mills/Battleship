from Coordinates import Coordinates

class ShipCoordinates():

	def __init__(self, coordinates: Coordinates, shipPartID: str):
		self.__coordinates = coordinates
		self.__shipPartID = shipPartID

	def setCoordinates(self, coordinates: Coordinates):
		self.__coordinates = coordinates

	def setShipPartID(self, shipPartId: str):
		self.__shipPartID = shipPartId

	def getCoordinates(self) -> Coordinates:
		return self.__coordinates

	def getShipPartID(self) -> str:
		return self.__shipPartID

		