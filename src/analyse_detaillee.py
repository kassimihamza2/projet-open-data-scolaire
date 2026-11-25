
import pandas as pd
from pathlib import Path

fichier = Path("data/raw/etablissements_scolaires.xls")
df = pd.read_excel(fichier)

# Nettoyer uniquement les espaces des noms de colonnes
df.columns = df.columns.str.strip().str.rstrip(";")

print("=" * 60)
print("1. NOMBRE DE VALEURS DISTINCTES")
print("=" * 60)

for colonne in ["Région", "Province", "Commune", "Nature",
                "Cycle d'enseignement", "Ville"]:
    print(f"\n{colonne} : {df[colonne].nunique()} valeurs différentes")
    print(df[colonne].value_counts(dropna=False).head(15))

print("\n" + "=" * 60)
print("2. REPARTITION PAR REGION")
print("=" * 60)
print(df["Région"].value_counts(dropna=False).to_string())

print("\n" + "=" * 60)
print("3. REPARTITION PAR NATURE")
print("=" * 60)
print(df["Nature"].value_counts(dropna=False).to_string())

print("\n" + "=" * 60)
print("4. REPARTITION PAR CYCLE")
print("=" * 60)
print(df["Cycle d'enseignement"].value_counts(dropna=False).to_string())

print("\n" + "=" * 60)
print("5. VALEURS MANQUANTES PAR LIGNE")
print("=" * 60)

lignes_incompletes = df[df.isnull().any(axis=1)]
print(f"Nombre de lignes incomplètes : {len(lignes_incompletes)}")
print(lignes_incompletes.head(15).to_string(index=False))

print("\n" + "=" * 60)
print("6. VALEURS DU FAX")
print("=" * 60)
print(df["FAX"].value_counts(dropna=False).head(15))

print("\n" + "=" * 60)
print("7. EXEMPLES DE COMMUNES")
print("=" * 60)
print(df["Commune"].value_counts(dropna=False).head(30))
