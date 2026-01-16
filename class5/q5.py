from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt

iris = load_iris()['data']
sepal_length=iris[:,0]
sepal_width=iris[:,1]
petal_length=iris[:,2]
petal_width=iris[:,3]

fig,ax=plt.subplots(4,4)
for i in range(4):
    for j in range(4):
        if i==j:
            ax[i][j].hist(iris[:,j],bins=11)
        else:
            ax[i][j].scatter(iris[:,j],iris[:,i],s=10)
plt.show()