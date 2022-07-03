from Coordinates.ICoordinates import ICoordinates
from ITile import ITile

class Tile(ITile):

	def __init__(self, coordinates: ICoordinates, pieceID: str, pieceSection: int, isHit:bool = None):
		self.__coordinates = coordinates
		self.__pieceID = pieceID
		self.__pieceSection = pieceSection
		self.__isHit = isHit

	def getCoordinates(self) -> ICoordinates:
		return self.__coordinates

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
		