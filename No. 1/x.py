from a import A

class X(A):
    def __init__(self):
        self.__x = True
        A.__init__(self)
    
    def GetSelfX(self):
        return f"X is {self.__x}"