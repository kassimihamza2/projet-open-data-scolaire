import pandas as pd
import csv
import re
from pathlib import Path

# ============================================================
# 1. CHARGEMENT DU FICHIER ORIGINAL
# ============================================================

fichier = Path("data/raw/etablissements_scolaires.xls")
df = pd.read_excel(fichier)

df.columns = df.columns.str.strip().str.rstrip(";")

# ============================================================
# 2. DEFINITION DU SCHEMA FINAL
# ============================================================

colonnes = [
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

# DataFrame avec les mêmes index que le fichier original
df_corrige = pd.DataFrame(index=df.index, columns=colonnes)

# ============================================================
# 3. IDENTIFICATION DES LIGNES MAL STRUCTUREES
# ============================================================

colonnes_geo = [
    "Nature",
    "Cycle d'enseignement",
    "Région",
    "Province",
    "Commune"
]

mask = df[colonnes_geo].isnull().all(axis=1)

lignes_normales = df.loc[~mask]
lignes_anomalies = df.loc[mask]

print("Lignes mal structurées :", len(lignes_anomalies))

# ============================================================
# 4. RECUPERATION DES LIGNES NORMALES
# ============================================================

for colonne in df.columns:
    if colonne in colonnes:
        df_corrige.loc[lignes_normales.index, colonne] = (
            lignes_normales[colonne]
        )

# ============================================================
# 5. REPARATION DES LIGNES ANORMALES
# ============================================================

nb_reparees = 0
nb_erreurs = 0

for index, valeur in lignes_anomalies["Nom Etablissement"].items():

    try:
        champs = next(csv.reader([str(valeur)]))

        if len(champs) != 11:
            print(f"Structure inattendue à l'index {index}: {len(champs)} champs")
            nb_erreurs += 1
            continue

        df_corrige.loc[index, colonnes] = champs
        nb_reparees += 1

    except Exception as e:
        print(f"Erreur à l'index {index}: {e}")
        nb_erreurs += 1

# ============================================================
# 6. NETTOYAGE DES VALEURS TEXTUELLES
# ============================================================

def nettoyer_texte(valeur):

    if pd.isna(valeur):
        return pd.NA

    valeur = str(valeur).replace("\xa0", " ").strip()
    valeur = re.sub(r"\s+", " ", valeur)

    if valeur.upper() in ["", "NULL", "NAN"]:
        return pd.NA

    return valeur


for colonne in colonnes:
    df_corrige[colonne] = df_corrige[colonne].apply(nettoyer_texte)

# ============================================================
# 7. NETTOYAGE DE LA COMMUNE
# ============================================================

df_corrige["Commune"] = (
    df_corrige["Commune"].str.rstrip(";").str.strip()
)

# ============================================================
# 8. NETTOYAGE DES VALEURS FAX PLACEHOLDER
# ============================================================

df_corrige["FAX"] = df_corrige["FAX"].apply(
    lambda x: pd.NA
    if isinstance(x, str) and x.replace(" ", "") in ["---", "-"]
    else x
)

# ============================================================
# 9. EXPORT DU DATASET
# ============================================================

df_corrige = df_corrige.reset_index(drop=True)

dossier = Path("data/processed")
dossier.mkdir(parents=True, exist_ok=True)

sortie = dossier / "etablissements_scolaires_corriges.csv"

df_corrige.to_csv(
    sortie,
    index=False,
    encoding="utf-8-sig"
)

# ============================================================
# 10. RAPPORT DE CONTROLE
# ============================================================

print("\n" + "=" * 55)
print("RAPPORT DE REPARATION")
print("=" * 55)

print("Lignes originales :", len(df))
print("Lignes normales :", len(lignes_normales))
print("Lignes réparées :", nb_reparees)
print("Erreurs :", nb_erreurs)
print("Lignes finales :", len(df_corrige))
print("Colonnes finales :", len(df_corrige.columns))

print("\nValeurs manquantes :")
print(df_corrige.isnull().sum())

print("\nDoublons exacts :", df_corrige.duplicated().sum())

print("\nExemples des lignes réparées :")
print(df_corrige.iloc[470:475].to_string(index=False))

print("\nFichier créé :", sortie)