import data, leJustePrix, vehicule

def main():
    print("---- Début du programme ----")

    print("Choissisez le module à jouer : ")
    print("1. Données")
    print("2. Le Juste Prix")
    print("3. Véhicule")

    choix = input("Entrez votre choix : ")

    if choix == "1":
        print(data.df)
    elif choix == "2":
        leJustePrix.jouer_juste_prix()
    elif choix == "3":
        moto = vehicule.Moto("Yamaha","MT 07","2023",689)
        moto.afficher_informations()
        moto.demarrer()
        moto.accelerer(100)
        moto.freiner()
    else:
        print("Choix invalide. Veuillez sélectionner un module valide.")

    print("---- Fin du programme ----")

# Appel de la fonction main
if __name__ == "__main__":
    main()