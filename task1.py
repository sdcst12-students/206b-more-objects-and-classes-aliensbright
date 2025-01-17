#!python3

""" def __init__(self,l=0,w=0,h=0):
        # note you will need to specify more input parameters
            self.length = l
            self.height = w
            self.width = h
            self.volume()
            self.surfaceArea()


    def volume(self):
        V = self.length * self.width * self.height
        if V == 0:
            V = None
        return V
    
    def surfaceArea(self):
        SA = self.length * self.width * 2 + self.width * self.height * 2 + self.length * self.height * 2
        if self.length == 0 or self.width == 0 or self.height == 0:
            SA = None
        return SA"""

class quadratic:
    a = 0
    b = 0
    c = 0
    dis = 0
    roots = []
    axis = 0
    x = 0
    y = 0
    vertexValues = []

    def __init__(self,a1=0,b1=0,c1=0):
        self.a = a1
        self.b = b1
        self.c = c1
        self.discriminant()
        self.hasRealRoots()
        self.isFactorable()
        self.calcRoots()
        self.axisOfSymmetry()
        self.vertex()

    def discriminant(self):
        self.dis = self.b ** 2 - 4 * self.a * self.c
        return self.dis
   
    def hasRealRoots(self):
        if self.dis < 0:
            return False
        else:
            return True

    def isFactorable(self):
        if self.dis < 0:
            return False
        elif (self.dis ** 0.5) % 1 == 0:
            return True
        else:
            return False
   
    def calcRoots(self):
        if self.hasRealRoots() == True:
            root1 = (-self.b - self.dis ** 0.5) / 2 / self.a
            root1 = round(root1,2)
            root2 = (-self.b + self.dis ** 0.5) / 2 / self.a
            root2 = round(root2,2)
            self.roots = [root1,root2]
        return self.roots
    
    def axisOfSymmetry(self):
        self.axis = (-1) * self.b / 2 / self.a
        print(self.axis)
        return self.axis

    def vertex(self):
        self.x = self.axis
        self.y = self.a * self.x ** 2 + self.b* self.x + self.c
        self.vertexValues = [self.x,self.y]
        print(self.vertexValues)
        return self.vertexValues





if __name__ == "__main__":
    q1 = quadratic(1,4,4)
    assert q1.isFactorable() == True
    assert q1.hasRealRoots() == True
    assert q1.discriminant() == 0
    assert q1.roots == [-2,-2]
    assert q1.axisOfSymmetry() == -2
    assert q1.vertex() == [-2,0]

    q2 = quadratic(1,1,-6)
    assert q2.isFactorable() == True
    assert q2.hasRealRoots() == True
    assert q2.discriminant() == 25
    assert q2.roots == [-3,2]
    assert q2.axisOfSymmetry() == -0.5
    assert q2.vertex() == [-0.5,-6.25]

    q3 = quadratic(1,1,10)
    assert q3.isFactorable() == False
    assert q3.hasRealRoots() == False
    assert q3.discriminant() == -39
    assert q3.roots == []
    assert q3.axisOfSymmetry() == -0.5

    q4 = quadratic(1,10,1)
    assert q4.isFactorable() == False
    assert q4.hasRealRoots() == True
    assert q4.discriminant() == 96
    assert q4.roots == [-9.90,-0.10]
    assert q4.axisOfSymmetry() == -5