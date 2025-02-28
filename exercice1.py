print("Exercice 1 :")
# Je demande à l'utilisateur d'entrer le montant total de ses achats
montant = float(input("Entrez le montant total de vos achats : "))
# Je crée une condition qui determine si la réduction de 10% doit être appliquée (si montant inferieur ou égal à 100, pas d remise. Sinon, remise de 10%)
if montant <= 100:
    reponse = f"Pas de remise. Montant à payer {montant}"
else:
    montant *= 0.9
    reponse = f"Remise de 10% appliquée. Montant à payer {montant}"
print(reponse)