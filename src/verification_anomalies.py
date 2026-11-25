
import pandas as pd
from pathlib import Path

fichier = Path("data/raw/etablissements_scolaires.xls")
df = pd.read_excel(fichier)

df.columns = df.columns.str.strip().str.rstrip(";")

print("=" * 60)
print("1. LIGNES AVEC PLUSIEURS INFORMATIONS MANQUANTES")
print("=" * 60)

colonnes_geo = [
    "Nature",
    "Cycle d'enseignement",
    "Région",
    "Province",
    "Commune"
]

lignes_sans_geo = df[df[colonnes_geo].isnull().all(axis=1)]

print("Nombre de lignes sans informations géographiques :",
      len(lignes_sans_geo))

print(lignes_sans_geo.head(20).to_string(index=False))

print("\n" + "=" * 60)
print("2. NOMS D'ETABLISSEMENTS SUSPECTS")
print("=" * 60)

suspects = df[
    df["Nom Etablissement"].astype(str).str.contains(
        r"\d{1,2}[-/]\w+",
        case=False,
        na=False
    )
]

print("Nombre de noms suspects :", len(suspects))
print(suspects.to_string(index=False))

print("\n" + "=" * 60)
print("3. VALEURS DISTINCTES DES CYCLES")
print("=" * 60)

for valeur in df["Cycle d'enseignement"].dropna().unique():
    print(repr(valeur))

print("\n" + "=" * 60)
print("4. EXEMPLES DE VALEURS DES COMMUNES")
print("=" * 60)

for valeur in df["Commune"].dropna().unique()[:20]:
    print(repr(valeur))

print("\n" + "=" * 60)
print("5. TYPES DES VALEURS DES NOMS")
print("=" * 60)

print(df["Nom Etablissement"].map(
    lambda x: type(x).__name__
).value_counts())
