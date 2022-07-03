from Board.ITile import ITile
from IBoard import IBoard

class Board(IBoard):
	def __init__(self, grid:list[ITile]):
		self.__grid = grid

	def getGrid(self) -> list[ITile]:
		return self.__grid
