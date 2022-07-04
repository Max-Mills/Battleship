from Coordinates import ICoordinates
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

	@abstractmethod
	def getIsHit(self):
		pass
	
	@abstractmethod
	def hitTile(self) -> bool:
		pass

	@abstractmethod
	def setPieceID(self, pieceID: str):
		pass

class Tile(ITile):
	def __init__(self, coordinates: ICoordinates, pieceID: str, pieceSection: int, isHit:bool = None):
		self.__coordinates = coordinates
		self.__pieceID = pieceID
		self.__pieceSection = pieceSection
		self.__isHit = isHit

	def getCoordinates(self) -> ICoordinates:
		return self.__coordinates

	def getPieceSection(self) -> int:
		return self.__pieceSection

	def getPieceID(self) -> str:
		return self.__pieceID

	def getIsHit(self):
		return self.__isHit
	
	def hitTile(self) -> bool:
		if self.__isHit != None:
			return None
		elif self.__pieceID != None:
			return True
		elif self.__pieceID == None:
			return False
		else:
			print("Something went wrong")

	def setPieceID(self, pieceID: str):
		self.__pieceID = pieceID
		