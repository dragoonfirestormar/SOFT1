class Rectangle:
    def __init__(self,x=0,y=0,w=0,l=0):
        self.x = x
        self.y = y
        self.w = w
        self.l = l
        pass

    def areaRect(self):
        return self.w*self.l

    pass


r = Rectangle()
r.x = 0
r.y = 0
r.w = 1
r.l = 2

print(r.areaRect())