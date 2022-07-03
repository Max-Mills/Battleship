from Coordinates.Coordinates import ICoordinates,xyCoordinates,xyzCoordinates
from Board.Tile import Tile, ITile
from Board.Board import Board, IBoard
from Player.Player import Player, IPlayer
from Ship.Ship import Ship, IShip, ShipTypes

class Factory:

	def makeCoordinate(format, x: int = -1, y: int = -1, z: int = -1) -> ICoordinates:
		if format == "2D":
			return xyCoordinates(x, y)
		elif format == "3D":
			return xyzCoordinates(x, y, z)
		else:
			print ("Format for makeCoordinate incorrect")

	def makeShipCoordinates(coordinate: ICoordinates, shipPart: str):
		return Tile(coordinate, shipPart)

	def makeBoard(grid: list[ITile]):
		return Board(grid)

	def makePlayer(id: str, ships: list[IShip], playBoard: IBoard, trackingBoard: IBoard):
		return Player(id, ships, playBoard, trackingBoard)

	def makeShip(id: str, name: ShipTypes, hitParts: list[bool]):
		return Ship(id, name, hitParts)

	##def makeGame():

