def clean_data(X, median_lotfrontage=None, moda_electrical=None, itsTrain=True):
    valid_nan_cols = [
        'Alley', 'MasVnrType', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'FireplaceQu',
        'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PoolQC', 'Fence', 'MiscFeature'
    ]

    for col in valid_nan_cols:
        X[col] = X[col].fillna('None')
    
    if itsTrain:
        median_lotfrontage = X['LotFrontage'].median()
        X['LotFrontage'] = X['LotFrontage'].fillna(median_lotfrontage)
    else:
        X['LotFrontage'] = X['LotFrontage'].fillna(median_lotfrontage)


    X['HasGarage'] = (X['GarageYrBlt'].notnull()).astype(int)
    
    X['GarageYrBlt'] = X['GarageYrBlt'].fillna(0)

    X['MasVnrArea'] = X['MasVnrArea'].fillna(0)

    if itsTrain:
        X.loc[
            (X['MasVnrType'] == 'None') & (X['MasVnrArea'] > 0),
            'MasVnrType'
        ] = 'Other'

    if itsTrain:
        moda_electrical = X['Electrical'].mode().iat[0]
        X['Electrical'] = X['Electrical'].fillna(moda_electrical)
    else:
        X['Electrical'] = X['Electrical'].fillna(moda_electrical)
    
    return X, median_lotfrontage, moda_electrical