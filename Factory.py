from Coordinates import ICoordinates,xyCoordinates,xyzCoordinates
from Game import Game
from Tile import Tile, ITile
from Board import Board, IBoard
from Player import Player, IPlayer
from Ship import Ship, IShip, ShipType
from GameTypes import GameType
from Game import Game
from Settings import ISettings, BattleshipSettings

class Factory:

	def makeCoordinate(format: str, *args) -> ICoordinates:
		if format == GameType.Battleship.name:
			return xyCoordinates(args)
		elif format == GameType.Battlesub.name:
			return xyzCoordinates(args)
		else:
			print (f"{format} is unknown game type")

	def makeShipCoordinates(coordinates: ICoordinates, pieceID: str, pieceSection: int) -> ITile:
		return Tile(coordinates, pieceID, pieceSection)

	def makeBoard(grid:list[ITile]) -> IBoard:
		return Board(grid)

	def makePlayer(id: str, ships: list[IShip], playBoard: IBoard, trackingBoard: IBoard) -> IPlayer:
		return Player(id, ships, playBoard, trackingBoard)

	def makeShip(id: str, name: ShipType, hitParts: list[bool]) -> IShip:
		return Ship(id, name, hitParts)

	def makeGame(settings: ISettings) -> Game:
		return Game(settings)

	def makeSettings(format: str) -> ISettings:
		if format == GameType.Battleship.name:
			return BattleshipSettings(0)
		elif format == GameType.Battlesub.name:
			pass
		else:
			print (f"{format} is unknown game type")
			

