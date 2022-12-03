from a import A
from b import B

class Y(A,B):
    def __init__(self):
        self.y = True
        A.__init__(self)
        B.__init__(self)

    def GetSelfY(self):
        return f"Y is {self.y}" 