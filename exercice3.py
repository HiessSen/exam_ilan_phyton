print("Exercice 3 :")
def verifier_mot_de_passe(mot_de_passe):
    if len(mot_de_passe) < 8:
        return "Mot de passe invalide. Votre mot de passe doit contenir au moins 8 caractères"
    if "0" not in mot_de_passe and "1" not in mot_de_passe and "2" not in mot_de_passe and "3" not in mot_de_passe and "4" not in mot_de_passe and "5" not in mot_de_passe and "6" not in mot_de_passe and "7" not in mot_de_passe and "8" not in mot_de_passe and "9" not in mot_de_passe:
        return "Mot de passe invalide. Votre mot de passe doit contenir au moins un nombre"
    return "Mot de passe valide"
mot_de_passe_utilisateur = input("Entrer le mot de passe utilisateur: ")
print(verifier_mot_de_passe(mot_de_passe_utilisateur))