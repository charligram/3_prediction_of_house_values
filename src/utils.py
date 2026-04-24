import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor


def get_dummies_align(X_train, X_test):
    X_train = pd.get_dummies(X_train)
    X_test = pd.get_dummies(X_test)

    X_train, X_test = X_train.align(X_test, join='left', axis=1, fill_value=0)

    return X_train, X_test


def fast_model_rmse_lr(X_train, X_test, y_train, y_test):

    linear_model = LinearRegression()

    linear_model.fit(X_train, y_train)

    y_pred = linear_model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    return rmse


def fast_model_rmse_xg(X_train, X_test, y_train, y_test):

    xgb_model = XGBRegressor()

    xgb_model.fit(X_train, y_train)

    y_pred = xgb_model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    return rmse

