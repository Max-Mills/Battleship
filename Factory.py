from Coordinates import ICoordinates,xyCoordinates,xyzCoordinates
from Game import Game
from Tile import Tile, ITile
from Board import Board, IBoard
from Player import Player, IPlayer
from Ship import Ship, IShip
from GameTypes import GameType
from Game import Game

class Factory:

	def makeCoordinate(format: GameType) -> ICoordinates:
		if format == GameType.Battleship:
			return xyCoordinates
		elif format == GameType.Battlesub:
			return xyzCoordinates
		else:
			print (f"{format} is unknown game type")

	def makeShipCoordinates() -> ITile:
		return Tile

	def makeBoard() -> IBoard:
		return Board

	def makePlayer() -> IPlayer:
		return Player

	def makeShip() -> IShip:
		return Ship

	def makeGame() -> Game:
		return Game

