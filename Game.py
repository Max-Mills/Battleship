from Player import IPlayer
from Settings import BattleshipSettings, ISettings

class Game:

	def __init__(self, settings: ISettings, players: list[IPlayer] = []):
		self.__settings = settings
		self.__players = players

	def getPlayers(self) -> list[IPlayer]:
		return self.__players

	def getSettings(self) -> ISettings:
		return self.__settings

	def getSetting(self, settingName: str):
		settings: BattleshipSettings = self.getSettings()
		return settings.getSetting(settingName)

	def addPlayer(self, player: IPlayer):
		self.__players.append(player)

	def setSetting(self, settingName: str):
		self.__settings.getSetting(settingName)


	