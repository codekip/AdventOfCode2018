import os

grid = [[0] * 1000, [0] * 1000]


class Rectangle:
    def __init__(self, claim):
        self.claim = claim
        self.all = claim.split()
        self.id = int(self.all[0][1:])
        self.left = int(self.all[2].split(",")[0])
        self.top = int(self.all[2].split(",")[1].split(":")[0])
        self.width = int(self.all[3].split("x")[0])
        self.height = int(self.all[3].split("x")[1])
        self.area = self.width * self.height

    def top_left(self):
        return (self.left, self.top)

    def top_right(self):
        return ((self.left + self.width), self.top)

    def bottom_right(self):
        return ((self.left + self.width), (self.top + self.height))

    def bottom_left(self):
        return (self.left, self.height + self.top)


def width(instruction):
    shp = Rectangle(instruction)
    return shp.width


def left(instruction):
    shp = Rectangle(instruction)
    return shp.left


def top(instruction):
    shp = Rectangle(instruction)
    return shp.top


def top_right(instruction):
    shp = Rectangle(instruction)
    return shp.top_right()


def bottom_right(instruction):
    shp = Rectangle(instruction)
    return shp.bottom_right()


def bottom_left(instruction):
    shp = Rectangle(instruction)
    return shp.bottom_left()


def area(instruction):
    shp = Rectangle(instruction)
    return shp.area


def top_left(instruction):
    shp = Rectangle(instruction)
    return shp.top_left()


def top_end(instruction):
    shp = Rectangle(instruction)
    return shp.top_end()


def id(instruction):
    shp = Rectangle(instruction)
    return shp.id


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        input = f.read().strip()


if __name__ == "__main__":
    main()
