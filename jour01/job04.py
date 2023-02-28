class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print("Les coordonnées du point sont ({}, {}).".format(self.x, self.y))
    
    def afficherX(self):
        print("La coordonnée x du point est {}.".format(self.x))
    
    def afficherY(self):
        print("La coordonnée y du point est {}.".format(self.y))
    
    def changerX(self, new_x):
        self.x = new_x
    
    def changerY(self, new_y):
        self.y = new_y

