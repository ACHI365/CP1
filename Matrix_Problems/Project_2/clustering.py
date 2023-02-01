import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import pandas as pd

customers = np.random.rand(20, 2)  # randomly generate data

# Plot the customer data
plt.scatter(customers[:, 0], customers[:, 1])
plt.xlabel('Income')
plt.ylabel('Age')
plt.show()

K = int(input("How many clusters: "))
centroids = customers[np.random.choice(customers.shape[0], K, replace=False)]


# choose amount of clusters and randomly choose initial centroids

def euclidean_norm(vector):  # second normal form
    res = 0
    for v in vector:
        res += v * v
    return sqrt(res)


def assign_cluster(customers, centroids):
    clusters = np.zeros(customers.shape[0])  # create cluster array

    for i, customer in enumerate(customers):
        min_distance = float('inf')
        for j, centroid in enumerate(centroids):
            curr_distance = euclidean_norm(customer - centroid)  # if should assign to new cluster assign
            if curr_distance < min_distance:
                min_distance = curr_distance
                clusters[i] = j

    return clusters


def update_centroids(customers, centroids, clusters):
    for i in range(centroids.shape[0]):  # update cluster according to formula
        cluster = customers[clusters == i]
        sum_points = np.sum(cluster, axis=0)
        centroids[i] = sum_points / len(cluster)
    return centroids


previous_centroids = []
clusters = assign_cluster(customers, centroids)
curr_clust = update_centroids(customers, centroids, clusters)
done = False
i = 0
while not done:  # while newer, better suited clusters can be found don't stop
    curr_clust = update_centroids(customers, curr_clust, clusters)
    if i > 0:
        done = np.not_equal(curr_clust, previous_centroids).any()
    i += 1
    clusters = assign_cluster(customers, curr_clust)
    previous_centroids = curr_clust.copy()
    print(done)

plt.scatter(customers[:, 0], customers[:, 1], c=clusters)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, linewidths=3, color='r')  # centroid locations
plt.xlabel('Income')
plt.ylabel('Age')
plt.show()
