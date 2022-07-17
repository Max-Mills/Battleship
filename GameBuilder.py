from GameFactory import Factory
from GameTypes import GameType
from Ship import ShipType

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
	grid1 = []
	grid2 = []
	for i in range(0, measurements, 1):
		letter = chr(i + 65)
		for j in range(0, measurements, 1):
			coordinate = Factory.makeCoordinate(GameType.Battleship.name, letter, j+1)
			tile1 = Factory.makeTile(coordinate, None, None)
			tile2 = Factory.makeTile(coordinate, None, None)
			grid1.append(tile1)
			grid2.append(tile2)
	board1 = Factory.makeBoard(grid1)
	board2 = Factory.makeBoard(grid2)
	return board1, board2