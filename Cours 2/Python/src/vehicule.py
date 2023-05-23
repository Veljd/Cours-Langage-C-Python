from abc import ABC, abstractmethod

class Vehicule(ABC):
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    @abstractmethod
    def demarrer(self):
        pass

    @abstractmethod
    def accelerer(self, vitesse):
        pass

    @abstractmethod
    def freiner(self):
        pass

    def afficher_informations(self):
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.modele}")
        print(f"Année: {self.annee}")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, nombre_portes):
        super().__init__(marque, modele, annee)
        self.nombre_portes = nombre_portes

    def demarrer(self):
        print("La voiture démarre.")

    def accelerer(self, vitesse):
        print(f"La voiture accélère à {vitesse} km/h.")

    def freiner(self):
        print("La voiture freine.")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, cylindree):
        super().__init__(marque, modele, annee)
        self.cylindree = cylindree

    def demarrer(self):
        print("La moto démarre.")

    def accelerer(self, vitesse):
        print(f"La moto accélère à {vitesse} km/h.")

    def freiner(self):
        print("La moto freine.")