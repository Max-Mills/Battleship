import string
from Tile import ITile
from abc import ABC,abstractmethod

class IBoard(ABC):
	@abstractmethod
	def getGrid(self) -> list[ITile]:
		pass

	@abstractmethod
	def printBoard(self) -> string:
		pass

class Board(IBoard):
	def __init__(self, grid:list[ITile]):
		self.__grid = grid

	def getGrid(self) -> list[ITile]:
		return self.__grid

	def printBoard(self):
		grid = self.getGrid()
		row = '0'
		boardString = ""
		for t in grid:
			coords = t.getCoordinates().getCoordinates()
			if row != coords[0]:
				boardString = boardString + "\n"
				row = coords[0]
			if t.getIsHit() == True:
				item = "X"
			elif t.getIsHit() == False:
				item = "O"
			elif t.getPieceID() != None:
				item = "/"
			else:
				item = " "
			boardString = boardString + "[" + item +"]"
		return boardString
		

