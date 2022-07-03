from Ship.IShip import IShip
from Board.IBoard import IBoard
from IPlayer import IPlayer

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


