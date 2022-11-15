import math

def main():
    radius1_inp, radius2_inp = input("Enter R : ").split()
    radius1 = Spherical(int(radius1_inp))
    print(type(radius1))
    print(dir(radius1))
    print(radius1)
    radius1.changeR(int(radius2_inp))
    print(radius1)

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


if __name__ == "__main__":
    main()
