
import pandas as pd
import csv
from collections import Counter
from pathlib import Path

fichier = Path("data/raw/etablissements_scolaires.xls")
df = pd.read_excel(fichier)

df.columns = df.columns.str.strip().str.rstrip(";")

colonnes_geo = [
    "Nature",
    "Cycle d'enseignement",
    "Région",
    "Province",
    "Commune"
]

# Repérer les lignes dont toutes les informations géographiques sont absentes
mask = df[colonnes_geo].isnull().all(axis=1)
lignes = df.loc[mask]

print("=" * 60)
print("1. DIAGNOSTIC DES LIGNES MAL STRUCTUREES")
print("=" * 60)

print("Nombre de lignes concernées :", len(lignes))
print("Nombre de colonnes du DataFrame :", len(df.columns))
print("Colonnes :", df.columns.tolist())

# Analyser le contenu de la première colonne
longueurs = []

for index, valeur in lignes["Nom Etablissement"].items():
    champs = next(csv.reader([str(valeur)]))
    longueurs.append(len(champs))

print("\n2. NOMBRE DE CHAMPS DANS LES LIGNES")
print(Counter(longueurs))

print("\n3. EXEMPLES DE LIGNES DECOMPOSEES")

for index, valeur in lignes["Nom Etablissement"].head(10).items():
    champs = next(csv.reader([str(valeur)]))

    print(f"\nLigne Excel/DataFrame : {index}")
    print("Nombre de champs :", len(champs))

    for numero, champ in enumerate(champs, start=1):
        print(f"Champ {numero} : {repr(champ)}")

print("\n4. VERIFICATION DES VALEURS DU DATAFRAME")

for index in lignes.index[:5]:
    print(f"\nIndex {index}")
    for colonne in df.columns:
        print(f"{colonne} = {repr(df.at[index, colonne])}")
