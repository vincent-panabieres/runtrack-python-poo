class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA/100)
    
    def afficher(self):
        print(f"Nom : {self.nom}")
        print(f"Prix HT : {self.prixHT} €")
        print(f"TVA : {self.TVA}%")
        print(f"Prix TTC : {self.calculerPrixTTC()} €")
    
    def modifierNom(self, nouveauNom):
        self.nom = nouveauNom
    
    def modifierPrix(self, nouveauPrixHT):
        self.prixHT = nouveauPrixHT
    
    def obtenirNom(self):
        return self.nom
    
    def obtenirPrix(self):
        return self.prixHT
    
    def obtenirTVA(self):
        return self.TVA
