from ICoordinates import ICoordinates

class ShipCoordinates():

	def __init__(self, coordinates: ICoordinates, shipPartID: str):
		self.__coordinates = coordinates
		self.__shipPartID = shipPartID

	def setShipPartID(self, shipPartId: str):
		self.__shipPartID = shipPartId

	def getCoordinates(self) -> ICoordinates:
		return self.__coordinates

	def getShipPartID(self) -> str:
		return self.__shipPartID

		