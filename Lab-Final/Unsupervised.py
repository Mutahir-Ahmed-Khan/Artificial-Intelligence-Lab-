import numpy as nm
import pandas as pd
import matplotlib.pyplot as mtp
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler 

df = pd.read_csv("Mall_Customer.csv")
df.head()
x = df.iloc[:, [3, 4]].values

wcss_list=[]
for i in range(1,11):
  kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
  kmeans.fit(x)
  wcss_list.append(kmeans.inertia_)
mtp.plot(range(1,11),wcss_list)
mtp.title('Mutahirs Graph')
mtp.ylabel('K240030')
mtp.xlabel('BSCS-4F')
mtp.show()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(x)

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_predict = kmeans.fit_predict(X_scaled)

mtp.scatter(x[y_predict == 0, 0], x[y_predict == 0, 1], s=100, c='blue', label='Cluster 1')
mtp.scatter(x[y_predict == 1, 0], x[y_predict == 1, 1], s= 100, c='red', label='Cluster 2')
mtp.scatter(x[y_predict == 2, 0], x[y_predict == 2, 1], s= 100, c='green', label='Cluster 3')
mtp.scatter(x[y_predict == 3, 0], x[y_predict == 3, 1], s= 100, c='purple', label='Cluster 4')
mtp.title('One More Graph')
mtp.ylabel('k240030')
mtp.xlabel('BSCS-4F')
mtp.legend()
mtp.show()
