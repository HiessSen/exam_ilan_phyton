print("Exercice 2 :")
# Je crée une liste vide
tableau = []
# je crée une variable "plus grand nombre que j'initialise à zéro"
plus_grand_nombre = 0
# Avec une boucle de 1 à 5, je demande à l'utilisateur de rentrer 5 nombres que j'ajoute au tableau précédemment créé
for i in range(5):
    tableau.append(int(input("Veuillez entrer un nombre")))
# Je parcoure les éléments du tableau
for element in tableau:
    # Je remplace "plus grand nombre"(initialement 0) par la valeur de l'élément actuel SI cet élément est supérieur à "plus grand nombre"
    plus_grand_nombre = element if element > plus_grand_nombre else plus_grand_nombre
print(f"Le plus grand nombre est {plus_grand_nombre}")