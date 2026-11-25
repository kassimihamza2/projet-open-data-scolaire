import pandas as pd
from pathlib import Path

fichier = Path("data/raw/etablissements_scolaires.xls")

if not fichier.exists():
    raise FileNotFoundError(f"Fichier introuvable : {fichier}")

df = pd.read_excel(fichier)

print("=" * 60)
print("1. DIMENSIONS DU DATASET")
print("=" * 60)
print(f"Nombre de lignes : {df.shape[0]}")
print(f"Nombre de colonnes : {df.shape[1]}")

print("\n2. NOMS DES COLONNES")
print(df.columns.tolist())

print("\n3. TYPES DES COLONNES")
print(df.dtypes)

print("\n4. VALEURS MANQUANTES")
print(df.isnull().sum())

print("\n5. DOUBLONS")
print(f"Nombre de doublons : {df.duplicated().sum()}")

print("\n6. APERÇU DES DONNÉES")
print(df.head(10).to_string(index=False))

print("\n7. INFORMATIONS GÉNÉRALES")
df.info()