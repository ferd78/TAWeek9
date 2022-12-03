from m import M
from b import B

class Z(B, M):
    def __init__(self):
        self.__z = True
        M.__init__(self)
        B.__init__(self)
    
    def GetSelfZ(self):
        return f"Z is {self.__z}"