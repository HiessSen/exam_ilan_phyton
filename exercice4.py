print("Exercice 4")
class Livre:
    def __init__(self, titre, auteur):
        self._titre = titre
        self._auteur = auteur
    @property
    def titre(self):
        return self._titre
    @property
    def auteur(self):
        return self._auteur
    def afficher_informations(self):
        reponse = f"Livre : {self._titre}, Auteur : {self._auteur}"
        return reponse
class LivreEmpruntable(Livre):
    def __init__(self, titre, auteur, disponible=False, retour=False):
        super().__init__(titre, auteur)
        self._disponible = disponible
        self._retour = retour
    @property
    def disponible(self):
        return self._disponible
    def afficher_informations(self):
        dispo = "Disponible\n" if self._disponible else "Indisponible\n"
        retour = "Le livre a été retourné" if self._retour else "Le livre a été emprunté"
        reponse = f"{super().afficher_informations()},\n"
        reponse += f"Disponibilité : {dispo}{retour}"
        return reponse
livre1 = Livre("1894", "George Orwell")
livre_emprunte1 = LivreEmpruntable("Le Petit Prince", "Antoine de Saint-Exupéry", True, False)
livre_emprunte2 = LivreEmpruntable("La possibilité d'une ile", "Michel Houellebecq", False, True)
print(livre1.afficher_informations())
print(livre_emprunte1.afficher_informations())
print(livre_emprunte2.afficher_informations())
