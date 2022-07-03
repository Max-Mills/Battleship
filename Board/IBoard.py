from Board.ITile import ITile
from abc import ABC,abstractmethod

class IBoard(ABC):

	@abstractmethod
	def getGrid(self) -> list[ITile]:
		pass