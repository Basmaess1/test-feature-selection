import pandas as pd
import matplotlib.pyplot as plt

# Toy dataset
data = {
    'Personne': [1, 2, 3, 4],
    'Taux de glucose': [80, 140, 90, 160],
    'Diabète': [0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Calcul manuel de la moyenne
glucoses = df['Taux de glucose']
moyenne = sum(glucoses) / len(glucoses)

# Calcul manuel de la variance (échantillon)
somme_ecarts_carrés = sum((x - moyenne) ** 2 for x in glucoses)
variance = somme_ecarts_carrés / (len(glucoses) - 1)

print("Moyenne du taux de glucose :", moyenne)
print("Variance du taux de glucose :", variance)

# Visualisation
plt.figure(figsize=(6, 4))
plt.bar(df['Personne'], df['Taux de glucose'], color='lightcoral')
plt.axhline(y=moyenne, color='blue', linestyle='--', label='Moyenne')
plt.title("Taux de glucose (Toy Dataset)")
plt.xlabel("Personne")
plt.ylabel("Taux de glucose (mg/dL)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
