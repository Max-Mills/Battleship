from abc import ABC, abstractmethod
from enum import Enum

class ISettings(ABC):

	@abstractmethod
	def getSetting() -> int:
		pass

	@abstractmethod
	def setSetting(setting: str, value: int):
		pass

class OptionsBattleshipSettings(Enum):
	Measurements = "__measurement"

class BattleshipSettings(ISettings):

	def __init__(self, measurement: int = 0):
		self.__measurement = measurement

	def setSetting(self, settingName: str, value: int):
		setattr(self, settingName, value)

	def getSetting(self, settingName: str) -> int:
		return getattr(self, settingName)
		

		



