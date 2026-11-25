import pandas as pd

fichier = "data/processed/etablissements_scolaires_corriges.csv"
df = pd.read_csv(fichier)

colonnes = [
    "Région",
    "Province",
    "Commune",
    "Nature",
    "Cycle d'enseignement"
]

print("=" * 65)
print("DIAGNOSTIC DES CATEGORIES")
print("=" * 65)

for colonne in colonnes:

    print("\n" + "=" * 65)
    print(f"COLONNE : {colonne}")
    print("Nombre de valeurs distinctes :", df[colonne].nunique())

    frequences = df[colonne].value_counts(dropna=False)

    for valeur, nombre in frequences.items():
        print(f"{repr(valeur)} : {nombre}")

# Recherche des espaces inutiles
print("\n" + "=" * 65)
print("RECHERCHE DES ESPACES INUTILES")
print("=" * 65)

for colonne in colonnes:

    espaces = df[colonne].dropna().astype(str).apply(
        lambda x: x != x.strip()
    ).sum()

    print(f"{colonne} : {espaces} valeurs avec espaces externes")