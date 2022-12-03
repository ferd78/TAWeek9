from x import X
from y import Y
from z import Z

class Object(X, Y, Z):
    def __init__(self):
        self.__Object = True
        X.__init__(self)
        Y.__init__(self)
        Z.__init__(self)
    
    def GetObject(self):
        return f"Object is {self.__Object}"