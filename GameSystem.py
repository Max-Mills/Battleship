from Factory import Factory
from Ship import IShip, ShipType

def startGame():
	gameSettings()

def gameSettings():
	print("Welcome to Battleship\n Choose your Gametype: 2D or 3D")
	coordinatesType="3D"
	print("How many tiles will each dimension be:\n")
	dimmensionNum=10
	playerNames = []
	playerNum = 1
	print("Enter the names of the players")
	while playerNum <= 2:
		name = input(f"Enter the name for Player {playerNum}: \n")
		playerNames.append(name)
		playerNum += 1
	setupGame(playerNames)

def setupGame(playerNames):
	game = Factory.makeGame()
	for player in playerNames:
		ships: list[IShip] = []
		for sType in ShipType:
			id = player + sType.name
			hitParts: list[bool] = []
			for _ in range(0, sType.value, 1):
				hitParts.append(False)
			ship: IShip = Factory.makeShip()
			ship(id, sType.name, hitParts)
			ships.append(ship)
		playerObject = Factory.makePlayer()
		playerObject()
		game.addPlayer(playerObject)
