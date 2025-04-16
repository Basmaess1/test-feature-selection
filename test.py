import pandas as pd
import matplotlib.pyplot as plt

# Toy dataset avec une variable utile (Glucose) et une inutile (aléatoire)
data = {
    'Personne': [1, 2, 3, 4],
    'Taux de glucose': [80, 140, 90, 160],  
    'Score aléatoire': [12, 45, 13, 42],  
    'Diabète': [0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Moyennes
moy_glucose = sum(df['Taux de glucose']) / len(df)
moy_aleatoire = sum(df['Score aléatoire']) / len(df)

# Variances
var_glucose = sum((x - moy_glucose) ** 2 for x in df['Taux de glucose']) / (len(df) - 1)
var_aleatoire = sum((x - moy_aleatoire) ** 2 for x in df['Score aléatoire']) / (len(df) - 1)

print("Variance - Taux de glucose :", var_glucose)
print("Variance - Score aléatoire :", var_aleatoire)

# Visualisation
plt.figure(figsize=(8, 5))
bar_width = 0.35
index = range(len(df))

plt.bar([i - 0.2 for i in index], df['Taux de glucose'], width=bar_width, label='Taux de glucose', color='salmon')
plt.bar([i + 0.2 for i in index], df['Score aléatoire'], width=bar_width, label='Score aléatoire', color='lightblue')

plt.title("Comparaison : Variable utile vs. inutile")
plt.xlabel("Personne")
plt.ylabel("Valeur")
plt.xticks(index, df['Personne'])
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
