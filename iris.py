#import numpy
from sklearn.datasets import load_iris

iris = load_iris()
#データの形
print (iris.data.shape)
#花の種類
print(iris.target_names)