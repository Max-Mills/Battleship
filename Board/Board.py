from Coordinates.ShipCoordinates import ShipCoordinates

class Board():
	def __init__(self, grid:list[ShipCoordinates]):
		self.__grid = grid

	def getGrid(self) -> list[ShipCoordinates]:
		return self.__grid
