from Factory import Factory
from Game import Game
from Ship import ShipType
from Settings import OptionsBattleshipSettings
from GameTypes import GameType
from Tile import Tile

def startGame():
	playerNames, settings = gameSettings()
	game = Factory.makeGame(settings)
	setupGame(playerNames, game)
	printBoards(game)

def testGameSettings():
	settings = Factory.makeSettings("Battleship")
	settings.setSetting(OptionsBattleshipSettings.Measurements.name, "10")
	playerNames = []
	playerNames.append("max")
	playerNames.append("samara")
	return playerNames, settings


def gameSettings():
	gameType = input("Welcome to Battleship\n Choose your Gametype:\n")
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
			shipCoords = Factory.makeShipCoordinates(coordinate, None, None)
			grid.append(shipCoords)
	board = Factory.makeBoard(grid)
	return board, board

def printBoards(game: Game):
	players = game.getPlayers()
	for p in players:
		boardString = p.getID() + ":  \n"
		grid = p.getPlayBoard().getGrid()
		row = '0'
		for t in grid:
			coords = t.getCoordinates().getCoordinates()
			if row != coords[0]:
				boardString = boardString + "\n"
				row = coords[0]
			boardString = boardString + "[" + str(coords) +"]"
		print(boardString)
