
import pandas as pd
from pathlib import Path

# =====================================================
# 1. CHARGEMENT DU DATASET
# =====================================================

fichier = Path("data/processed/etablissements_scolaires_normalises.csv")
df = pd.read_csv(fichier)

print("=" * 65)
print("       ANALYSE EXPLORATOIRE DES ETABLISSEMENTS SCOLAIRES")
print("=" * 65)

print("\n1. INFORMATIONS GENERALES")
print("Nombre d'établissements :", len(df))
print("Nombre de colonnes :", len(df.columns))


# =====================================================
# 2. REPARTITION PAR REGION
# =====================================================

print("\n2. NOMBRE D'ETABLISSEMENTS PAR REGION")

region = df["Région"].value_counts()

print(region.to_string())

print("\nTop 5 des régions :")
print(region.head(5).to_string())


# =====================================================
# 3. REPARTITION PAR CYCLE
# =====================================================

print("\n3. REPARTITION PAR CYCLE D'ENSEIGNEMENT")

cycle = df["Cycle d'enseignement"].value_counts()

print(cycle.to_string())

print("\nPourcentage par cycle :")
print((cycle / len(df) * 100).round(2).to_string())


# =====================================================
# 4. REPARTITION PAR NATURE
# =====================================================

print("\n4. REPARTITION PAR NATURE D'ETABLISSEMENT")

nature = df["Nature"].value_counts()

print(nature.to_string())


# =====================================================
# 5. TOP 10 DES PROVINCES
# =====================================================

print("\n5. TOP 10 DES PROVINCES")

province = df["Province"].value_counts()

print(province.head(10).to_string())


# =====================================================
# 6. TOP 10 DES COMMUNES
# =====================================================

print("\n6. TOP 10 DES COMMUNES")

commune = df["Commune"].value_counts()

print(commune.head(10).to_string())


# =====================================================
# 7. CROISEMENT REGION / CYCLE
# =====================================================

print("\n7. REPARTITION REGION / CYCLE")

croisement = pd.crosstab(
    df["Région"],
    df["Cycle d'enseignement"]
)

print(croisement.to_string())


# =====================================================
# 8. STATISTIQUES DESCRIPTIVES
# =====================================================

print("\n8. STATISTIQUES DESCRIPTIVES")

print("Nombre de régions :", df["Région"].nunique())
print("Nombre de provinces :", df["Province"].nunique())
print("Nombre de communes :", df["Commune"].nunique())
print("Nombre de natures :", df["Nature"].nunique())
print("Nombre de cycles :", df["Cycle d'enseignement"].nunique())


# =====================================================
# 9. EXPORT DES RESULTATS
# =====================================================

dossier = Path("reports/eda")
dossier.mkdir(parents=True, exist_ok=True)

region.rename_axis("Région").reset_index(
    name="Nombre établissements"
).to_csv(dossier / "repartition_regions.csv", index=False, encoding="utf-8-sig")

cycle.rename_axis("Cycle").reset_index(
    name="Nombre établissements"
).to_csv(dossier / "repartition_cycles.csv", index=False, encoding="utf-8-sig")

nature.rename_axis("Nature").reset_index(
    name="Nombre établissements"
).to_csv(dossier / "repartition_natures.csv", index=False, encoding="utf-8-sig")

province.rename_axis("Province").reset_index(
    name="Nombre établissements"
).to_csv(dossier / "repartition_provinces.csv", index=False, encoding="utf-8-sig")

commune.rename_axis("Commune").reset_index(
    name="Nombre établissements"
).to_csv(dossier / "repartition_communes.csv", index=False, encoding="utf-8-sig")

croisement.to_csv(
    dossier / "croisement_region_cycle.csv",
    encoding="utf-8-sig"
)

print("\n9. EXPORT DES RESULTATS")
print("Fichiers CSV enregistrés dans :", dossier)

print("\n" + "=" * 65)
print("             ANALYSE TERMINEE")
print("=" * 65)
