import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.datasets import load_iris
import joblib
from sklearn.metrics import accuracy_score, classification_report
s = pd.read_csv("data.csv")
x = s.drop(columns=['Flow_ID',' Source_IP',' Source_Port',' Destination_IP','Destination_Port',' Timestamp','Label','Flow_Bytes_per_second',' Flow_Packets_per_second','Fwd_Packets_per_second'])
y = s['ACK_Flag_Count']
x = pd.get_dummies(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
g = GaussianNB()
g.fit(x_train, y_train)
y_predict = g.predict(x_test)
print("gaussian nb")
ac = accuracy_score(y_test, y_predict)
c = classification_report(y_test, y_predict)
print(ac)
print("Classification Report:",c)
joblib.dump(g,"model.h5")
model = LogisticRegression()
model = LogisticRegression(max_iter=200)
model.fit(x_train, y_train)
probabilities = model.predict_proba(x_test)[:, 1]
threshold = 0.5
predictions = (probabilities > threshold).astype(int)
print("logistic regression")
ac1 = accuracy_score(y_test, predictions)
print(ac1)
c1=classification_report(y_test, predictions)
print(c1)
model5 = DecisionTreeClassifier()
model5 = DecisionTreeClassifier(max_depth=3)
model5.fit(x_train, y_train)
probabilities5= model5.predict_proba(x_test)
threshold1 = 0.5
predictions5= (probabilities5 [:, 1]> threshold1).astype(int)
print("decision tree classifier")
ac2= accuracy_score(y_test, predictions5)
print(ac2)
c2= classification_report(y_test,predictions5)
print(c2)
model1= LinearRegression()
model1.fit(x_train, y_train)
probabilities2 = model1.predict(x_test)
y_predict=(probabilities2>0.5).astype(int)
print("linear regression")
ac3= accuracy_score(y_test,y_predict)
print(ac3)
c3= classification_report(y_test,y_predict)
print(c3)
data=load_iris()
X=data.data
y=data.target
y=(y>1).astype(int)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model2= SVC(probability=True,kernel='linear')
model2.fit(x_train, y_train)
probabilities3= model2.predict(x_test)
print("svc")
ac4= accuracy_score(y_test,probabilities3)
print(ac4)
c4= classification_report(y_test,probabilities3)
print(c4)
