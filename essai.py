somme = 899
compteur = 0
compteur +=1

while somme > 0:
    if somme > 500:
        somme -=500
        compteur +=1

    elif somme > 200:
        somme -= 200
        compteur +=1

    elif somme > 100:
        somme -= 100
        compteur +=1

    elif somme > 50:
        somme -= 50
        compteur +=1

    elif somme > 20:
        somme -= 20
        compteur +=1

    elif somme > 10:
        somme -= 10
        compteur +=1

    elif somme > 5:
        somme -= 5
        compteur +=1

    elif somme > 2:
        somme -= 2
        compteur +=1

    elif somme > 1:
        somme -= 1   
        compteur +=1

print(compteur)