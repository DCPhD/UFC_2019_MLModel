import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import numpy as np





pd.set_option("display.width", 2000)
pd.set_option("display.max_columns", 80)
pd.set_option("display.max_rows", 2000000)

# read in file
ml_model= pd.read_csv("2019_UFC_fights_WL_included_B.csv")

# all columns except WINNER
X = ml_model.drop(columns=['FIGHTER', 'WINNER'])

# make y target variable
y = ml_model['WINNER'].values
#print(y[0:5])

# split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# create knn classifier
knn = KNeighborsClassifier(n_neighbors=3)

# fit classifier to data
knn.fit(X_train, y_train)

# check accuracy
#print(knn.score(X_test, y_test))
# .5875

# create new KNN model for cross validation
knn_cv = KNeighborsClassifier(n_neighbors=3)

# train model with 5 cross validation steps
cv_scores = cross_val_score(knn_cv, X, y, cv=5)

# print each cv score and average them
#print(cv_scores)
#print('cv_scores mean:{}'.format(np.mean(cv_scores)))
#0.633

# hypertuning with GridSearchCV

# create new KNN model
knn2 = KNeighborsClassifier()

# create dictionary for the range of K values we want to test
param_grid = {'n_neighbors': np.arange(1,25)}

# use gridsearch to test all values
knn_gscv = GridSearchCV(knn2, param_grid, cv=5)

# fit model to data
knn_gscv.fit(X, y)

# check top performing # of neighbors
print(knn_gscv.best_params_)
# 18

# check mean score for top performing # of neighbors
print(knn_gscv.best_score_)
# .6508
