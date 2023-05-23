import pandas as pd

data = {
  "Nom": ["Pâtes", "Beurre", "Oeuf"],
  "Prix": [1.29, 1.51, 1.09],
  "Poids / Unité ": ["500 g", "300 g", 6]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)


