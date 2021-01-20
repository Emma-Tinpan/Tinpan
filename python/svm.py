from sklearn import datasets, svm
import random
import numpy

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


#SVM
#SVC()メソッドでSVCアルゴリズムのオブジェクトを作成
#ここではSVMの中でも標準的なSVCアルゴリズムを利用する
clf = svm.SVC()
#fit()メソッドでデータを学習する
clf.fit(value_train, label_train)

#predict()メソッドでテストデータを予測
pred = clf.predict(value_test)
#予測がどれくらい合っているのか確認
result = list(pred == label_test).count(True) / len(label_test) * 100
print("正解率=" +str(result) +"%")