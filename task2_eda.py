import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# Load dataset
# -----------------------------
file_path = "data/country_population.csv"

df = pd.read_csv(file_path)

print("\n========== DATASET PREVIEW ==========")
print(df.head())

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# -----------------------------
# Clean population column
# -----------------------------
df["population"] = (
    df["population"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.replace(" ", "", regex=False)
)

df["population"] = pd.to_numeric(
    df["population"],
    errors="coerce"
)

# -----------------------------
# Basic statistics
# -----------------------------
print("\n========== DESCRIPTIVE STATISTICS ==========")
print(df["population"].describe())

# -----------------------------
# Top 10 most populated
# -----------------------------
top10 = df.nlargest(10, "population")

print("\n========== TOP 10 POPULATED LOCATIONS ==========")
print(top10[["country", "population"]])

# -----------------------------
# Create output folder
# -----------------------------
os.makedirs("outputs", exist_ok=True)

# -----------------------------
# Save EDA summary
# -----------------------------
with open(
    "outputs/eda_summary.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "CodeAlpha Data Analytics Internship - Task 2 EDA\n\n"
    )

    f.write(
        f"Dataset shape: {df.shape}\n\n"
    )

    f.write("Columns:\n")
    f.write(str(df.columns.tolist()))

    f.write("\n\nData Types:\n")
    f.write(str(df.dtypes))

    f.write("\n\nMissing Values:\n")
    f.write(str(df.isnull().sum()))

    f.write("\n\nDescriptive Statistics:\n")
    f.write(str(df["population"].describe()))

    f.write("\n\nTop 10 Populated Locations:\n")
    f.write(str(top10[["country", "population"]]))

# -----------------------------
# Visualization 1
# Top 10 populations
# -----------------------------
plt.figure(figsize=(12, 6))

sns.barplot(
    data=top10,
    x="population",
    y="country"
)

plt.title("Top 10 Most Populated Locations")
plt.xlabel("Population")
plt.ylabel("Location")

plt.tight_layout()

plt.savefig(
    "outputs/top10_population.png"
)

plt.show()

# -----------------------------
# Visualization 2
# Population distribution
# -----------------------------
plt.figure(figsize=(10, 6))

sns.histplot(
    df["population"].dropna(),
    bins=30
)

plt.title("Population Distribution")
plt.xlabel("Population")
plt.ylabel("Number of Locations")

plt.tight_layout()

plt.savefig(
    "outputs/population_distribution.png"
)

plt.show()

# -----------------------------
# Completion message
# -----------------------------
print("\n========== TASK 2 COMPLETED ==========")
print("EDA results saved in the outputs folder.")
