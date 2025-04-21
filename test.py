import pandas as pd
import matplotlib.pyplot as plt

# Importer les données depuis un fichier CSV
df = pd.read_csv('diabetes.csv')

# Affichage des premières lignes pour vérification
# print(df.head())

# Sélection des colonnes 'Glucose' et 'BMI'
glucoses = df['Glucose']
bmi = df['BMI']

# Calcul manuel de la moyenne pour 'Glucose'
moyenne_glucose = sum(glucoses) / len(glucoses)

# Calcul manuel de la variance pour 'Glucose'
somme_ecarts_carrés_glucose = sum((x - moyenne_glucose) ** 2 for x in glucoses)
variance_glucose = somme_ecarts_carrés_glucose / (len(glucoses) - 1)

# Calcul manuel de la moyenne pour 'BMI'
moyenne_bmi = sum(bmi) / len(bmi)

# Calcul manuel de la variance pour 'BMI'
somme_ecarts_carrés_bmi = sum((x - moyenne_bmi) ** 2 for x in bmi)
variance_bmi = somme_ecarts_carrés_bmi / (len(bmi) - 1)

# Affichage des résultats
print("Moyenne du glucose :", moyenne_glucose)
print("Variance du glucose :", variance_glucose)

print("Moyenne du BMI :", moyenne_bmi)
print("Variance du BMI :", variance_bmi)

# Visualisation
plt.figure(figsize=(12, 6))
plt.bar(df.index, df['Glucose'], width=0.4, label='Glucose', color='purple', align='center')
plt.bar(df.index, df['BMI'], width=0.4, label='BMI', color='orange', align='edge')
plt.title("Taux de Glucose et BMI")
plt.xlabel("Personne")
plt.ylabel("Valeur")
plt.legend()
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
