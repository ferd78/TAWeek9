from circle import Circle

class Cylinder(Circle):
    def __init__(self, height: float = 1.0, radius: float = 1.0, color: str = "red") -> None:
        self.height = height
        super().__init__(radius, color)

    def getHeight(self) -> float:
        return self.height

    def setHeight(self, height: float) -> None:
        self.height = height

    def toString(self) -> dict:
        var = super().toString()
        var.update({"height": self.height})
        return var

    def getVolume(self) -> float:
        return self.getArea() * self.height
