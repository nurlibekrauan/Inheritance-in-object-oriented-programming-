# 20. Наследование в объектно-ориентированном программировании |
# ООП Python
class Geom:
    name = "Geom"

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    name = "Line"
    def draw(self):
        print("Рисование линии")


class React(Geom):
    def draw(self):
        print("Рисование прямоугольника")


l = Line()
r = React()
g = Geom()
g.set_coords(0,0,0,0)
l.set_coords(1, 1, 2, 2)
r.set_coords(1, 1, 2, 2)
print(l.__dict__)
print(l.x1)
print(r.__dict__)
print(l.name)
print(r.name)