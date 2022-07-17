from Tile import ITile
from abc import ABC,abstractmethod

class IBoard(ABC):
	@abstractmethod
	def getGrid(self) -> list[ITile]:
		pass

	@abstractmethod
	def printBoard(self) -> str:
		pass

	@abstractmethod
	def getTile(self, coords: str) -> ITile:
		pass

class Board(IBoard):
	def __init__(self, grid:list[ITile]):
		self.__grid = grid

	def getGrid(self) -> list[ITile]:
		return self.__grid

	def getTile(self, coords: str) -> ITile:
		coords = coords[0].capitalize() + coords[1:]
		for t in self.__grid:
			if t.getCoordinates() == coords:
				return t

	def printBoard(self):
		grid = self.getGrid()
		gridLength = int(pow(len(grid),0.5))
		row = '0'
		boardString = "   "
		for i in range(0, gridLength):
			boardString = boardString + str(i + 1) + "  "
		for t in grid:
			coords = t.getCoordinates()
			if row != coords[0]:
				boardString = boardString + "\n" + coords[0] + " "
				row = coords[0]
			if t.getIsHit() == True:
				item = "X"
			elif t.getIsHit() == False:
				item = "O"
			elif t.getPieceID() != None:
				item = "/"
			else:
				item = " "
				#item = (ord(coords[0]) * gridLength) + int(coords[1])
			boardString = boardString + "[" + str(item) +"]"
		return boardString
		

