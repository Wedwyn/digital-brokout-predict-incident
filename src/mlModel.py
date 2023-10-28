import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

df = pd.read_csv('/content/FDATASET.csv')
df
df['Summa CHP and nas'] = df['Summa CHP']/df['Население']


regr = RandomForestRegressor(max_depth=7, random_state=0)

X = df[['T','День года','Po', 'P', 'U', 'Ff', 'Summa CHP and nas']]
Y = df[['Y']]



from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X[X.columns[1:]] = scaler.fit_transform(X[X.columns[1:]])



X_train, X_test, y_train, y_test = train_test_split(
   X, Y, test_size=0.2, random_state=7)

regr.fit(X_train, y_train)

pred = regr.predict(X_test)

pred
mean_squared_error(y_test, pred)