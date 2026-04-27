import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor


def get_dummies_align(X_train, X_test):
    """
    Obtener dummies y alinear los datos de los test con los features del entrenamiento, rellenando con ceros los valores que estén en el
    entrenamiento pero no en el test y eliminando los features que no han sido vistos por el entrenamiento.

    Args:
        X_train (pd.DataFrame): DataFrame de entrenamiento del modelo.

        X_test (pd.DataFrame): DataFrame de prueba del modelo.

    Returns:
        X_train (pd.DataFrame): DataFrame con dummies de todos los valores categóricos.

        X_test (pd.DataFrame): DataFrame con dummies de todos los valores categóricos alineados a los features de entranamiento.
    """
    X_train = pd.get_dummies(X_train)
    X_test = pd.get_dummies(X_test)

    X_train, X_test = X_train.align(X_test, join='left', axis=1, fill_value=0)

    return X_train, X_test


def fast_model_rmse_lr(X_train, X_test, y_train, y_test):
    """
    Calcular el rmse para ciertos datos con el modelo de LinearRegression

    Args:
        X_train (pd.DataFrame): DataFrame de entrenamiento de X, sin nulos.

        X_test (pd.DataFrame): DataFrame de pruebas de X, sin nulos, alineados a los features del entrenamiento.

        y_train (pd.Series): Serie de los precios para el entrenamiento en y.

        y_test (pd.Series): Serie de los precios para las pruebas en y.

    Returns:
        rmse (int): Valor de rmse (root mean squared error), indicando cuanto se equivoca en promedio el modelo con respecto al valor real. 
    
    """

    linear_model = LinearRegression()

    linear_model.fit(X_train, y_train)

    y_pred = linear_model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    return rmse


def fast_model_rmse_xg(X_train, X_test, y_train, y_test):
    """
    Calcular el rmse para ciertos datos con el modelo de XGBRegressor

    Args:
        X_train (pd.DataFrame): DataFrame de entrenamiento de X, sin nulos.

        X_test (pd.DataFrame): DataFrame de pruebas de X, sin nulos, alineados a los features del entrenamiento.

        y_train (pd.Series): Serie de los precios para el entrenamiento en y.

        y_test (pd.Series): Serie de los precios para las pruebas en y.

    Returns:
        rmse (int): Valor de rmse (root mean squared error), indicando cuanto se equivoca en promedio el modelo con respecto al valor real. 
    
    """

    xgb_model = XGBRegressor()

    xgb_model.fit(X_train, y_train)

    y_pred = xgb_model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    return rmse

