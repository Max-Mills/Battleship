from Coordinates.ICoordinates import ICoordinates
from abc import ABC, abstractmethod

class ITile(ABC):

	@abstractmethod
	def setShipPartID(self, shipPartId: str):
		pass

	@abstractmethod
	def getCoordinates(self) -> ICoordinates:
		pass

	@abstractmethod
	def getShipPartID(self) -> str:
		pass

		