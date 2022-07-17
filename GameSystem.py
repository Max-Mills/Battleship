from GameFactory import Factory
from GameBuilder import build2DBoards, buildShips
from Settings import OptionsBattleshipSettings
from Game import Game
from Ship import Ship

def startGame():
	playerNames, settings = testGameSettings()
	game = Factory.makeGame(settings)
	setupGame(playerNames, game)
	gameLoop(game, playerNames)

def gameLoop(game: Game, playerNames: list):
	player1 = game.getPlayers()[0]
	player2 = game.getPlayers()[1]
	currentPlayer = player1
	otherPlayer = player2
	i = 0
	player2.placeShip("j6", "Patrol", "left")
	gameOver = False
	while gameOver == False:
		coords = input("What coords are you attempting to hit? example: A10\n")
		pieceid = currentPlayer.attemptHit(otherPlayer.getPlayBoard().getTile(coords))
		if pieceid != None:
			otherPlayer.damageShip(pieceid)
		printPlayerBoard(game, currentPlayer.getID())
		gameOver = checkGameOver(otherPlayer.getShips())

		if gameOver == True:
			print(f"{currentPlayer.getID()} has won!")
			break

		if currentPlayer == player1:
			currentPlayer = player2
			otherPlayer = player1
		else:
			currentPlayer = player1
			otherPlayer = player2
		i = i + 1

def checkGameOver(ships: list[Ship]):
	for s in ships:
		for hp in s.getHitParts():
			if hp == False:	
				return False		
	return True
	
			
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

def setupGame(playerNames: list, game: Game):
	for player in playerNames:
		ships = buildShips(player)
		board, board2 = build2DBoards(int(game.getSetting(OptionsBattleshipSettings.Measurements.name)))
		playerObject = Factory.makePlayer(player, ships, board, board2)
		game.addPlayer(playerObject)

def printPlayerBoard(game: Game, playerName: str):
	players = game.getPlayers()
	for p in players:
		if p.getID() == playerName:
			p.printBoard()
			return
	print(f"Player {playerName} not found")
	
