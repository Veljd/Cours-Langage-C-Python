class Animal:

    def __init__(self, nom, regime):
        self.nom = nom
        self.regime = regime

    def speak(self):
        print("L'animal se nomme", self.nom, "et il est", self.regime)

    def __str__(self):
        return "Nom: {self.nom}, Régime: {self.regime}"
    
class Tigre(Animal) : 

    def __init__(self, nom, regime):
        self.nom = nom
        self.regime = regime
        self.famille = "félin"
    
Tigrou = Tigre("Tigrou", "Carnivore")
Tigrou.speak()