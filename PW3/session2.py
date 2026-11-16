import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

df_heart = pd.read_csv("heart.csv")

healthy = df_heart[df_heart["target"] == 0]["thalach"]
disease = df_heart[df_heart["target"] == 1]["thalach"]

stat, p_val = stats.ttest_ind(healthy, disease, equal_var=False)
print(f"Thalach comparison (Welch's t-test): t-stat = {stat:.4f}, p-value = {p_val:.4e}")

def get_ci(data):
    mean = np.mean(data)
    sem = stats.sem(data)
    ci = sem * stats.t.ppf((1 + 0.95) / 2., len(data) - 1)
    return mean, ci

mean_h, ci_h = get_ci(healthy)
mean_d, ci_d = get_ci(disease)

print(f"The healthy group Thalach Mean: {mean_h:.2f} ± {ci_h:.2f}")
print(f"The disease group Thalach Mean:  {mean_d:.2f} ± {ci_d:.2f}")

plt.figure(figsize=(6, 5))
plt.errorbar(["Healthy (0)", "Disease (1)"], [mean_h, mean_d], yerr=[ci_h, ci_d], fmt='o', capsize=5, capthick=2, color='red')
plt.ylabel("Mean Max Heart Rate (thalach)")
plt.title("Thalach Comparison with 95% CI")
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig("thalach_comparison.png")
plt.close()

corr, corr_p = stats.pearsonr(df_heart["age"], df_heart["thalach"])
print(f"Age vs Thalach Pearson correlation: r = {corr:.4f}, p-value = {corr_p:.4e}")

plt.figure(figsize=(7, 5))
plt.scatter(df_heart["age"], df_heart["thalach"], alpha=0.6, color='purple')
plt.xlabel("Age")
plt.ylabel("Max Heart Rate (thalach)")
plt.title(f"Age vs Thalach (r = {corr:.2f})")
plt.savefig("age_vs_thalach.png")
plt.close()
(Pollution Index sabit saxlanıldıqda) 
df_chem = pd.read_csv("chemicals_cancer.csv")

corr_benz, _ = stats.pearsonr(df_chem["benzene"], df_chem["malignancy"])
corr_cadm, _ = stats.pearsonr(df_chem["cadmium"], df_chem["malignancy"])

print("\n--- Naive Analysis ---")
print(f"Benzene vs Malignancy: r = {corr_benz:.4f}")
print(f"Cadmium vs Malignancy: r = {corr_cadm:.4f}")

q_low, q_high = df_chem["pollution_index"].quantile([0.4, 0.6])
df_filtered = df_chem[(df_chem["pollution_index"] >= q_low) & (df_chem["pollution_index"] <= q_high)]

corr_benz_adj, _ = stats.pearsonr(df_filtered["benzene"], df_filtered["malignancy"])
corr_cadm_adj, _ = stats.pearsonr(df_filtered["cadmium"], df_filtered["malignancy"])

print("\n--- Adjusted Analysis ---")
print(f"Benzene vs Malignancy (Adjusted): r = {corr_benz_adj:.4f}")
print(f"Cadmium vs Malignancy (Adjusted): r = {corr_cadm_adj:.4f}")

p = df_heart["target"].value_counts(normalize=True)
entropy = -np.sum(p * np.log2(p))
print(f"\nBONUS: Target column Entropy = {entropy:.4f} bits (Max = 1.0 bit)")