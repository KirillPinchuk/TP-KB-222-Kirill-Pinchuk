import math

class Cylinder:
    def __init__(self, r=4, h=10):
        self.radius = r
        self.height = h

    def volume(self):
        return self.radius * self.height * math.pi

    def __str__(self):
        return str(self.volume())

cylinder = Cylinder(4, 10)
print(cylinder)