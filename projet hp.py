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
    reponse = input("Bonjour sorcier/e. Tu es sur le Chemin de traverse.\nSi tu souhaites aller chez Fleury et Bott, librairie de sorcier, tape 1 \nSi tu souhaites aller chez Madame Guipure, magasin de prêt à porter pour mages et sorcier, tape 2 \nSi tu souhaites aller chez Ollivander, fabricant de baguettes magiques, tape 3 \nOù souhaites-tu aller ? ")
    if reponse == '1':
        somme_obligatoire = (0, 60, 63, 231, 899)
        argent_a_rendre_librairie = int(input("Combien doit-ont vous rendre ? (entrez un entier)"))
        print("\n")
        chez_fleury_et_bott(argent_a_rendre_librairie)
        print("\n")
        print("La consigne obligeant, voici l'affichage des sommes à rendre obligatoires:")
        for elements in somme_obligatoire:
            print(f"Rendu monnaie pour {elements}€")
            chez_fleury_et_bott(elements)
            print("\n")

        
        
        
    
    elif reponse == '2' :
        djdsj
    #Si on répond n'importe quoi ca fait quand meme ollivander
    else :
        Chez_Ollivander()

def chez_fleury_et_bott(argent_a_rendre):
    
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
    
    for i in dico_monnaie_illimitée.keys():
            while argent_a_rendre2 >= i:
                dico_monnaie_illimitée[i] += 1
                argent_a_rendre2 -= i
    for i in dico_monnaie_illimitée.keys():
        if dico_monnaie_illimitée[i] > 0 :
            print(f"Le vendeur vous rend {dico_monnaie_illimitée[i]} coupure.s de {i} €")

a_rendre = []
gallions = int(input("Combien de gallions ? "))
mornilles = int(input("Combien de mornilles ? "))
noises = int(input("Combien de noises ? "))
somme_en_noises = (gallions * 17 * 29) + (mornilles * 29) + noises
gallions_a_rendre = somme_en_noises // (17*29)
a_rendre.append(gallions_a_rendre)
somme_en_noises -= gallions_a_rendre * (17*29)
mornilles_a_rendre = somme_en_noises // 29
a_rendre.append(mornilles_a_rendre)
somme_en_noises -= mornilles_a_rendre * 29
noises_a_rendre = somme_en_noises
a_rendre.append(noises_a_rendre)
print(a_rendre)

'''
def affichage_resultat() :
    
'''
'''
    Affiche le résulat sous forme de phrase

    Entrée : Un dico 
    Sortie : Une chaine de caractères
'''
'''

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
    for i in dico_monnaie_illimitée.keys():
            while argent >= i:
                dico_monnaie_illimitée[i] += 1
                argent -= i
    for i in dico_monnaie_illimitée.keys():
        if dico_monnaie_illimitée[i] > 0 :
            print(f"le vendeur vous rend {dico_monnaie_illimitée[i]} coupure.s de {i}")
'''

