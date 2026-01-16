from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt

iris = load_iris()['data']
sepal_length=iris[:,0]
sepal_width=iris[:,1]
petal_length=iris[:,2]
petal_width=iris[:,3]

fig,ax=plt.subplots(4,4)
