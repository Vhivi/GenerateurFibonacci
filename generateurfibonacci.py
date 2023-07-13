#!/usr/bin/python
# -*- coding: utf-8 -*-

# Générateur des nombres de la suite de Fibonacci

# La série mathématique connue sous le nom de suite de Fibonacci a été l’une
# des questions informatique les plus populaires. Essentiellement, vous
# commencez avec deux nombres, de préférence 0 et 1, et vous les ajoutez
# pour créer votre troisième nombre de Fibonacci. Ensuite, il suffit
# d’additionner la somme et l’avant-dernier terme de Fibonacci pour générer
# le suivant.

# Ce qui donne :

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987...

# Dans ce projet, vous demandez la position du nombre de Fibonacci requise
# par l’utilisateur et vous le générez simplement. Une fois généré, vous
# pouvez afficher le nombre correspondant à l’utilisateur. Vous pouvez aller
# plus loin et montrer à l’utilisateur la série entière jusqu’à ce point avec
# le fonctionnement mathématique. C’est l’un des meilleurs projets Python
# pour s’initier au concept de la fonction récursive.


# Génération de la suite et affichage du nombre à la position demandée
def fibonacci(position):
    # Vérification de la position donnée
    # Elle doit être un entier positif supérieur à 0
    if position < 1:
        raise ValueError('''La position doit être un entier positif
                         supérieur à 0.''')
    else:
        # Génération de la suite jusqu'à la position demandée
        suitelist = [0]
        a = 0
        b = 1
        total = 0
        while len(suitelist) != position:
            a = b
            b = total
            total = a + b
            suitelist.append(total)
        return suitelist[position - 1], suitelist


def main():
    while True:
        try:
            # Demande de la position du nombre
            position = int(input('''Quel position dans la suite de Fibonacci
                            voulez-vous voir ?'''))
            # Génération de la suite et affichage dans la console
            print('Le nombre à la position {} est {}'
                .format(position, fibonacci(position)[0]))
            print('Voici la suite entière jusqu\'à la position demandée : {}'
                .format(fibonacci(position)[1]))
            break
        except ValueError as e:
            print(e)


main()
