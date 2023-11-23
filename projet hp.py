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