from Player import IPlayer
from Settings import ISettings

class Game:

	def __init__(self, players: list[IPlayer] = [], settings: ISettings = ISettings):
		self.__players = players
		self.__settings = settings

	def getPlayers(self) -> list[IPlayer]:
		return self.__players

	def getSettings(self) -> ISettings:
		return self.__settings

	def addPlayer(self, players: list[IPlayer]):
		self.__players.append(players)

	def setSetting(self, settingName: str, settings: ISettings):
		self.__settings.getSetting(settingName)


	