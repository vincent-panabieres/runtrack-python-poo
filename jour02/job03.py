class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()
        else:
            print("Le nombre de crédits ajouté doit être supérieur à zéro.")

    def student_info(self):
        print("Nom : ", self.__nom)
        print("Prénom : ", self.__prenom)
        print("Identifiant étudiant : ", self.__num_etudiant)
        print("Niveau : ", self.__level)