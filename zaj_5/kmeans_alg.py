import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

x = list()
y = list()
import random as r

for e in range(100):
    x.append(r.randint(1, 25))
    y.append(r.randint(1, 25))

data = list(zip(x, y))

km = KMeans(n_clusters=4)
km.fit(data)

plt.scatter(x, y, c=km.labels_)
plt.show()