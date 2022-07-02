from abc import ABC, abstractmethod

class ICoordinates(ABC):

	@abstractmethod
	def getCoordinates(self) -> tuple:
		pass