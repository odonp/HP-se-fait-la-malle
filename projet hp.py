# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:30:49 2023

@author: loubna.zbitou
"""

argent = int(input("Combien avez-vous payé ?"))

while argent > 0 :
    if argent > 500 :
        argent = argent - 500
        print (500)
    elif argent > 200 :
        argent = argent - 200
        print (200)
    elif argent > 100 :
        argent = argent - 100
        print (100)
    elif argent > 50 :
        argent = argent - 50
        print (50)
    elif argent > 20 :
        argent = argent - 20
        print (20)
    elif argent > 10 :
        argent = argent - 10
        print (10)
    elif argent > 5 :
        argent = argent - 5
        print (5)
    elif argent > 2 :
        argent = argent - 2
        print (2)
    else :
        argent = argent - 1
        print (1)

Deux idées pour continuer le projet :

argent = int(input("Combien avez-vous payé ? "))
monnaie = {'Billet' : 500,'Billet' : 200,'Billet' : 100,'Billet' : 50,'Billet' : 20,'Billet' : 10,'Billet': 5,'Pièce' : 2,'Pièce' : 1}
monnaie.values(argent)


prix = int(input("Quel est le prix à payer ? "))
monnaie = [{'Billet' : '500'},{'Billet' : '200'},{'Billet' : '100'},{'Billet' : '50'},{'Billet' : '20'},{'Billet' : '10'},{'Billet': '5'},{'Pièce' : '2'},{'Pièce' : '1'}]
monnaie.append(prix)    
print(monnaie)

# interface homme machine avec conversion de l'argent

entrée = input("Bonjour sorcier/e, vous entrez dans le chemin de traverse, pret a acheter vos fourniture ?")
 
if entrée == "oui" :
        magasin = input("Voulez vous commencer par achetez des livres ?")
        if magasin == "oui" :
        livre = input("vous entré Chez Fleury & Bott voulez vous achetez : Le Livre des sorts et enchantements, niveau 1 de Miranda Fauconnette et Histoire de la magie de Bathilda Tourdesac ?")
        if livre == "oui" : 
            argent = int(input("Combien doit-t-on vous rendre ?"))
            
                magasin = input("Voulez vous continuer vos achat et achetez une cape ?")

                   if magasin == "oui"
                       magasin = input("Voulez vous terminez votre course par achetez une baguette ?")
    
                       elif magasion == "oui"
                           Ors = int(input("Combien vaut 1 Gallion ?"))
                           Gallion = Ors
                           Mornille = Ors / 17
                           Gallion = Mornille * 17
                           Noises = Mornille / 29 
                           Mornille = 29 * Noises

else:
    entrée = int(input("Ëtes vous sur ?, vous entré dans le chemin de traverse, pret a acheter vos fourniture ?"))
    
