def feature_engineering_v1_lr(X):

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