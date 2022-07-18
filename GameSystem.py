from GameFactory import Factory
from GameBuilder import build2DBoards, buildShips
from Player import IPlayer
from Settings import OptionsBattleshipSettings
from Game import Game
from Ship import IShip
from copy import copy

def startGame():
	playerNames, settings = testGameSettings()
	game = Factory.makeGame(settings)
	setupGame(playerNames, game)
	selectPlacementShips(game.getPlayers())
	gameLoop(game)

def gameLoop(game: Game):
	player1 = game.getPlayers()[0]
	player2 = game.getPlayers()[1]
	currentPlayer = player1
	otherPlayer = player2
	i = 0
	
	gameOver = False
	while gameOver == False:
		pieceid = None
		while pieceid == None or pieceid == False:
			print("\n\n\n\n\n")
			printPlayerBoard(game, currentPlayer.getID())
			coords = input("What coords are you attempting to hit? example: A10\n")
			pieceid = currentPlayer.attemptHit(otherPlayer.getPlayBoard().getTile(coords))
		if pieceid != True:
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

def checkGameOver(ships: list[IShip]):
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
		ships: list[IShip] = buildShips(player)
		board, board2 = build2DBoards(int(game.getSetting(OptionsBattleshipSettings.Measurements.name)))
		playerObject = Factory.makePlayer(player, ships, board, board2)
		game.addPlayer(playerObject)
	

def selectPlacementShips(players: list[IPlayer]):
	for player in players:
		shipsToPlace=copy(player.getShips())
		print(f"\n\n\nPlayer {player.getID()} enter where you'd like to place your ships:\n")
		while len(shipsToPlace) != 0:
			print("You still have the following ships to place \n\n")
			for stp in shipsToPlace:
				print(stp.getName())
			shipName = input("\n\nEnter a ship name: \n")
			player.printBoard()
			locationToPlace = input("Enter the coordinates to place it: \n")
			direction= input("Enter the direction it will be placed: \n")

			i = 0
			shipPop = -1
			for stp in shipsToPlace:
				if stp.getName() == shipName:
					shipPop = i
					break
				i = i + 1

			if shipPop == -1:
				print("\n\n\nThat is not a ship you can place\n\n\n")
			elif player.placeShip(locationToPlace, shipName, direction) == True:
				shipsToPlace.pop(shipPop)
			else:
				print("\nTry again\n")

def printPlayerBoard(game: Game, playerName: str):
	players = game.getPlayers()
	for p in players:
		if p.getID() == playerName:
			p.printBoard()
			return
	print(f"Player {playerName} not found")
	
