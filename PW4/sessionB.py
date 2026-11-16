import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

os.makedirs("results", exist_ok=True)

#B1
wine = load_wine(as_frame=True)
X = wine.data
cultivar = wine.target

#B2
pca_raw = PCA()
pca_raw.fit(X)
loadings_raw = pd.Series(pca_raw.components_[0], index=X.columns).sort_values(ascending=False)
print("Raw PC1 dominates with Proline:\n", loadings_raw.head(3))

#B3
scaler = StandardScaler(with_mean=True, with_std=True)
Z = scaler.fit_transform(X)
pca_scaled = PCA()
pca_scaled.fit(Z)

explained_var = pca_scaled.explained_variance_ratio_
cum_var = np.cumsum(explained_var)


plt.figure()
plt.bar(range(1, len(explained_var)+1), explained_var, alpha=0.5, label='Individual')
plt.step(range(1, len(cum_var)+1), cum_var, where='mid', label='Cumulative')
plt.axhline(y=0.9, color='r', linestyle='--')
plt.xlabel('Principal Components')
plt.ylabel('Variance Ratio')
plt.legend()
plt.savefig('results/scree_plot.png')

#B4
inertias = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, init="k-means++", n_init=10, max_iter=300, random_state=0)
    km.fit(Z)
    inertias.append(km.inertia_)

plt.figure()
plt.plot(range(1, 11), inertias, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.savefig('results/elbow_plot.png')


km3 = KMeans(n_clusters=3, init="k-means++", n_init=10, max_iter=300, random_state=0)
km3.fit(Z)


Z_pca = pca_scaled.transform(Z)
plt.figure()
scatter = plt.scatter(Z_pca[:, 0], Z_pca[:, 1], c=km3.labels_, cmap='viridis', alpha=0.6)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend(*scatter.legend_elements(), title="Clusters")
plt.savefig('results/pca_scatter.png')

#B6
def get_agreement(true_labels, cluster_labels):
    table = pd.crosstab(true_labels, cluster_labels)
    return table.max(axis=0).sum() / len(true_labels)

agr_scaled = get_agreement(cultivar, km3.labels_)

km_raw = KMeans(n_clusters=3, init="k-means++", n_init=10, max_iter=300, random_state=0)
km_raw.fit(X)
agr_raw = get_agreement(cultivar, km_raw.labels_)

km_pc2 = KMeans(n_clusters=3, init="k-means++", n_init=10, max_iter=300, random_state=0)
km_pc2.fit(Z_pca[:, :2])
agr_pc2 = get_agreement(cultivar, km_pc2.labels_)

agreement_df = pd.DataFrame({
    "Method": ["Scaled", "Raw", "2 PCs of Scaled"],
    "Agreement": [agr_scaled, agr_raw, agr_pc2]
})
agreement_df.to_csv("results/B_agreement.csv", index=False)
print("Session B Completed. Saved plots and B_agreement.csv")
