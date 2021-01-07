import pandas
from sklearn.datasets import load_iris

iris = load_iris()
iris_pd = pandas.DataFrame(iris.data, columns=iris.feature_names)
iris_target_pd = pandas.DataFrame(iris.target)

print(iris_pd.head())
print(iris_target_pd.head())

#join（横方向）
iris_data = pandas.concat([iris_pd,iris_target_pd],axis=1)
print(iris_data)

#pandas前処理
#dataype
print(iris_data.dtypes)
#pandasの.describe()
print(iris_data.describe())