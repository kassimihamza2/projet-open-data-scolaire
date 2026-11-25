
import pandas as pd
from pathlib import Path

# 1. Charger le dataset normalisé
fichier = Path("data/processed/etablissements_scolaires_normalises.csv")
df = pd.read_csv(fichier)

print("=" * 55)
print("          CONTROLE FINAL DU DATASET")
print("=" * 55)

# 2. Dimensions
print("\n1. DIMENSIONS")
print("Nombre de lignes :", df.shape[0])
print("Nombre de colonnes :", df.shape[1])

# 3. Valeurs manquantes
print("\n2. VALEURS MANQUANTES")
manquants = df.isnull().sum()
print(manquants)
print("\nTotal des valeurs manquantes :", manquants.sum())

# 4. Doublons
print("\n3. DOUBLONS")
print("Doublons exacts :", df.duplicated().sum())

# 5. Vérification des catégories
print("\n4. CATEGORIES")

for colonne in ["Région", "Nature", "Cycle d'enseignement"]:
    print(f"\n{colonne} :")
    print("Nombre de catégories :", df[colonne].nunique())
    print(df[colonne].value_counts(dropna=False))

# 6. Vérification des champs géographiques
print("\n5. COHERENCE GEOGRAPHIQUE")

for colonne in ["Région", "Province", "Commune"]:
    print(
        f"{colonne} - valeurs manquantes :",
        df[colonne].isnull().sum()
    )

# 7. Vérification des lignes mal réparées
print("\n6. VERIFICATION STRUCTURE")

motifs = df["Nom Etablissement"].astype(str).str.contains(
    r'".*,.*".*,',
    regex=True,
    na=False
)

print("Lignes avec un possible enregistrement CSV non réparé :", motifs.sum())

# 8. Vérification des colonnes essentielles
print("\n7. CHAMPS ESSENTIELS")

essentielles = [
    "Nom Etablissement",
    "Nature",
    "Cycle d'enseignement",
    "Région",
    "Province",
    "Commune"
]

for colonne in essentielles:
    print(
        f"{colonne} :",
        df[colonne].isnull().sum(),
        "valeur(s) manquante(s)"
    )

print("\n" + "=" * 55)
print("          CONTROLE TERMINE")
print("=" * 55)
