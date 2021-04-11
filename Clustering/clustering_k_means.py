from sklearn.cluster import KMeans, MeanShift, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs, make_moons, make_circles
import matplotlib.pyplot as plt

puntos, etiquetas = make_blobs(n_samples=500, centers=5, cluster_std=1)
# puntos, etiquetas = make_moons(noise=0.1)

# Code to help programmer determine how many clusters are recommended for this dataset
# error = []
# for clusters in range(1, 11):
#     k_means = KMeans(n_clusters=clusters)
#     resultado = k_means.fit_predict(puntos)
#     error.append(k_means.inertia_)
#
# plt.plot(range(1, 11), error)
# plt.show()
# Here it ends

# Code to compute all the points and cluster them
# k_means = KMeans(n_clusters=5)
# resultado = k_means.fit_predict(puntos)
#
# plt.scatter(puntos[:, 0], puntos[:, 1], c=resultado, cmap="plasma")
# plt.show()
# Here it ends


# Code to compute all the points and cluster them using MeanShift
# agrupador = MeanShift(bandwidth=2)
# Fit predict returns all the labels the algorithm has found
# resultado = agrupador.fit_predict(puntos)

# plt.scatter(puntos[:, 0], puntos[:, 1], c=resultado, cmap="plasma")
# plt.show()


# Code to compute all the points and cluster them using MeanShift
# agrupador = DBSCAN(eps=0.3, min_samples=2)
# Fit predict returns all the labels the algorithm has found
# resultado = agrupador.fit_predict(puntos)
#
# plt.scatter(puntos[:, 0], puntos[:, 1], c=resultado, cmap="plasma")
# plt.show()


agrupador = GaussianMixture(n_components=5)
# Fit predict returns all the labels the algorithm has found
resultado = agrupador.fit_predict(puntos)

plt.scatter(puntos[:, 0], puntos[:, 1], c=resultado, cmap="plasma")
plt.show()
