#crée le 30 Août 2023
#Crée par Zhenchen Xu
#Une programme de deviner le nombre


#Variables et imports
import random
playing = True
global number
number = 0
global number1
global number2

#ce fonction est fait pour demander l'usager de choisirt un range pour le number
def range():
    number1 = int(input('le minimum range:'))
    number2 = int(input('le maximum range:'))
    print('le nombre à deviner est choisi, ce sera entre ' + str(number1) + ' et ' + str(number2))
    return random.randint(number1, number2)

print('Bievenue au Number_Guess, ici tu devine un nombre de 0 à 1000 (inclus) et essaye de deviner le chiffre en le moins de essaies possibles. ')

#fonction pour voir si le joueur veut recommencer une autre partie
while playing == True:
    #fonction en haut
    number = range()
    Essai = 0
    guess = 'x'
    #un loop pour le n. d'essaie par l'utilisateur
    while (guess != number) :
        Essai += 1
        guess = int(input('Entrez le chiffre:'))

        #analyzer input
        if guess < number:
            print('Le chiffre à deviner est plus grand que ce que tu as entré.')
        elif guess > number:
            print('Le chiffre à deviner est plus petit que ce que tu as entré.')
        else:
            # la personne a réussi à deviner le nombre
            print('Bravo! Vous avez trouvez le chiffre, ' + str(number) + ' ! Cela vous a pris ' + str(Essai) + ' d\'essai. ')
    quit = str(input('Voule-vous recommencer une autre partie? 1 pour oui 2 pour non:'))
    #quitter ou recommencer une autre partie
    if quit == '2':
        #la partie termine
        playing = False
    else:
        #une nouvelle partie
        playing = True