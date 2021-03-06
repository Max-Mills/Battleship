from Tile import ITile
from Ship import IShip, ShipType
from Board import IBoard

def printBoard(id: str, trackingBoard: IBoard, playerBoard: IBoard):
	playerString = id + ":  \n"
	grid1 = trackingBoard.printBoard()
	grid2 = playerBoard.printBoard()
	print (playerString + "\n  Tracking Board: \n" + grid1 +"\n\n" + "  Player Board\n" + grid2 +"\n\n")

def placeShip(coords: str, ship: str, playerBoard: IBoard, direction: str) -> bool:
	gridLength = pow(len(playerBoard.getGrid()),0.5)
	shipSize=ShipType[ship].value
	coords = coords[0].capitalize() + coords[1:]
	direction = direction.upper()
	y = ord(coords[0]) - 64
	x = int(coords[1:])

	if not x >= 0 or not x <= gridLength or not y >= 0 or not y <= gridLength:
		print ("You are outside the range of the board")
		return

	if direction == "UP":
		tiles = checkIfPlacementValid(playerBoard, -1, "hor", shipSize, coords, y, gridLength)
	elif direction == "DOWN":
		tiles = checkIfPlacementValid(playerBoard, 1, "hor", shipSize, coords, y, gridLength)
	elif direction == "LEFT":
		tiles = checkIfPlacementValid(playerBoard, -1, "ver", shipSize, coords, x, gridLength)
	elif direction == "RIGHT":
		tiles = checkIfPlacementValid(playerBoard, 1, "ver", shipSize, coords, x, gridLength)
	else:
		print("invalid direction")
		return False
	
	if tiles == False:
		return False

	hp = 0
	for t in tiles:
		t.setPieceID(str(hp) + ship)
		hp = hp + 1

	return True


def checkIfPlacementValid(playerBoard: IBoard, posOrNeg: int, horOrVer: str, shipSize: int, coords: str, xOrY: int, gridLength: int):
	tiles: list[ITile] = []
	if not xOrY + (posOrNeg * shipSize) >= 0 or not xOrY + (posOrNeg * shipSize) <= gridLength:
		print("ship does not fit here")
		return False

	for _ in range(0, shipSize):
		tile = playerBoard.getTile(coords)
		tiles.append(tile)
		if tile.getPieceID() != None:
			print("ship is there")
			return False
		if horOrVer == "hor":
			coords=chr(ord(coords[0])+posOrNeg)+coords[1:]
		elif horOrVer == "ver":
			coords=coords[0]+str(int(coords[1:])+posOrNeg)
		else:
			print("Something went wrong")
			return False
	return tiles

def attemptHit(trackingBoard: IBoard, opponentTile: ITile) -> str:
	isHit = opponentTile.hitTile()
	if isHit == False:
		print("Miss")
		trackingBoard.getTile(opponentTile.getCoordinates()).setIsHit(False)
		return True
	elif isHit == True:
		print("Hit!")
		trackingBoard.getTile(opponentTile.getCoordinates()).setIsHit(True)
		return opponentTile.getPieceID()
	else:
		print("You've already shot here")
		return False
	return None

def damageShip(ships: list[IShip], pieceID: str):
	nameOfShip = pieceID[1:]
	for s in ships:
		if s.getName() == nameOfShip:
			s.changeHitParts(int(pieceID[0]))
			print("ship damaged")

		

		
