from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import pandas as pd

#Reading dataset from the input file
dataset = pd.read_csv('./glass.csv')

#Handling null values and filling them with mean values of specific column
dataset = dataset.apply(lambda x: x.fillna(x.mean()),axis=0)

print(dataset.isnull().sum())

#Selecting the features
X_train = dataset.drop("Type",axis=1)
Y_train = dataset["Type"]

#Using train_test_split function for test data
X_train, X_test, Y_train, y_test= train_test_split(X_train, Y_train, test_size=0.33, random_state=42)

#Gaussian
g= GaussianNB()
g.fit(X_train, Y_train)
Y_pred =g.predict(X_test)
score = round(g.score(X_test, y_test) * 100, 2)
print("GNB Accuracy",score)

#KNN
k = KNeighborsClassifier()
k.fit(X_train, Y_train)
predicted = k.predict(X_train)
print("KNN Accuracy:",round(k.score(X_test, y_test) * 100, 2))

#SVM
s = SVC()
s.fit(X_train, Y_train)
predicted = s.predict(X_train)
print("SVM Accuracy:", round(s.score(X_test, y_test) * 100, 2))