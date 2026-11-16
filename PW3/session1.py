import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

df_heart = pd.read_csv("heart.csv")
print("Heart dataset shape:", df_heart.shape)
print(df_heart.head())

continuous_cols = ["age", "chol", "trestbps", "thalach"]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

for i, col in enumerate(continuous_cols):
    axes[i].hist(df_heart[col], bins=15, edgecolor='black', alpha=0.7)
    axes[i].set_title(f"Distribution of {col}")
    axes[i].set_xlabel(col)
    axes[i].set_ylabel("Frequency")

plt.tight_layout()
plt.savefig("distributions.png")
plt.close()

print("\n--- The Shapiro-Wilk Test ---")
for col in continuous_cols:
    stat, p_value = stats.shapiro(df_heart[col])
    is_normal = p_value > 0.05
    print(f"{col}: W-stat={stat:.4f}, p-value={p_value:.4e} -> is normal? {is_normal}")