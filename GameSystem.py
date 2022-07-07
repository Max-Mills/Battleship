from Factory import Factory
from Ship import ShipType
from Settings import OptionsBattleshipSettings
from GameTypes import GameType
from Game import Game

def startGame():
	playerNames, settings = gameSettings()
	game = Factory.makeGame(settings)
	setupGame(playerNames, game)
	printBoards(game)
	game.getPlayers()[0].getPlayBoard().getGrid()[2].setPieceID(1234)
	print(game.getPlayers()[0].getPlayBoard().getGrid()[2].hitTile())

	printBoards(game)

def testGameSettings():
	settings = Factory.makeSettings("Battleship")
	settings.setSetting(OptionsBattleshipSettings.Measurements.name, "10")
	playerNames = []
	playerNames.append("max")
	playerNames.append("samara")
	return playerNames, settings


def gameSettings():
	gameType = input("Welcome to Battleship\n Choose your Gametype: \n - Battleship \n\n")
	settings = Factory.makeSettings(gameType)
	measurement = input("\nHow many tiles will each dimension be:\n")
	settings.setSetting(OptionsBattleshipSettings.Measurements.name, measurement)
	playerNames = []
	playerNum = 1
	print("\nEnter the names of the players\n")
	while playerNum <= 2:
		name = input(f"Enter the name for Player {playerNum}: \n")
		playerNames.append(name)
		playerNum += 1
	return playerNames, settings

def setupGame(playerNames, game):
	for player in playerNames:
		ships = buildShips(player)
		board, board2 = build2DBoards(int(game.getSetting(OptionsBattleshipSettings.Measurements.name)))
		playerObject = Factory.makePlayer(player, ships, board, board2)
		game.addPlayer(playerObject)

def buildShips(player):
	ships = []
	for sType in ShipType:
		id = player + sType.name
		hitParts: list[bool] = []
		for _ in range(0, sType.value, 1):
			hitParts.append(False)
		ship = Factory.makeShip(id, sType.name, hitParts)
		ships.append(ship)
	return ships

def build2DBoards(measurements: int):
	grid = []
	for i in range(0, measurements, 1):
		for j in range(0, measurements, 1):
			coordinate = Factory.makeCoordinate(GameType.Battleship.name, i, j)
			tile = Factory.makeTile(coordinate, None, None)
			grid.append(tile)
	board = Factory.makeBoard(grid)
	return board, board

def printBoards(game: Game):
	players = game.getPlayers()
	for p in players:
		playerString = p.getID() + ":  \n"
		grid = p.getPlayBoard().printBoard()
		print (playerString + grid)
