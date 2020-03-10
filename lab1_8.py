from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

#Reading dataset from the input CSV file
dataset = pd.read_csv('./winequality-red.csv')

#Selecting data and the target label
X_train=dataset.drop(['quality'],axis=1)
Y_train=np.log(dataset.quality)

#Splitting train and test data
X_train, X_test, Y_train, y_test= train_test_split(X_train, Y_train, test_size=0.33, random_state=42)

#Performing regression and fitting into the model
MR = LinearRegression()
MR.fit(X_train, Y_train)
y_pred=MR.predict(X_test)

#Calculating R-Squared and RMSE Value
print("(Before EDA) R-Squared: ", MR.score(X_test, y_test))
print("(Before EDA) RMSE(Root Mean Squared Error):",np.sqrt(mean_squared_error(y_test,y_pred)))

#After EDA
#Handling Nulling values if exists
data=dataset.apply(lambda x: x.fillna(x.mean()),axis=0)
print(data.isnull().sum())

#selecting data and the target label
X_train = data.drop("quality",axis=1)
Y_train = np.log(dataset.quality)

#Splitting train and test data with different test size
X_train, X_test, Y_train, y_test= train_test_split(X_train, Y_train, test_size=0.33, random_state=42)

#Performing regression and fitting into the model
MR = LinearRegression()
MR.fit(X_train, Y_train)
y_pred=MR.predict(X_test)

#Calculating R-Squared and RMSE Value
print("(After EDA) R-Squared: ",MR.score(X_test, y_test))
print("(After EDA) RMSE(Root Mean Squared Error):", np.sqrt(mean_squared_error(y_test,y_pred)))