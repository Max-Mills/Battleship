from abc import ABC, abstractmethod
from Ship import IShip
from Board import IBoard
from Tile import ITile
from PlayerSystem import placeShip, printBoard, attemptHit, damageShip

class IPlayer(ABC):
	@abstractmethod
	def getID(self) -> str:
		pass

	@abstractmethod
	def getShips(self) -> list[IShip]:
		pass

	@abstractmethod
	def getPlayBoard(self) -> IBoard:
		pass

	@abstractmethod
	def getTrackingBoad(self) -> IBoard:
		pass

	@abstractmethod
	def setID(self, id: str):
		pass
	
	@abstractmethod
	def setShips(self, ships: list[IShip]):
		pass

	@abstractmethod
	def setPlayBoard(self, playBoard: IBoard):
		pass

	@abstractmethod
	def setTrackingBoard(self, trackingBoard: IBoard):
		pass

	@abstractmethod
	def placeShip(self, coords: str, ship: str, directon: str):
		pass

	@abstractmethod
	def printBoard(self):
		pass

	@abstractmethod
	def attemptHit(self, opponentTile: ITile) -> str:
		pass

	@abstractmethod
	def damageShip(self, pieceID: str):
		pass

class Player(IPlayer):

	def __init__(self, id: str, ships: list[IShip], playBoard: IBoard, trackingBoard: IBoard):
		self.__id = id
		self.__ships = ships
		self.__playBoard = playBoard
		self.__trackingBoard = trackingBoard

	def getID(self) -> str:
		return self.__id

	def getShips(self) -> list[IShip]:
		return self.__ships

	def getPlayBoard(self) -> IBoard:
		return self.__playBoard

	def getTrackingBoad(self) -> IBoard:
		return self.__trackingBoard

	def setID(self, id: str):
		self.__id = id
	
	def setShips(self, ships: list[IShip]):
		self.__ships = ships

	def setPlayBoard(self, playBoard: IBoard):
		self.__playBoard = playBoard

	def setTrackingBoard(self, trackingBoard: IBoard):
		self.__trackingBoard = trackingBoard

	def printBoard(self):
		printBoard(self.getID(), self.getTrackingBoad(), self.getPlayBoard())

	def placeShip(self, coords: str, ship: str, directon: str):
		placeShip(coords, ship, self.getPlayBoard(), directon)

	def attemptHit(self, opponentTile: ITile) -> str:
		return attemptHit(self.getTrackingBoad(), opponentTile)

	def damageShip(self, pieceID: str):
		damageShip(self.getShips(), pieceID)

		