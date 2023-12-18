"""
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
"""

# coding: utf-8

#import des modules

from random import randint


#définition des constantes




#définition des variables 
argent_rendu = []
dico1 = {\
  500 : 0 ,
  200:0 ,
  100:0 , 
  50:0 ,
  20:0 ,
  10:0 ,
  5:0  , 
  2:0   ,
  1:0 }


#définition des fonctions dans l'ordre d'utlilisation

def Chez_Fleury_et_Bott(argent_a_rendre):
    argent_rendu = []
    while argent_a_rendre > 0 :
        monnaie = [500,200,100,50,20,10,5,2,1]
        monnaie.append(argent_a_rendre)
        monnaie.sort(reverse = True)
        index = monnaie.index(argent_a_rendre)
        argent_a_rendre = argent_a_rendre - monnaie[index + 1]
        argent_rendu.append(monnaie[index+1])
    return argent_rendu


def Chez_Ollivander():
    a_rendre = []
    gallions = int(input('Combien de gallion(s) me devez-vous ? '))
    mornilles = int(input('Combien de mornille(s) me devez-vous ? '))
    noises = int(input('Combien de noise(s) me devez-vous ? '))
    somme = (gallions*17*29) + (mornilles*17) + noises
    while somme > 0 :
        if somme >= 493 :
            nbr_gallions = somme // (17*29)
            a_rendre.append(nbr_gallions)
            somme -= nbr_gallions  
        elif somme < 493 and somme >= 29 :
            nbr_mornilles = somme // 29
            a_rendre.append(nbr_mornilles)
            somme -= nbr_mornilles   
        else :
            nbr_noises = somme
            a_rendre.append(nbr_noises)
    return a_rendre


def menu():
    reponse = input("Tu es sur le Chemin de traverse.\nSi tu souhaites aller chez Chez Fleury et Bott, la libairie des sorciers, clique sur 1 \nSi tu souhaites aller chez Madame Guipure, prêt à porter pour mages et sorciers, clique sur 2 \nSi tu souhaites aller chez Ollivander, fabricant de baguettes magiques, clique sur 3 \nOù souhaites-tu aller ?  ")
    if reponse == '1':
        somme_obligatoire = (0, 60, 63, 231, 899)
        for chiffre in somme_obligatoire: 
            librairie = Chez_Fleury_et_Bott(chiffre)
            print(librairie)
    
    elif reponse == '2' :
        djdsj
    else :
        dsqjdsqd
    reponse = input("Tu es sur le Chemin de traverse.\nVeux-tu aller en 1,2 ou 3 ? ")

menu()



"""

#DEBUT DU PROGRAMME PRINCIPAL





"""


'''
idée du prof
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

entrée = input("Bonjour sorcier/e, vous entrez dans le chemin de traverse, prêt à acheter vos fournitures ? (répondez 'oui' ou 'non')")
if entrée == "oui" or entrée == "OUI" or entrée == "Oui" :
    livre = input("vous entrez Chez Fleury & Bott voulez vous achetez : Le Livre des sorts et enchantements, niveau 1 de Miranda Fauconnette et Histoire de la magie de Bathilda Tourdesac ? (répondez 'oui' ou 'non')")
    if livre == "oui" or livre == "OUI" or livre == "Oui" : 
        argent = int(input("Combien doit-ont vous rendre ? (entrez un entier)"))
        
        liste_rendu_monnaie = rendu_monnaie_illimitee(argent)
        
        for i in dico1.keys():
            while argent >= i:
                dico1[i] += 1
                argent -= i
        for i in dico1.keys():
            if dico1[i] > 0 :
                print(f"le vendeur vous rend {dico1[i]} coupure.s de {i}")  









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
