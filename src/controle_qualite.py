import pandas as pd
from pathlib import Path

# Chargement du dataset réparé
fichier = Path("data/processed/etablissements_scolaires_corriges.csv")
df = pd.read_csv(fichier)

print("=" * 60)
print("CONTROLE QUALITE DU DATASET")
print("=" * 60)

# 1. Dimensions
print("\n1. DIMENSIONS")
print("Nombre de lignes :", df.shape[0])
print("Nombre de colonnes :", df.shape[1])

# 2. Vérification du schéma
print("\n2. COLONNES")
print(df.columns.tolist())

# 3. Valeurs manquantes
print("\n3. VALEURS MANQUANTES")
print(df.isnull().sum())

# 4. Vérification des informations géographiques
colonnes_geo = [
    "Région",
    "Province",
    "Commune"
]

print("\n4. INFORMATIONS GEOGRAPHIQUES")
for colonne in colonnes_geo:
    print(f"{colonne} : {df[colonne].isnull().sum()} valeurs manquantes")

# 5. Vérification des lignes encore mal structurées
print("\n5. LIGNES POTENTIELLEMENT MAL STRUCTUREES")

anomalies = df["Nom Etablissement"].astype(str).str.contains(
    ',"',
    regex=False
)

print("Lignes contenant encore un motif CSV :", anomalies.sum())

# 6. Vérification des doublons
print("\n6. DOUBLONS")
print("Doublons exacts :", df.duplicated().sum())

# 7. Vérification des catégories
print("\n7. NOMBRE DE CATEGORIES")

for colonne in ["Région", "Nature", "Cycle d'enseignement"]:
    print(f"\n{colonne} :")
    print(df[colonne].nunique(), "valeurs distinctes")

# 8. Vérification des données récupérées
print("\n8. DONNEES AVEC TELEPHONE OU EMAIL")
print(
    df[["Nom Etablissement", "Téléphone", "Email"]]
    .dropna(subset=["Téléphone", "Email"], how="all")
    .head(10)
    .to_string(index=False)
)

# 9. Contrôle final
print("\n9. CONTROLES AUTOMATIQUES")

assert len(df) == 9859, "Nombre de lignes inattendu"
assert len(df.columns) == 11, "Nombre de colonnes inattendu"
assert df["Région"].notna().all(), "Régions manquantes détectées"
assert df["Province"].notna().all(), "Provinces manquantes détectées"
assert df["Commune"].notna().all(), "Communes manquantes détectées"

print("Tous les contrôles automatiques sont réussis.")