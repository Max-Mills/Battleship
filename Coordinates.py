from abc import ABC, abstractmethod

class ICoordinates(ABC):
	@abstractmethod
	def getCoordinates(self) -> tuple:
		pass

class xyCoordinates(ICoordinates):

	def __init__ (self, x: int, y: int):
		self.__points = str(x) + " " + str(y)

	def getCoordinates(self) -> str:
		return self.__points

class xyzCoordinates(ICoordinates):
	def __init__ (self, x: int, y: int, z: int):
		self.__points = str(x) + " " + str(y) + " " + str(z)

	def getCoordinates(self) -> str:
		return self.__points
