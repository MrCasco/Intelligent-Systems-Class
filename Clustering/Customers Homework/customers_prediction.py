import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OrdinalEncoder, OneHotEncoder
from sklearn.cluster import KMeans, MeanShift, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs, make_moons, make_circles
import matplotlib.pyplot as plt

"""
The whole next section is about cleaning and normalizing our dataset
"""
# PHASE 1: Reading from csv
data = pd.read_csv('Mall_Customers.csv')

# PHASE 2: Filling null data with the median
median_spending_score = data["Spending Score"].median()
data["Spending Score"].fillna(median_spending_score, inplace=True)

# PHASE 3: Data normalizing
# data_without_gender = data.drop("Gender", axis=1)
# scaler = StandardScaler()
# result = scaler.fit_transform(data_without_gender)
# data_normalized = pd.DataFrame(result, columns=data_without_gender.columns, index=data_without_gender.index)
# data_normalized['Gender'] = data['Gender']

# PHASE 4: Convert non-numeric columns to numeric values
encoder = OrdinalEncoder()
result = encoder.fit_transform(data[['Gender']])
data['Gender'] = result

"""
The whole next section is about clustering now that we got all our data clean
"""


# Code block to know how many clusters are a good number for the k-means algorithm
# error = []
# for clusters in range(1, 11):
#     k_means = KMeans(n_clusters=clusters)
#     resultado = k_means.fit_predict(data[['Age']])
#     error.append(k_means.inertia_)
#
# plt.plot(range(1, 11), error)
# plt.show()


# K MEANS SECTION
k_means = KMeans(n_clusters=4)
resultado = k_means.fit_predict(data[['Age']])
# Plot results (Age vs Spending Score)
plt.scatter(data.iloc[:,2], data.iloc[:,4], c=resultado, cmap="plasma")
plt.xlabel("Age")
plt.ylabel("Spending Score")
plt.show()

k_means = KMeans(n_clusters=4)
resultado = k_means.fit_predict(data[['Age']])
# Plot results (Age vs Annual Income)
plt.scatter(data.iloc[:,2], data.iloc[:,3], c=resultado, cmap="plasma")
plt.xlabel("Age")
plt.ylabel("Annual Income")
plt.show()


# DBSCAN SECTION
# Code to compute all the points and cluster them using MeanShift
agrupador = DBSCAN(eps=0.3, min_samples=3)
# Fit predict returns all the labels the algorithm has found
resultado = agrupador.fit_predict(data[['Age']])

plt.scatter(data.iloc[:,2], data.iloc[:,4], c=resultado, cmap="plasma")
# plt.show()


# MEAN SHIFT SECTION
# Code to compute all the points and cluster them using MeanShift
agrupador = MeanShift(bandwidth=3)
# Fit predict returns all the labels the algorithm has found
resultado = agrupador.fit_predict(data[['Age']])

plt.scatter(data.iloc[:,2], data.iloc[:,4], c=resultado, cmap="plasma")
# plt.show()


# GAUSSIAN MIXTURE SECTION
agrupador = GaussianMixture(n_components=4)
# Fit predict returns all the labels the algorithm has found
resultado = agrupador.fit_predict(data[['Age']])

plt.scatter(data.iloc[:,2], data.iloc[:,4], c=resultado, cmap="plasma")
# plt.show()


# HISTOGRAM TO SEE AGES OF BEST-BUYING MALE AND FEMALE BUYERS
males = data[data['Gender']==1].loc[(data['Age'] < 40) & (data['Age'] > 28)]
females = data[data['Gender']==0].loc[(data['Age'] < 40) & (data['Age'] > 28)]
print((len(males)+len(females))/220)
print('Females:', len(females))
print('Males:', len(males))
