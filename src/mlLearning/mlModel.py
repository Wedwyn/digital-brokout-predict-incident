import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error
df = pd.read_csv('/Users/timofeymoskalev/Programming/Jupyter notebooks/FINAL_DATASET_643.csv',low_memory=False)
y = df['Проиcшествие']
X = df.drop(['Проиcшествие','Дата','Район'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=101)
from sklearn.ensemble import GradientBoostingRegressor
gb_model = GradientBoostingRegressor(verbose=1,n_estimators=110,max_depth=5)
gb_model.fit(X_train,y_train)
y_predict =  gb_model.predict(X_test)

SMSE = np.sqrt(mean_squared_error(y_test,y_predict))
MAE = mean_absolute_error(y_test,y_predict)
print(MAE,SMSE)
gb_model.feature_importances_