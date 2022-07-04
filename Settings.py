from abc import ABC, abstractmethod

class ISettings(ABC):

	@abstractmethod
	def getSetting() -> int:
		pass

	@abstractmethod
	def setSetting(setting: str, value: int):
		pass

class BattleshipSettings(ISettings):

	def __init__(self, measurement: int):
		self.__measurement = measurement

	def setSetting(self, setting: str, value: int):
		if setting == "measurement":
			self.__measurement = value
		print(f"{setting} does not exist")

	def getSetting(self, setting: str) -> int:
		if setting == "measurement":
			return self.__measurement
		print(f"{setting} does not exist")
		




