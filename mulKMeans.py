from sklearn.cluster import KMeans
# import numpy as np

def train(X,x):

    kmeans = KMeans(n_clusters=20, random_state=0).fit(X)
    result = kmeans.predict(x)
    return result


