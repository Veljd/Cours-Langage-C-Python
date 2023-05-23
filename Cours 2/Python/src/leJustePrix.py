import random

def jouer_juste_prix():
    print("Bienvenue au Juste Prix !")
    print("Je pense à un nombre entre 1 et 100. Devinez quel est ce nombre !")

    nombre_a_deviner = random.randint(1, 100)
    nombre_devine = False

    while not nombre_devine:
        try:
            proposition = int(input("Entrez votre proposition : "))

            if proposition < nombre_a_deviner:
                print("C'est plus !")
            elif proposition > nombre_a_deviner:
                print("C'est moins !")
            else:
                print("Félicitations ! Vous avez trouvé le juste prix !")
                nombre_devine = True

        except ValueError:
            print("Veuillez entrer un nombre valide.")

    print("Merci d'avoir joué !")

