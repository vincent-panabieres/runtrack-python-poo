class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
        
    def set_largeur(self, largeur):
        self.__largeur = largeur
        
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    longueur = property(get_longueur, set_longueur)
    largeur = property(get_largeur, set_largeur)

    self_rectangle = Rectangle(10, 5)
