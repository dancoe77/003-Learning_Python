zz = "##############################################"
print(zz)

aa = "Problem #1"
bb = "Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line."
print(aa)
print(bb)
print(zz)

class Line:
    def __init__(self,coor1,coor2):
        pass
    def distance(self):
        pass
    def slope(self):
        pass
# Example Output

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())
print(zz)

cc = "Problem #2"
dd = "Fill in the class"
print(cc)
print(dd)
print(zz)

class Cylinder:
    def __init__(self,height=1,radius=1):
        pass
    def volume(self):
        pass
    def surface_area(self):
        pass
# Example Output
cylinder = Cylinder(2,3)
print(cylinder.volume())
print(cylinder.surface_area())