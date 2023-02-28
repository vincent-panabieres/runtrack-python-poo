class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        return "Je m'appelle {} {}.".format(self.prenom, self.nom)

personne1 = Personne("Panabieres", "vincent")
print(personne1.SePresenter())

personne2 = Personne("allan", "lafrance")
print(personne2.SePresenter())

personne3 = Personne("abdou", "metidji")
print(personne3.SePresenter())
