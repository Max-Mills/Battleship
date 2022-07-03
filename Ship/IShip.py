from abc import ABC, abstractmethod

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
	def changeHitParts(self, shipPartIndex):
		pass