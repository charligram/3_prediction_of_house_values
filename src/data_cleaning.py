def clean_data(X, median_lotfrontage=None, moda_electrical=None, itsTrain=True):
    """
    Rellenar con valores "None" los features que su valor de NaN o vacío tiene como significado la falta del feature, mas no la
    falta de información.

    Args:
        X (pd.DataFrame): Dataframe de entrenamiento o de pruebas con columnas con registros vacíos.

        median_lotfrontage (int): Número de la media del feature LotFrontage, solo es necesario para la liempieza 
        de un X de prueba. (default: None)

        moda_electrical (int): Valor de la moda del feature Electrical, solo necesario para X de prueba. (default: None)

        itsTrain (bool): Indicador booleano de si el DataFrame en X es entrenamiento o test. (default:True)

    Returns:
        X (pd.DataFrame): DataFrame con categorías rellenadas de "None" en los features donde la casa no contiene tal característica.

        median_lotfrontage (int): Valor de la media de LotFrontage para el dataset ingresado.

        moda_electrical (int): Valor de la moda de Electrical para el dataset ingresado.

    """

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