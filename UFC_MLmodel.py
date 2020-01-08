import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler



pd.set_option("display.width", 2000)
pd.set_option("display.max_columns", 80)
pd.set_option("display.max_rows", 2000000)

# read in file
ml_model= pd.read_csv("smallUFCdataset.csv")


# change fighter names to numeric label
le = preprocessing.LabelEncoder()
ml_model["FIGHTER"] = le.fit_transform(ml_model["FIGHTER"])

#print(ml_model.head())

# all columns except WINNER
X = ml_model.iloc[:, :3].values
# only DC column
y = ml_model.iloc[:, 4:].values

# split train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# apply feature scaling to normalize the range of each feature
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


#LinearSVC model
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

svc_model = LinearSVC(random_state=0)
pred = svc_model.fit(X_train, y_train).predict(X_test)
print("LinearSVC accuracy: ", accuracy_score(y_test, pred, normalize=True))

# K Nearest Neighbor model

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

neigh = KNeighborsClassifier(n_neighbors=5)
neigh.fit(X_train, y_train)
pred = neigh.predict(X_test)
print("KNeighbors accuracy scores :",accuracy_score(y_test,pred))

# Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

gnb = GaussianNB()
pred = gnb.fit(X_train, y_train).predict(X_test)
print("Naive-Bayes accuracy : ",accuracy_score(y_test, pred, normalize=True))








