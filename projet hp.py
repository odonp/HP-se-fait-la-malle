# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:20:07 2023

@author: LOUBNA.ZBITOU
"""

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
22/12/2023


ADRESSE GITHUB: 
https://github.com/odonp/HP-se-fait-la-malle

"""

#Moyen à la fin du programe de tout quitter ("si vous voulez partir, tapez ... " et ca quitte)
#affichage somme consigne 2)
#reduire les chaines de caractère pour la pep_8


# coding: utf-8

#import des modules

from random import randint


#définition des constantes




#définition des variables 
argent_rendu = []

dico_monnaie_illimitée = {\
  500 : 0 ,
  200:0 ,
  100:0 , 
  50:0 ,
  20:0 ,
  10:0 ,
  5:0  , 
  2:0   ,
  1:0 }

rendre = 0

#définition des fonctions dans l'ordre d'utlilisation

def affichage (argent_a_r, dico):
    '''
    Affiche le rendu de monnaie détaillé
    
    Entrée :
    Sortie : 
    
    '''
    if argent_a_r == 0 :
        print("Le commerçant n'a rien à vous rendre")
    for i in dico.keys():
            while argent_a_r >= i:
                dico[i] += 1
                argent_a_r -= i
    for i in dico.keys():
        if dico[i] > 0 :
            print(f"Le commerçant vous rend {dico[i]} coupure.s de {i} €")


def chez_fleury_et_bott(somme_a_rendre_chez_fleury_et_bott):
    '''
    Réalise le rendu de monnaie et une partie de l'IHM pour la boutique de fleury et bott

    Entrée : 

    Sortie : 
    
    '''
    argent_a_rendre_chez_fleury_et_bott = []
    somme_a_rendre_initiale_chez_fleury_et_bott = 0
    somme_a_rendre_initiale_chez_fleury_et_bott = somme_a_rendre_chez_fleury_et_bott
    dico_monnaie_illimitée = {\
        500 : 0 ,
        200:0 ,
        100:0 , 
        50:0 ,
        20:0 ,
        10:0 ,
        5:0  , 
        2:0   ,
        1:0 }

    somme_a_rendre_initiale__chez_fleury_et_bott = somme_a_rendre_chez_fleury_et_bott
    while somme_a_rendre_chez_fleury_et_bott > 0 :
        tiroir_caisse_chez_fleury_et_bott = [500,200,100,50,20,10,5,2,1]
        tiroir_caisse_chez_fleury_et_bott.append(somme_a_rendre_chez_fleury_et_bott)
        tiroir_caisse_chez_fleury_et_bott.sort(reverse = True)
        index = tiroir_caisse_chez_fleury_et_bott.index(somme_a_rendre_chez_fleury_et_bott)
        somme_a_rendre_chez_fleury_et_bott = somme_a_rendre_chez_fleury_et_bott - tiroir_caisse_chez_fleury_et_bott[index + 1]
        argent_a_rendre_chez_fleury_et_bott.append(tiroir_caisse_chez_fleury_et_bott[index+1])
    
    affichage(somme_a_rendre_initiale_chez_fleury_et_bott, dico_monnaie_illimitée)

def madame_guipure(montant):
    somme_obligatoire_chez_madame_guipure = (0, 17, 68, 231, 497, 842)
    tiroir_caisse_chez_madame_guipure = {
        200: 1,
        100: 3,
        50: 1,
        20: 1,
        10: 1,
        5: 1,
        2: 5
    }
    print("Rendu de monnaie :")
    for element in range(len(somme_obligatoire_chez_madame_guipure)):
        rendu = {}
        
        for espece in sorted(tiroir_caisse_chez_madame_guipure.keys(), reverse=True):
            while montant >= espece and tiroir_caisse_chez_madame_guipure[espece] > 0:
                montant -= espece
                rendu[espece] = rendu.get(espece, 0) + 1
                tiroir_caisse_chez_madame_guipure[espece] -= 1

        for espece, quantite in rendu.items():
            
            print(f"{quantite} coupure(s) de {espece} €")
        # Vérifier s'il manque de l'argent à rendre
    if montant > 0:
        print(f"Il manque {montant} euro(s) dans le tiroir caisse.")

def Ollivander ():
    '''
    Fait le change, le calcul et une partie de l'IHM pour le magasin de Ollivander
    
    Entrée : 
    Sortie : 
    '''

    gallions = 0
    mornilles = 0
    noises = 0
    a_rendre = []
    monnaie_magique = ["Gallions","Mornilles", "Noises"]
    gallions = int(input("Combien de gallions dois-je rendre ? (Entrez une valeur)"))
    mornilles = int(input("Combien de mornilles dois-je rendre ? (Entrez une valeur) "))
    noises = int(input("Combien de noises dois-je rendre ? (Entrez une valeur) "))
    somme_en_noises = (gallions * 17 * 29) + (mornilles * 29) + noises
    gallions_a_rendre = somme_en_noises // (17*29)
    a_rendre.append(gallions_a_rendre)
    somme_en_noises -= gallions_a_rendre * (17*29)
    mornilles_a_rendre = somme_en_noises // 29
    a_rendre.append(mornilles_a_rendre)
    somme_en_noises -= mornilles_a_rendre * 29
    noises_a_rendre = somme_en_noises
    a_rendre.append(noises_a_rendre)
    
    for i in range (3):
        print(f"Ollivander vous rends {a_rendre[i]} {monnaie_magique[i]}")



def menu():
    '''
    Régie tout le programme en faisant appel aux fonctions
    Entré : 
    Sortie 
    '''
    reponse = input("Bonjour sorcier/e. Tu es sur le Chemin de traverse.\n\n- Si tu souhaites aller chez Fleury et Bott, librairie de sorciers 📚, tape 1 \n\n- Si tu souhaites aller chez Madame Guipure, magasin de prêt à porter pour mages et sorcier\es 🧥, tape 2 \n\n- Si tu souhaites aller chez Ollivander, fabricant de baguettes magiques 🧙, tape 3 \n\n- Si tu souhaites quitter le chemin de traverse 🏦, tape sur n'importe quel autre chiffre \n\nOù souhaites-tu aller ? ")   
    while reponse=='1' or reponse=='2' or reponse=='3' :  
        if reponse == '1':
            somme_obligatoire_chez_fleury_et_bott = (0, 60, 63, 231, 899)
            argent_a_rendre_librairie = int(input("\nVous êtes dans le magasin de Fleury et Bott📚.\n\nCombien doit-ont vous rendre ? (entrez un entier)"))
            print("\n")
            chez_fleury_et_bott(argent_a_rendre_librairie)
            print("\n")
            reponse_somme_obligatoire_fleury = input("La consigne obligeant, tapez 1 si vous voulez voir l'affichage des sommes à rendre obligatoires.\nSinon tapez n'importe quel nombre pour sortir de chez Fleury et Bott. ")
            if reponse_somme_obligatoire_fleury == '1':
                for elements in somme_obligatoire_chez_fleury_et_bott:
                    print(f"Rendu monnaie pour {elements}€")
                    chez_fleury_et_bott(elements)
                    print("\n")
        elif reponse == '2' :
            somme_obligatoire_madame_guipure = (0, 17, 68, 231, 497, 842)
            argent_a_rendre_guipure = int(input("\nVous êtes dans le magasin de Mme guipure 🧥.\n\nCombien doit-on vous rendre ? (entrez un entier)"))
            print("\n")
            madame_guipure(argent_a_rendre_guipure)
            print("\n")
            reponse_somme_obligatoire_guipure = input("La consigne obligeant, tapez 1 si vous voulez voir l'affichage des sommes à rendre obligatoires.\n Sinon tapez n'importe quel nombre pour sortir de chez Madame Guipure. ")
            if reponse_somme_obligatoire_guipure == '1':
                for elements_2 in somme_obligatoire_madame_guipure:
                    print(f"Rendu monnaie pour {elements_2}€")
                    madame_guipure(elements_2)
                    print("\n")
        else :
            somme_obligatoire_chez_ollivander = [{Gallions : 0 , Mornilles : 0 , Noises :0},{Gallions : 0, Mornilles : 0, Noises : 654},{Gallions : 0, Mornilles : 23, Noises : 78}, {Gallions : 2 , Mornilles : 11, Noises : 9}, {Gallions : 7 , Mornilles : 531 , Noises : 451}]
            print("\nVous êtes dans la boutique de Ollivander 🧙.")
            Ollivander()
            print("\n")
            reponse_somme_obligatoire_ollivander = input("La consigne obligeant, tapez 1 si vous voulez voir l'affichage des sommes à rendre obligatoires. Sinon tapez n'importe quel nombre pour sortir de chez Ollivander. ")
            if reponse_somme_obligatoire_ollivander == '1' : 
                for elements_3 in somme_obligatoire_chez_ollivander :
                    print(f"Rendu monnaie pour {elements_3}€")
                    Ollivander(elements_3)
                    print("\n")
        reponse = input("Te revoilà sur le Chemin de traverse !\n\nSi tu souhaites aller chez Fleury et Bott, librairie de sorcier, tape 1 \nSi tu souhaites aller chez Madame Guipure, magasin de prêt à porter pour mages et sorcier, tape 2 \nSi tu souhaites aller chez Ollivander, fabricant de baguettes magiques, tape 3 \nSi tu souhaites quitter le chemin de traverse,  \nOù souhaites-tu aller ? ")
    print("\nVous quittez le chemin de traverse 🏦, à bientôt 👋!")      

"""
PROGRAMME PRINCIPAL
"""

menu()
tuple_1 = (0, 0, 0)
a, b, c = tuple_1
monnaie_obligatoire_chez_ollivander = [{Gallions : 0 , Mornilles : 0 , Noises :0},{Gallions : 0, Mornilles : 0, Noises : 654},{Gallions : 0, Mornilles : 23, Noises : 78}, {Gallions : 2 , Mornilles : 11, Noises : 9}, {Gallions : 7 , Mornilles : 531 , Noises : 451}]

menu()
tuple_1 = (0, 0, 0)
a, b, c = tuple_1
monnaie_obligatoire_chez_ollivander = [{Gallions : 0 , Mornilles : 0 , Noises :0},{Gallions : 0, Mornilles : 0, Noises : 654},{Gallions : 0, Mornilles : 23, Noises : 78}, {Gallions : 2 , Mornilles : 11, Noises : 9}, {Gallions : 7 , Mornilles : 531 , Noises : 451}]
