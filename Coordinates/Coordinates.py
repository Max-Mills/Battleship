class Coordinates:

	def __init__ (self, x: int, y: int):
		self.__x = x
		self.__y = y

	def getXY(self) -> tuple[int, int]:
		return self.__x, self.__y