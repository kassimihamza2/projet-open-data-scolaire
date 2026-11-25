import pandas as pd
import re
from pathlib import Path

# =====================================================
# 1. CHARGEMENT
# =====================================================

source = Path("data/processed/etablissements_scolaires_corriges.csv")

df = pd.read_csv(source)

print("Dataset chargé :", df.shape)

# =====================================================
# 2. NORMALISATION GENERALE DES TEXTES
# =====================================================

colonnes_textuelles = [
    "Nom Etablissement",
    "Adresse",
    "Ville",
    "Téléphone",
    "FAX",
    "Email",
    "Nature",
    "Cycle d'enseignement",
    "Région",
    "Province",
    "Commune"
]

for colonne in colonnes_textuelles:

    df[colonne] = df[colonne].apply(
        lambda x: re.sub(r"\s+", " ", x.replace("\xa0", " ")).strip()
        if isinstance(x, str)
        else x
    )

# =====================================================
# 3. HARMONISATION DU CYCLE D'ENSEIGNEMENT
# =====================================================

df["Cycle d'enseignement"] = (
    df["Cycle d'enseignement"]
    .replace({
        "Etablissement de l'enseignement collégial":
        "Etablissement de l'Enseignement Collégial"
    })
)

# =====================================================
# 4. NETTOYAGE DES COMMUNES
# =====================================================

df["Commune"] = df["Commune"].str.rstrip(";").str.strip()

# =====================================================
# 5. EXPORT DU DATASET NORMALISE
# =====================================================

sortie = Path("data/processed/etablissements_scolaires_normalises.csv")

df.to_csv(
    sortie,
    index=False,
    encoding="utf-8-sig"
)

# =====================================================
# 6. COMPARAISON AVANT / APRES
# =====================================================

print("\n" + "=" * 55)
print("RAPPORT DE NORMALISATION")
print("=" * 55)

print("Nombre de lignes :", len(df))

print("\nCycles après normalisation :")
print(df["Cycle d'enseignement"].value_counts())

print("\nNombre de catégories de cycle :")
print(df["Cycle d'enseignement"].nunique())

print("\nNombre de régions :")
print(df["Région"].nunique())

print("\nNombre de natures :")
print(df["Nature"].nunique())

print("\nDoublons exacts :", df.duplicated().sum())

print("\nFichier créé :", sortie)