from Coordinates import ICoordinates
from abc import ABC, abstractmethod

class ITile(ABC):
	@abstractmethod
	def getCoordinates(self) -> str:
		pass

	@abstractmethod
	def getPieceSection(self) -> int:
		pass

	@abstractmethod
	def getPieceID(self) -> str:
		pass

	@abstractmethod
	def getIsHit(self) -> bool:
		pass
	
	@abstractmethod
	def hitTile(self) -> bool:
		pass

	@abstractmethod
	def setPieceID(self, pieceID: str):
		pass

	@abstractmethod
	def setIsHit(self, bool: bool):
		pass
		

class Tile(ITile):
	def __init__(self, coordinates: ICoordinates, pieceID: str, pieceSection: int, isHit:bool = None):
		self.__coordinates = coordinates
		self.__pieceID = pieceID
		self.__pieceSection = pieceSection
		self.__isHit = isHit

	def getCoordinates(self) -> str:
		return self.__coordinates.getCoordinates()

	def getPieceSection(self) -> int:
		return self.__pieceSection

	def getPieceID(self) -> str:
		return self.__pieceID

	def getIsHit(self) -> bool:
		return self.__isHit

	def setIsHit(self, bool: bool):
		self.__isHit = bool
	
	def hitTile(self) -> bool:
		if self.__isHit != None:
			return None
		elif self.__pieceID != None:
			self.__isHit = True
			return True
		elif self.__pieceID == None:
			self.__isHit = False
			return False
		else:
			print("Something went wrong")

	def setPieceID(self, pieceID: str):
		self.__pieceID = pieceID
		