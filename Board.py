from Tile import ITile
from abc import ABC,abstractmethod

class IBoard(ABC):
	@abstractmethod
	def getGrid(self) -> list[ITile]:
		pass

class Board(IBoard):
	def __init__(self, grid:list[ITile]):
		self.__grid = grid

	def getGrid(self) -> list[ITile]:
		return self.__grid
