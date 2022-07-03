from ShipTypes import ShipTypes
from IShip import IShip

class Ship:

	def __init__(self, id: str, name: ShipTypes, hitParts: list[bool]):
		self.__id = id
		self.__name = name
		self.__hitParts = hitParts

	def getID(self):
		return self.__id
	
	def getName(self):
		return self.__name

	def getHitParts(self):
		return self.__hitParts

	def changeHitParts(self, shipPartIndex):
		self.__hitParts[shipPartIndex] = True
		print(f"{self.__name} has been hit")