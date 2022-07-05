from abc import ABC, abstractmethod

class ICoordinates(ABC):
	@abstractmethod
	def getCoordinates(self) -> tuple:
		pass

class xyCoordinates(ICoordinates):

	def __init__ (self, xy: tuple):
		self.__points = str(xy[0]) + " " + str(xy[1])

	def getCoordinates(self) -> str:
		return self.__points

class xyzCoordinates(ICoordinates):
	def __init__ (self, xyz: tuple):
		self.__points = str(xyz[0]) + " " + str(xyz[1]) + " " + str(xyz[2])

	def getCoordinates(self) -> str:
		return self.__points
