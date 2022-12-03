class Circle():
    def __init__(self, radius: float = 1.0, color: str = "red") -> None:
        self.radius = radius
        self.color = color

    def getRadius(self) -> float:
        return self.radius
        
    def setRadius(self, radius: float) -> None:
        self.radius = radius

    def getColor(self) -> float:
        return self.color
        
    def setColor(self, color: str) -> None:
        self.color = color
    
    def toString(self) -> dict:
        return {"class": self.__class__.__name__, "radius": self.radius, "color": self.color}

    def getArea(self) -> float:
        return 22/7 * (self.radius ** 2)