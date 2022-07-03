from abc import ABC, abstractmethod
from Ship.IShip import IShip
from Board.IBoard import IBoard

class IPlayer(ABC):

	@abstractmethod
	def getID(self) -> str:
		pass

	@abstractmethod
	def getShips(self) -> list[IShip]:
		pass

	@abstractmethod
	def getPlayBoard(self) -> IBoard:
		pass

	@abstractmethod
	def getTrackingBoad(self) -> IBoard:
		pass

	@abstractmethod
	def setID(self, id: str):
		pass
	
	@abstractmethod
	def setShips(self, ships: list[IShip]):
		pass

	@abstractmethod
	def setPlayBoard(self, playBoard: IBoard):
		pass

	@abstractmethod
	def setTrackingBoard(self, trackingBoard: IBoard):
		pass