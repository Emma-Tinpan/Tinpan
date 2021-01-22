from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import random 
import numpy as np
import pandas as pd


#sklearnからirisデータを取得
iris = datasets.load_iris()

#dataとtargetの結合
data = list(zip(iris.data.tolist(), iris.target))
#dataリストをシャッフル
random.shuffle(data)

#リストの分割
training_data = data[0:130]
test_data = data[130:150]

#print(training_data)

value_train, label_train = zip(*training_data)
value_test, label_test = zip(*test_data)


#k-NN
#k-NN
knc = KNeighborsClassifier(n_neighbors=10)
knc.fit(value_train, label_train)


#predict()メソッドでテストデータを予測
pred = knc.predict(value_test)
#予測がどれくらい合っているのか確認
result = list(pred == label_test).count(True) / len(label_test) * 100
print("正解率=" +str(result) +"%")