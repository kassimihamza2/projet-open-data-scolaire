
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# =====================================================
# 1. CONFIGURATION
# =====================================================

fichier = Path("data/processed/etablissements_scolaires_normalises.csv")
df = pd.read_csv(fichier)

dossier = Path("reports/figures")
dossier.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid", palette="viridis")

print("Dataset chargé :", df.shape)
print("Génération des graphiques...\n")


# =====================================================
# 2. GRAPHIQUE : ETABLISSEMENTS PAR REGION
# =====================================================

plt.figure(figsize=(12, 8))

region = df["Région"].value_counts().sort_values()

sns.barplot(
    x=region.values,
    y=region.index
)

plt.title("Nombre d'établissements scolaires par région (2011)")
plt.xlabel("Nombre d'établissements")
plt.ylabel("Région")
plt.tight_layout()

plt.savefig(dossier / "etablissements_par_region.png", dpi=300)
plt.close()

print("1. Graphique par région créé.")


# =====================================================
# 3. GRAPHIQUE : REPARTITION PAR CYCLE
# =====================================================

plt.figure(figsize=(9, 7))

cycle = df["Cycle d'enseignement"].value_counts()

plt.pie(
    cycle.values,
    labels=["Primaire", "Collégial", "Qualifiant"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Répartition des établissements par cycle (2011)")
plt.tight_layout()

plt.savefig(dossier / "repartition_par_cycle.png", dpi=300)
plt.close()

print("2. Graphique par cycle créé.")


# =====================================================
# 4. GRAPHIQUE : TOP 10 DES PROVINCES
# =====================================================

plt.figure(figsize=(11, 7))

province = df["Province"].value_counts().head(10).sort_values()

sns.barplot(
    x=province.values,
    y=province.index
)

plt.title("Top 10 des provinces par nombre d'établissements")
plt.xlabel("Nombre d'établissements")
plt.ylabel("Province")
plt.tight_layout()

plt.savefig(dossier / "top10_provinces.png", dpi=300)
plt.close()

print("3. Graphique Top 10 provinces créé.")


# =====================================================
# 5. GRAPHIQUE : TOP 10 DES COMMUNES
# =====================================================

plt.figure(figsize=(11, 7))

commune = df["Commune"].value_counts().head(10).sort_values()

sns.barplot(
    x=commune.values,
    y=commune.index
)

plt.title("Top 10 des communes par nombre d'établissements")
plt.xlabel("Nombre d'établissements")
plt.ylabel("Commune")
plt.tight_layout()

plt.savefig(dossier / "top10_communes.png", dpi=300)
plt.close()

print("4. Graphique Top 10 communes créé.")


# =====================================================
# 6. HEATMAP : REGION / CYCLE
# =====================================================

croisement = pd.crosstab(
    df["Région"],
    df["Cycle d'enseignement"]
)

# Renommer les colonnes pour faciliter la lecture
croisement.columns = [
    colonne.replace("Etablissement de l'Enseignement ", "")
    for colonne in croisement.columns
]

plt.figure(figsize=(12, 9))

sns.heatmap(
    croisement,
    annot=True,
    fmt="d",
    cmap="YlGnBu",
    linewidths=0.5
)

plt.title("Répartition des établissements par région et par cycle")
plt.xlabel("Cycle d'enseignement")
plt.ylabel("Région")
plt.tight_layout()

plt.savefig(dossier / "heatmap_region_cycle.png", dpi=300)
plt.close()

print("5. Heatmap région/cycle créée.")


# =====================================================
# 7. BILAN
# =====================================================

print("\n" + "=" * 55)
print("       GENERATION DES GRAPHIQUES TERMINEE")
print("=" * 55)

print("\nDossier de sortie :", dossier)

for image in sorted(dossier.glob("*.png")):
    print("-", image.name)
