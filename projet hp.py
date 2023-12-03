'''
Harry Potter se fait la malle


REGLES:




AUTEURS:
Valentine
Loubna
Odon

LICENCE:



VERSION:



DATE DE DERNIERE REVISION:



ADRESSE GITHUB: 


'''

# coding: utf-8

#import des modules

from random import randint


#définition des constantes




#définition des variables 
argent_rendu = []

#définitionn des fonctions dans l'ordre d'utlilisation

def rendu_monnaie_illimitee(argent_a_rendre):
    while argent_a_rendre > 0 :
        monnaie = [500,200,100,50,20,10,5,2,1]
        monnaie.append(argent_a_rendre)
        monnaie.sort(reverse = True)
        index = monnaie.index(argent_a_rendre)
        argent_a_rendre = argent_a_rendre - monnaie[index + 1]
        argent_rendu.append(monnaie[index+1])
    return argent_rendu





#DEBUT DU PROGRAMME PRINCIPAL





"""
idée du prof
"""

'''

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
'''
 
 
 
"""
notre programme qui marche 
"""

'''
#On est obligé d'avoir les oui ? Ca alourdit vraiment et ca multiplie les erreurs

entrée = input("Bonjour sorcier/e, vous entrez dans le chemin de traverse, prêt à acheter vos fournitures ? (répondez 'oui' ou 'non')")
if entrée == "oui" or entrée == "OUI" or entrée == "Oui" :
    livre = input("vous entrez Chez Fleury & Bott voulez vous achetez : Le Livre des sorts et enchantements, niveau 1 de Miranda Fauconnette et Histoire de la magie de Bathilda Tourdesac ? (répondez 'oui' ou 'non')")
    if livre == "oui" or livre == "OUI" or livre == "Oui" : 
        argent = int(input("Combien doit-ont vous rendre ? (entrez un entier)"))
        
        liste_rendu_monnaie = rendu_monnaie_illimitee(argent)
        print(liste_rendu_monnaie)
        for i in range(len(liste_rendu_monnaie)) :
            print(f"On vous rend {liste_rendu_monnaie[i]}")
'''











'''
entrée = input("Bonjour sorcier/e, vous entrez dans le chemin de traverse, prêt à acheter vos fournitures ? (répondez 'oui' ou 'non')")
if entrée == "oui" or entrée == "OUI" or entrée == "Oui" :
    livre = input("vous entré Chez Fleury & Bott voulez vous achetez : Le Livre des sorts et enchantements, niveau 1 de Miranda Fauconnette et Histoire de la magie de Bathilda Tourdesac ? (répondez 'oui' ou 'non')")
    if livre == "oui" or livre == "OUI" or livre == "Oui" : 
        argent = int(input("Combien doit-ont vous rendre ? (entrez un entier)"))
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
        livre = input("vous entré Chez Fleury & Bott voulez vous achetez : Le Livre des sorts et enchantements, niveau 1 de Miranda Fauconnette et Histoire de la magie de Bathilda Tourdesac ? (répondez 'oui' ou 'non')")
        magasin = input("Voulez vous continuer vos achat et achetez une cape ? ")
        if magasin == "oui" or magasin == "Oui" or magasin == "OUI" : 
            autre_magasin = input("Voulez vous terminez vos course par achetez une baguette ? (répondez 'oui' ou 'non')")
            if autre_magasin == "oui" or "Oui" or "OUI":
                Ors = int(input("Combien vaut 1 Gallion ?"))
                Gallion = Ors
                Mornille = Ors / 17
                Gallion = Mornille * 17
                Noises = Mornille / 29 
                Mornille = 29 * Noises

        else : 
            autre_magasin = input("Voulez vous terminez vos course par achetez une baguette ? (répondez 'oui' ou 'non')")
else:
    entrée = input("Ëtes vous sur ?, vous entré dans le chemin de traverse, pret à acheter vos fournitures ? (répondez 'oui' ou 'non')")
    '''

