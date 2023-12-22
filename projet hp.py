# -*- coding: utf-8 -*-

"""
Harry Potter se fait la malle

REGLES:
Bienvenue sur le chemin de traverse, vous incarnez un sorcier qui souhaite faire ses courses de fournitures scolaires avant d'intégrer l'école de Poudlard.

AUTEURS:
Valentine TAUDON-JARIES
Odon PROUILLE
Loubna ZBITOU

LICENCE:
Aucune

VERSION:
Finale

DATE DE DERNIERE REVISION:
22/12/2023

ADRESSE GITHUB: 
https://github.com/odonp/HP-se-fait-la-malle

# coding: utf-8

#import des modules
from random import randint

#définition des constantes
monnaie_magique = ["gallions","mornilles", "noises"]

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

#définition des fonctions 

def affichage (argent_a_rendre_fonction, dico):
    '''
    Affiche le rendu de monnaie détaillé 
        
    Entrée : Argent de monnaie à rendre brute
    Sortie : Affichage du rendu de monnaie 
    '''
    if argent_a_rendre_fonction == 0 :
        print("Le commerçant n'a rien à vous rendre")
    for i in dico.keys():
            while argent_a_rendre_fonction >= i:
                dico[i] += 1
                argent_a_rendre_fonction -= i
    for i in dico.keys():
        if dico[i] > 0 :
            print(f"Le commerçant vous rend {dico[i]} coupure.s de {i} €")

def chez_fleury_et_bott(somme_a_rendre_chez_fleury_et_bott):        
    '''
    Rend la monnaie avec le moins de billets possibles pour la boutique Chez Fleury et Bott à l'aide d'un tiroir caisse illimité 
    
    Entrée : Somme d'argent à rendre (Argent obligatoire ou argent choisi par l'utilisateur)
    Sortie : Somme d'argent rendu par Chez Fleury et Bott 
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
    '''
    Rend la monnaie avec le moins de billets possibles pour la boutique Madame Guipure à l'aide d'un tiroir caisse limité et indique éventuellement si le rendu de monnaie est incomplet avec combien d'argent il sera impossible de rendre
  
    Entrée : Somme d'argent à rendre (Argent obligatoire ou argent choisi par l'utilisateur)
    Sortie : Somme d'argent rendu par Madame Guipure
    '''
    #Création d'un dictionnaire tiroir caisse limité
    tiroir_caisse_chez_madame_guipure = {
        200: 1,
        100: 3,
        50: 1,
        20: 1,
        10: 1,
        5: 1,
        2: 5
    }
    rendu = {}
    #Trier toutes les clés du tiroir caisse limité par ordre décroissanr
    for espece in sorted(tiroir_caisse_chez_madame_guipure.keys(), reverse=True):
        while montant >= espece and tiroir_caisse_chez_madame_guipure[espece] > 0:
            montant -= espece
            if espece in rendu:
                rendu[espece] += 1
            else:
                rendu[espece] = 1
            tiroir_caisse_chez_madame_guipure[espece] -= 1

    for espece, quantite in rendu.items():
        print(f"{quantite} coupure(s) de {espece} €")
    # Vérifier s'il manque de l'argent à rendre
    if montant > 0:
        print(f"Désolé, il manque {montant} euro(s) dans le tiroir caisse.")

def ollivander (gallions1, mornilles1, noises1):
    '''
    Réalise la conversion pour rendre le moins de pièces possibles en monnaie magique (gallions, noises et mornilles)
        
    Entrée : Nombre de gallions, nombre de mornilles et nombre de noises (Argent obligatoire ou argent choisi par l'utilisateur) des entiers 
    Sortie : Minimun de pièces possible, sous forme de liste car résultat traité par une autre fonction après
    '''
    a_rendre = []
    monnaie_magique = ["gallions","mornilles", "noises"]
    # Tranformation de toute la monnaie en noises
    somme_en_noises = (gallions1 * 17 * 29) + (mornilles1 * 29) + noises1
    gallions_a_rendre = somme_en_noises // (17*29)
    a_rendre.append(gallions_a_rendre)
    somme_en_noises -= gallions_a_rendre * (17*29)
    mornilles_a_rendre = somme_en_noises // 29
    a_rendre.append(mornilles_a_rendre)
    somme_en_noises -= mornilles_a_rendre * 29
    noises_a_rendre = somme_en_noises
    a_rendre.append(noises_a_rendre)
    return a_rendre
    
def affichage_ollivander(nbre_entier_num1, nbre_entier_num2, nbre_entier_num3):
    '''
    Affiche les valeurs de gallions, mornilles et noises que Ollivander rend
    
    Entrée : Des nombres entiers
    Sortie : Des chaines de caractères
    '''
    valeurs_rendues_fonction = ollivander(nbre_entier_num1, nbre_entier_num2, nbre_entier_num3)
    for i in range (3):
        print(f"Ollivander vous rends {valeurs_rendues_fonction[i]} {monnaie_magique[i]}")

def menu():
    '''
    Régie tout le programme en faisant appel aux fonctions
    '''
    reponse = input("\nBonjour sorcier/n. Tu es sur le Chemin de traverse.\n\n- Si tu souhaites aller chez Fleury et Bott, librairie de sorciers 📚, tape 1 \n\n- Si tu souhaites aller chez Madame Guipure, magasin de prêt à porter pour mages et sorcier\es 🧥, tape 2 \n\n- Si tu souhaites aller chez ollivander, fabricant de baguettes magiques 🧙, tape 3 \n\n- Si tu souhaites quitter le chemin de traverse 🏦, tape sur n'importe quel autre chiffre \n\nOù souhaites-tu aller ? ")   
    while reponse=='1' or reponse=='2' or reponse=='3' :  
        if reponse == '1':
            print("\nVous êtes dans le magasin de Fleury et Bott📚.")
            #affichage des sommes obligatoires 
            print("\nAffichage des résultats obligatoires\n")
            somme_obligatoire_chez_fleury_et_bott = (0, 60, 63, 231, 899)
            for elements in somme_obligatoire_chez_fleury_et_bott:
                    print(f"Rendu monnaie pour {elements}€")
                    # Appel de la fonction Chez Fleury et Bott
                    chez_fleury_et_bott(elements)
                    print("\n")
            reponse_menu_fleuryetbott = input("\nSi vous voulez entrer des valeurs manuellement, tapez 6. \nSinon, pour quitter le magasin et retourner au chemin de traverse, tapez n'importe quel nombre ou caractère")        
            if reponse_menu_fleuryetbott == '6':
                argent_a_rendre_librairie = int(input("\nCombien doit-ont vous rendre ? (entrez un entier)  "))
                print("\n")
                chez_fleury_et_bott(argent_a_rendre_librairie)
                print("\n")      
        elif reponse == '2' :
            somme_obligatoire_madame_guipure = (0, 17, 68, 231, 497, 842)
            print("\nVous êtes dans le magasin de Mme guipure 🧥.\n")
            print("\nAffichage des résultats obligatoires\n")
            for elements_somme_obligatoire_guipure in somme_obligatoire_madame_guipure:
                    print(f"Rendu monnaie pour {elements_somme_obligatoire_guipure}€")
                    # Appel de la fonction Madame Guipure
                    madame_guipure(elements_somme_obligatoire_guipure)
                    print("\n")
            reponse_menu_guipure = input("\nSi vous voulez entrer des valeurs manuellement, tapez 8. \nSinon, pour quitter le magasin et retourner au chemin de traverse, tapez n'importe quel nombre ou caractère. ")        
            if reponse_menu_guipure == '8':
                argent_a_rendre_guipure = int(input("\nCombien doit-on vous rendre ? (entrez un entier)"  ))
                print("\n")
                madame_guipure(argent_a_rendre_guipure)
                print("\n")
        else :
            print("\nVous êtes dans la boutique de ollivander 🧙.\n")
            somme_obligatoire_chez_ollivander = [
            {'gallions': 0, 'mornilles': 0, 'noises': 0},
            {'gallions': 0, 'mornilles': 0, 'noises': 654},
            {'gallions': 0, 'mornilles': 23, 'noises': 78},
            {'gallions': 2, 'mornilles': 11, 'noises': 9},
            {'gallions': 7, 'mornilles': 531, 'noises': 451}
        ]
            # Affichage des résultats obligatoires
            print("Affichage des résultats obligatoires:\n")
            for elements_dans_la_liste_obligatoire_ollivander in somme_obligatoire_chez_ollivander:
                gallions_rendu_obligatoire = elements_dans_la_liste_obligatoire_ollivander['gallions']
                mornilles_rendu_obligatoire = elements_dans_la_liste_obligatoire_ollivander['mornilles']
                noises_rendu_obligatoire = elements_dans_la_liste_obligatoire_ollivander['noises']
                print(f"\nRendu de monnaie pour Gallions: {gallions_rendu_obligatoire}, Mornilles: {mornilles_rendu_obligatoire}, Noises: {noises_rendu_obligatoire}")
                # Appel de la fonction Ollivander
                affichage_ollivander(gallions_rendu_obligatoire, mornilles_rendu_obligatoire, noises_rendu_obligatoire)         
            #Entrée manuelle des valeurs
            reponse_menu_ollivander = input("\nSi vous voulez entrer des valeurs manuellement, tapez 7. \nSinon, pour quitter le magasin et retourner au chemin de traverse, tapez n'importe quel nombre ou caractère")
            if reponse_menu_ollivander == '7':
                gallions = int(input("Combien de gallions dois-je rendre ? (Entrez une valeur)"  ))
                mornilles = int(input("Combien de mornilles dois-je rendre ? (Entrez une valeur) "  ))
                noises = int(input("Combien de noises dois-je rendre ? (Entrez une valeur) "  ))
                affichage_ollivander(gallions, mornilles, noises)
            else :
                print("vous quittez le magasin d'Ollivander")     
        reponse = input("\nTe revoilà sur le Chemin de traverse !\n\nSi tu souhaites aller chez Fleury et Bott, librairie de sorcier, tape 1 \nSi tu souhaites aller chez Madame Guipure, magasin de prêt à porter pour mages et sorcier, tape 2 \nSi tu souhaites aller chez ollivander, fabricant de baguettes magiques, tape 3 \nSi tu souhaites quitter le chemin de traverse, tape sur n'importe quel autre chiffre \n \nOù souhaites-tu aller ? ")
    print("\nVous quittez le chemin de traverse 🏦, à bientôt 👋!")      

"""
PROGRAMME PRINCIPAL
Appel de la fonction menu qui permet d'entrer sur le chemin de traverse et d'aller dans différentes boutiques
"""

menu()
