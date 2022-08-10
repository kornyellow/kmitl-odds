import math

class Spherical:
    def __init__(self,r):
        self.radius = r
    def changeR(self,Radius):
        self.radius = Radius
    def findVolume(self):
        return math.pi * self.radius * self.radius * self.radius * (4/3)
    def findArea(self):
        return math.pi * self.radius * self.radius * 4
    def __str__(self):
        ret = "Radius =" + str(int(self.radius))
        ret += " Volumn = " + str(self.findVolume())
        ret += " Area = " + str(self.findArea())
        return ret

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)

