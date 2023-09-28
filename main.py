#crée le 30 Août 2023
#Crée par Zhenchen Xu
#Une programme de deviner le nombre


#Variables et imports
import random
Essai = 0
guess = 1001

number = random.randint(0, 1000)
print('Bievenue au Number_Guess, ici tu devine un nombre de 0 à 1000 (inclus) et essaye de deviner le chiffre en le moins de essaies possibles. ')

#un loop pour le n. d'essaie par l'utilisateur
while (guess != number) :
    Essai += 1
    guess = int(input("Entrez un chiffre de 0 à 1000 :"))

    #analyzer input
    if guess < number:
        print('Le chiffre à deviner est plus grand que ce que tu as entré.')
    else:
        print('Le chiffre à deviner est plus petit que ce que tu as entré.')

#la personne a réussi à deviner le nombre
print('Bravo! Vous avez trouvez le chiffre, ' + str(number) + ' ! Cela vous a pris ' + str(Essai) +' d\'essai. ')