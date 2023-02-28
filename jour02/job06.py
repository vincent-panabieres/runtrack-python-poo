class Commande:
    def __init__(self, num_commande):
        self.__num_commande = num_commande
        self.__plats = {}
        self.__statut = "en cours"
    
    def ajouter_plat(self, nom_plat, prix_plat):
        self.__plats[nom_plat] = {"prix": prix_plat, "statut": "en cours"}
    
    def annuler_commande(self):
        self.__statut = "annulée"
        for plat in self.__plats.values():
            plat["statut"] = "annulé"
    
    def calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats.values() if plat["statut"] != "annulé")
        return total
    
    def afficher_commande(self):
        print("Commande n°", self.__num_commande)
        for nom_plat, plat in self.__plats.items():
            print(f"- {nom_plat} ({plat['statut']}) : {plat['prix']} €")
        total = self.calculer_total()
        print(f"Total : {total} € (TVA incluse : {self.calculer_tva()} €)")
    
    def calculer_tva(self):
        total = self.calculer_total()
        tva = total * 0.2
        return tva