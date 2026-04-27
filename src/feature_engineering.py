def feature_engineering_v1_lr(X):
    """
    Primera versón de feature engineering para el modelo de LinearRegression, mapeando los features con variables categóricas ordinales
    en donde sus categorías son "None", "Po", "Fa", "TA", "Gd", "Ex".

    Args:
        X (pd.DataFrame): DataFrame con features con categorías ordinales como palabras.

    Returns:
        X (pd.DataFrame): DataFrame con features ordenados de manera numérica del 0 al 5.

    """

    category_map_ordinal = {
        'None': 0,
        'Po': 1,
        'Fa': 2,
        'TA': 3,
        'Gd': 4,
        'Ex': 5
    }
    
    cols_category_ordinal = [
        'BsmtQual', 'BsmtCond', 'HeatingQC', 'KitchenQual', 'FireplaceQu', 'GarageQual',
        'GarageCond', 'PoolQC'
    ]

    for col in cols_category_ordinal:
        X[col] = X[col].map(category_map_ordinal)

    return X