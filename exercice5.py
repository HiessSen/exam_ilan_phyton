def retirer_argent(montant_utilisateur):
    reponse = "Billets distribués :\n"
    billets_existants = [50, 20, 10]
    liste_billets = []
    if montant_utilisateur % 10 == 0:
        if montant_utilisateur <= 500:
            montant_restant = montant_utilisateur
            for billet in billets_existants:
                nombre_billets = 0
                while montant_restant >= billet:
                    nombre_billets += 1
                    montant_restant -= billet
                if nombre_billets > 0:
                    liste_billets.append((billet, nombre_billets))
            for billet_propose, nombre in liste_billets:
                if nombre == 1:
                    reponse += f"- {nombre} billet de {billet_propose}€\n"
                else:
                    reponse += f"- {nombre} billets de {billet_propose}€\n"
        else:
            reponse = "La somme est trop grosse. Vous ne pouvez pas retirer plus de 500 euros."
    else:
        reponse = "Vous devez demander une somme qui soit un multiple de 10."
    return reponse
montant_utilisateur = float(input("Veuillez choisir un montant à retirer: "))
print(retirer_argent(montant_utilisateur))