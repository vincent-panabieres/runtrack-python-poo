import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print("Cercle de rayon", self.rayon)

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon

c1 = Cercle(4)
c2 = Cercle(7)

for c in [c1, c2]:
    c.afficherInfos()
    print("Circonférence :", c.circonference())
    print("Diamètre :", c.diametre())
    print("Aire :", c.aire())
    print("------------------------")
