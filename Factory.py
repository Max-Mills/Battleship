from Coordinates.Coordinates import ICoordinates,xyCoordinates,xyzCoordinates
from Coordinates.ShipCoordinates import ShipCoordinates

class Factory():

	def makeCoordinate(format, x: int = -1, y: int = -1, z: int = -1) -> ICoordinates:
		if format == "2D":
			return xyCoordinates(x, y)
		elif format == "3D":
			return xyzCoordinates(x, y, z)
		else:
			print ("Format for makeCoordinate incorrect")

	def makeShipCoordinates(coordinate: ICoordinates, shipPart: str):
		return ShipCoordinates(coordinate, shipPart)
