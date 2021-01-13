import pandas
from sklearn.datasets import load_iris
import random
import numpy
from sklearn.cluster import KMeans

#from sklearn import cluster

iris = load_iris()
iris_pd = pandas.DataFrame(iris.data, columns=iris.feature_names)
iris_target_pd_df = pandas.DataFrame(iris.target)
iris_target_pd = iris_target_pd_bf.rename( columns={'Unnamed: 0':'cluster'}, inplace=True )
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

#データの行をランダムに入れ替える
#pandas.dataframe.sample()
#frac=1でシャッフルできる
#reset_index()メソッドでデータフレームインデックスをリセットする
data_shuffle_1 = iris_data.sample(frac=1).reset_index(drop=True)
print(data_shuffle_1)

#numpy.random.permutation()　DaraFrameのインデックスをシャッフルする
#iloc()メソッドを使用するとランダムにできる
data_shuffle_2 = iris_data.iloc[numpy.random.permutation(iris_data.index)].reset_index(drop=True)
print(data_shuffle_2)

#分割0~120 120~150に分ける
data1 = data_shuffle_1[:120]
data2 = data_shuffle_1[120:]

print(data1)
print(data2)

#k-means
kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit(data1)
data1['cluster'] = clusters.labels_

print(data1['cluster'].unique())
data1.head()