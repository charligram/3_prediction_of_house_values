import pandas as pd

def preprocess(df):

    # Diccionario de orden para jerarquías en features categoricas
    HIERARCHIES_DICT = {
        'Po': 1,
        'Fa': 2,
        'TA': 3,
        'Gd': 4,
        'Ex': 5
    }

    # Lista de features que tienen la jerarquía anterior
    list_hierarchies_same_features = [
        'ExterQual',
        'ExterCond',
        'BsmtQual',
        'BsmtCond',
        'HeatingQC',
        'KitchenQual',
        'FireplaceQu',
        'GarageQual',
        'GarageCond',
        'PoolQC'
    ]

    # Diccionario para mapear LotShape
    dict_to_map_lotshape = {
        'IR3': 1,
        'IR2': 2,
        'IR1': 3,
        'Reg': 4
    }

    df['LotShape'] = df['LotShape'].map(dict_to_map_lotshape)

    # Iteración en cada feature de categorico ordinal de la lista
    for feat in list_hierarchies_same_features:
        df[feat] = df[feat].map(HIERARCHIES_DICT).fillna(0)         # Le ponemos un 0 cuando no coincide con nada de la jerarquía (no contiene el feature)

    return df


def model_predict(model, df):
    prediction = model.predict(df)

    return prediction