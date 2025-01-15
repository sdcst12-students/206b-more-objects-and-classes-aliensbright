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
    des = 0
    roots = []
    axis = 0

    def __init__(self,a1=0,b1=0,c1=0):
        self.a = a1
        self.b = b1
        self.c = c1
        self.discriminant()
        self.hasRealRoots()
        self.isFactorable()
        self.calcRoots()

    def discriminant(self):
        self.des = self.b ** 2 - 4 * self.a * self.c
        # requires no positional arguments
        # will make use of class properties a,b and c
        # to determine the discriminant which is calculated as
        # b^2 - 4ac
        # return value should be a float type decimal
        return self.des
   
    def hasRealRoots(self):
        # requires no positional arguments
        # will make use of class properties a,b and c
        # to determine if the quadratic has real roots
        # defined when the discriminant is non negative
        # return value should be True or False
        if self.des < 0:
            return False
        else:
            return True

    def isFactorable(self):
        # requires no positional arguments
        # will make use of class properties a,b and c
        # to determine if the quadratic can be factored
        # quadratic can be factored if the discriminant is a perfect square
        # return value is True or False
        if self.des < 0:
            return False
        elif (self.des ** 0.5) % 1 == 0:
            return True
        else:
            return False
   
    def calcRoots(self):
        # requires no positional arguments
        # will make use of class properties a,b and c
        # to determine the roots of the quadratic if
        # the quadratic has real roots
        # should make use of the class methods:
        # self.hasRealRoots()
        # self.discriminant
        # method does not have a return value
        # but should store the values of the roots in the
        # list self.roots
        # list should be sorted in ascending order
        # roots should be rounded to 2 decimal places
        self.discriminant()
        if self.hasRealRoots() == True:
            root1 = (-self.b - self.des ** 0.5) / 2 / self.a
            root1 = round(root1,2)
            root2 = (-self.b + self.des ** 0.5) / 2 / self.a
            root2 = round(root2,2)
            self.roots = [root1,root2]
        return self.roots
    
    def axisOfSymmetry(self):
        # requires no positional arguments
        # will make use of class properties a,b and c
        # to determine the x value that is for the equation
        # of the axis of symmetry
        # should return the x value for the axis of symmetry
        if self.roots != []:
            r1 = self.roots[0]
            r2 = self.roots[1]
            distance = (r2 - r1) / 2
            self.axis = r1 + distance
        return self.axis

    def vertex(self):
        # requires no positional arguments
        # will make use of class properties a,b and c
        # to determine the x,y value of the vertex
        # should return the a list with the x and y coordinates of the vertex
        pass
        return





if __name__ == "__main__":
    q1 = quadratic(1,4,4)
    assert q1.isFactorable() == True
    assert q1.hasRealRoots() == True
    assert q1.discriminant() == 0
    assert q1.roots == [-2,-2]
    assert q1.axisOfSymmetry == -2
    #assert q1.vertex == [-2,0]

    q2 = quadratic(1,1,-6)
    assert q2.isFactorable() == True
    assert q2.hasRealRoots() == True
    assert q2.discriminant() == 25
    assert q2.roots == [-3,2]
    assert q2.axisOfSymmetry == -0.5
    #assert q2.vertex == [-0.5,-6.25]

    q3 = quadratic(1,1,10)
    assert q3.isFactorable() == False
    assert q3.hasRealRoots() == False
    assert q3.discriminant() == -39
    assert q3.roots == []
    assert q3.axisOfSymmetry == -0.5

    q4 = quadratic(1,10,1)
    assert q4.isFactorable() == False
    assert q4.hasRealRoots() == True
    assert q4.discriminant() == 96
    assert q4.roots == [-9.90,-0.10]
    assert q4.axisOfSymmetry == -2.5