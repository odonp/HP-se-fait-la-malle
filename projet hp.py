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
https://github.com/odonp/HP-se-fait-la-malle

"""

#Moyen à la fin du programe de tout quitter ("si vous voulez partir, tapez ... " et ca quitte)


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



#définition des fonctions dans l'ordre d'utlilisation




def menu():
    '''
    Régie tout le programme en faisant appel aux fonctions
    Entré : 
    Sortie 
    '''
    reponse = input("Bonjour sorcier/e. Tu es sur le Chemin de traverse.\n\nSi tu souhaites aller chez Fleury et Bott, librairie de sorcier, tape 1 \nSi tu souhaites aller chez Madame Guipure, magasin de prêt à porter pour mages et sorcier, tape 2 \nSi tu souhaites aller chez Ollivander, fabricant de baguettes magiques, tape 3 \nOù souhaites-tu aller ? ")
    if reponse == '1':
        somme_obligatoire = (0, 60, 63, 231, 899)
        argent_a_rendre_librairie = int(input("\nVous êtes dans le magasin.\nCombien doit-ont vous rendre ? (entrez un entier)"))
        print("\n")
        chez_fleury_et_bott(argent_a_rendre_librairie)
        print("\n")
        reponse_somme_obligatoire_flury = input("La consigne obligeant, tapez 9 si vous voulez voir l'affichage des sommes à rendre obligatoires. Sinon tapez n'importe quel nombre pour sortir de chez Fleury et Bott. ")
        if reponse_somme_obligatoire_flury == '9':
            for elements in somme_obligatoire:
                print(f"Rendu monnaie pour {elements}€")
                chez_fleury_et_bott(elements)
                print("\n")
        else :
            reponse = input("Bonjour sorcier/e. Tu es de retour sur le Chemin de traverse.\nSi tu souhaites aller chez Fleury et Bott, librairie de sorcier, tape 1 \nSi tu souhaites aller chez Madame Guipure, magasin de prêt à porter pour mages et sorcier, tape 2 \nSi tu souhaites aller chez Ollivander, fabricant de baguettes magiques, tape 3 \nOù souhaites-tu aller ? ")

    elif reponse == '2' :
        Guipur()
    
    #Si on répond n'importe quoi ca fait quand meme ollivander
    elif reponse == '3':
        print(Ollivander())
    else :
        print("Merci d'entrer un nombre entier, compris entre 1 et 3 et correspondant au bon magasion du chemin de traverse")
        #Moyen de relancer le programme au menu 

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


def chez_fleury_et_bott(argent_a_rendre):
    '''
    Réalise le rendu de monnaie et une partie de l'IHM pour la boutique de fleury et bott

    Entrée : 

    Sortie : 
    
    
    '''
    argent_rendu = []
    argent_a_rendre2 = 0
    argent_a_rendre2 = argent_a_rendre
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
    
    argent_a_rendre2 = argent_a_rendre
    while argent_a_rendre > 0 :
        monnaie = [500,200,100,50,20,10,5,2,1]
        monnaie.append(argent_a_rendre)
        monnaie.sort(reverse = True)
        index = monnaie.index(argent_a_rendre)
        argent_a_rendre = argent_a_rendre - monnaie[index + 1]
        argent_rendu.append(monnaie[index+1])
    
    affichage(argent_a_rendre2, dico_monnaie_illimitée)
    


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
    paroles = ["Gallions","Mornilles", "Noises"]
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
        print(f"Je vous rends {a_rendre[i]} {paroles[i]}")




"""
PROGRAMME PRINCIPAL
"""

menu()
