zz = "##############################################"
print(zz)

aa = "Problem #1"
bb = "Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line."
print(aa)
print(bb)
print(zz)

class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 +(y2-y1)**2)**0.5
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1) / (x2-x1)
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
        self.height = height
        self.radius = radius
    def volume(self):
        return self.height * 3.14 * (self.radius)**2
    def surface_area(self):
        top = 3.14 * (self.radius**2)
        return (2*top) + (2*3.14*self.radius*self.height)
# Example Output
cylinder = Cylinder(2,3)
print(cylinder.volume())
print(cylinder.surface_area())
print(zz)