from abc import ABC, abstractmethod
from ShipTypes import ShipType

class IShip(ABC):
	@abstractmethod
	def getID(self):
		pass
	
	@abstractmethod
	def getName(self):
		pass

	@abstractmethod
	def getHitParts(self):
		pass

	@abstractmethod
	def changeHitParts(self, shipPartIndex: int):
		pass

class Ship(IShip):
	def __init__(self, id: str, name: ShipType, hitParts: list[bool]):
		self.__id = id
		self.__name = name
		self.__hitParts = hitParts

	def getID(self):
		return self.__id
	
	def getName(self):
		return self.__name

	def getHitParts(self):
		return self.__hitParts

	def changeHitParts(self, shipPartIndex: int):
		self.__hitParts[shipPartIndex] = True