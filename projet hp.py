"""
idée du prof
"""
def rendu_fleury(a_rendre):
    monnaie = (500, 200, 100, 50, 20, 10, 5, 2, 1)
    rendu = []
    for liquide in monnaie:
        while liquide <= a_rendre:
            rendu.append(liquide)
            a_rendre -= liquide
    return rendu

def affichage(monnaie_a_rendre):
    print()
 """
 notre programme qui marche 
 """
entrée = input("Bonjour sorcier/e, vous entrez dans le chemin de traverse, prêt à acheter vos fournitures ? ")
if entrée == "oui" or entrée == "OUI" or entrée == "Oui" :
    livre = input("vous entré Chez Fleury & Bott voulez vous achetez : Le Livre des sorts et enchantements, niveau 1 de Miranda Fauconnette et Histoire de la magie de Bathilda Tourdesac ? ")
    if livre == "oui" or livre == "OUI" or livre == "Oui" : 
        argent = int(input("Combien doit-ont vous rendre ? "))
        argent_rendu = []
        while argent > 0 :
            monnaie = [500,200,100,50,20,10,5,2,1]
            monnaie.append(argent)
            monnaie.sort(reverse = True)
            index = monnaie.index(argent)
            argent = argent - monnaie[index + 1]
            argent_rendu.append(monnaie[index+1])
            print(argent_rendu)
    else : 
        livre = input("vous entré Chez Fleury & Bott voulez vous achetez : Le Livre des sorts et enchantements, niveau 1 de Miranda Fauconnette et Histoire de la magie de Bathilda Tourdesac ? ")
        magasin = input("Voulez vous continuer vos achat et achetez une cape ? ")
        if magasin == "oui" or magasin == "Oui" or magasin == "OUI" : 
            autre_magasin = input("Voulez vous terminez vos course par achetez une baguette ? ")
            if autre_magasin == "oui" or "Oui" or "OUI":
                Ors = int(input("Combien vaut 1 Gallion ?"))
                Gallion = Ors
                Mornille = Ors / 17
                Gallion = Mornille * 17
                Noises = Mornille / 29 
                Mornille = 29 * Noises

        else : 
            autre_magasin = input("Voulez vous terminez vos course par achetez une baguette ? ")
else:
    entrée = input("Ëtes vous sur ?, vous entré dans le chemin de traverse, pret à acheter vos fournitures ? ")
