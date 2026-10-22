import streamlit as st
import requests
import os

st.title('House Prices Predictor')

st.write(
    'Introduce las caracteristicas de la vivienda'
)

st.subheader('Caracteristicas de la vivienda')


options_mssubclass = range(20, 191, 10)
options_mssubclass = list(options_mssubclass)
options_mssubclass = [str(number) for number in options_mssubclass]
ms_sub_class = st.selectbox(
    'Tipo de vivienda',
    options=options_mssubclass
)

ms_zoning = st.selectbox(
    'Zona general de la vivienda',
    options=['A', 'C', 'FV', 'I', 'RH', 'RL', 'RP', 'RM']
)

lot_frontage = st.number_input(
    'Pies desde la calle hasta la propiedad',
    min_value=0.0,
    value=0.0,
    step=5.0
)

lot_area = st.number_input(
    'Tamaño del terreno en pies cuadrados',
    min_value=0,
    value=1000,
    step=1000
)

street = st.selectbox(
    'Tipo de acceso vial a la propiedad',
    options=['Grvl', 'Pave']
)

alley = st.selectbox(
    'Tipo de acceso a la propiedad desde un callejón',
    options=['Grvl', 'Pave', 'NoAlleyAccess', None]
)

lot_shape = st.selectbox(
    'Forma general de la propiedad',
    options=['Reg', 'IR1', 'IR2', 'IR3']
)

land_contour = st.selectbox(
    'Planitud del terreno',
    options=['Lvl', 'Bnk Banked', 'HLS Hillside', 'Low Depression']
)

utilities = st.selectbox(
    'Tipo de servicios disponibles',
    options=['AllPub', 'NoSewr', 'NoSeWa', 'ELO']
)

lot_config = st.selectbox(
    'Configuración del terreno',
    options=['Inside', 'Corner', 'CulDSac', 'FR2', 'FR3']
)

land_slope = st.selectbox(
    'Pendiente de la propiedad',
    options=['Gtl', 'Mod', 'Sev']
)

neighborhood = st.selectbox(
    'Barrio',
    options=[
        'Blmngtn',
        'Blueste',
        'BrDale',
        'BrkSide',
        'ClearCr',
        'CollgCr',
        'Crawfor',
        'Edwards',
        'Gilbert',
        'IDOTRR',
        'MeadowV',
        'Mitchel',
        'Names',
        'NoRidge',
        'NPkVill',
        'NridgHt',
        'NWAmes',
        'OldTown',
        'SWISU',
        'Sawyer',
        'SawyerW',
        'Somerst',
        'StoneBr',
        'Timber',
        'Veenker'
    ]
)

condition1 = st.selectbox(
    'Proximidad a una condicion',
    options=['Artery', 'Feedr', 'Norm', 'RRNn', 'RRAn', 'PosN', 'PosA', 'RRNe', 'RRAe']
)

condition2 = st.selectbox(
    'Proximidad a una segunda condicion',
    options=['Artery', 'Feedr', 'Norm', 'RRNn', 'RRAn', 'PosN', 'PosA', 'RRNe', 'RRAe']
)

bldg_type = st.selectbox(
    'Tipo de edificación',
    options=['1Fam', '2FmCon', 'Duplx', 'TwnhsE', 'TwnhsI']
)

house_style = st.selectbox(
    'Estilo de edificación',
    options=['1Story', '1.5Fin', '1.5Unf', '2Story', '2.5Fin', '2.5Unf', 'SFoyer', 'SLvl']
)

overall_qual = st.slider(
    'Calidad general de la vivienda',
    min_value=1,
    max_value=10,
    value=5
)

overall_cond = st.slider(
    'Condicion general de la vivienda',
    min_value=1,
    max_value=10,
    value=5
)

year_built = st.number_input(
    'Año de construccion',
    min_value=1800,
    max_value=2026,
    value=2000,
    step=1
)

year_remod_add = st.number_input(
    'Año de remodelación',
    min_value=1800,
    max_value=2026,
    value=2000,
    step=1
)

roof_style = st.selectbox(
    'Estilo del techo',
    options=['Flat', 'Gable', 'Gambrel', 'Hip', 'Mansard', 'Shed']
)

roof_mat = st.selectbox(
    'Material del techo',
    options=['ClyTile', 'CompShg', 'Membran', 'Metal', 'Roll', 'Tar&Grv', 'WdShake', 'WdShngl']
)

exterior1st = st.selectbox(
    'Revestimiento de la parte exterior de la casa',
    options=[
        'AsbShng',
        'AsphShn',
        'BrkComm',
        'BrkFace',
        'CBlock',
        'CemntBd',
        'HdBoard',
        'ImStucc',
        'MetalSd',
        'Other',
        'Plywood',
        'PreCast',
        'Stone',
        'Stucco',
        'VinylSd',
        'Wd Sdng',
        'WdShing'
    ]
)

exterior2nd = st.selectbox(
    'Segundo revestimiento de la parte exterior de la casa',
    options=[
        'AsbShng',
        'AsphShn',
        'BrkComm',
        'BrkFace',
        'CBlock',
        'CemntBd',
        'HdBoard',
        'ImStucc',
        'MetalSd',
        'Other',
        'Plywood',
        'PreCast',
        'Stone',
        'Stucco',
        'VinylSd',
        'Wd Sdng',
        'WdShing'
    ]
)

mas_vnr_type = st.selectbox(
    'Tipo de revestimiento de mamposteria',
    options=['BrkCmn', 'BrkFace', 'CBlock', 'Stone', 'NoMasVnr', None]
)

# Aquí checkear la caja si es que se sabe el area de revestimiento
# Si no se sabe, solo queda None
know_mas_vnr_area = st.checkbox(
    'Conoces el área de revestimiento de mampostería?'
)
if know_mas_vnr_area:
    mas_vnr_area = st.number_input(
        'Área de revestimiento de mampostería',
        min_value=0.0,
        value=0.0,
        step=10.0
    )
else:
    mas_vnr_area = None


exter_qual = st.selectbox(
    'Calidad del material del exterior',
    options=['Ex', 'Gd', 'TA', 'Fa', 'Po']
)


exter_cond = st.selectbox(
    'Condición del material del exterior',
    options=['Ex', 'Gd', 'TA', 'Fa', 'Po']
)


foundation = st.selectbox(
    'Tipo de cimentación',
    options=['BrkTil', 'CBlock', 'PConc', 'Slab', 'Stone', 'Wood']
)


have_basement = st.checkbox(
    'La vivienda contiene sótano?'
)
if have_basement:
    bsmt_qual = st.selectbox(
        'Altura del sótano',
        options=['Ex', 'Gd', 'TA', 'Fa', 'Po']
    )
    bsmt_cond = st.selectbox(
        'Condiciones del sótano',
        options=['Ex', 'Gd', 'TA', 'Fa', 'Po']
    )
    bsmt_exposure = st.selectbox(
        'Exposición del sótano (paredes que dan hacia el exterior)',
        options=['Gd', 'Av', 'Mn', 'No']
    )
    bsmt_fin_type1 = st.selectbox(
        'Calificación del area terminada del sótano tipo 1',
        options=['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf']
    )
    bsmt_fin_sf1 = st.number_input(
        'Sótano tipo 1 terminado en pies cuadrados',
        min_value=0,
        value=10,
        step=10
    )
    bsmt_fin_type2  = st.selectbox(
        'Calificación del area terminada del sótano tipo 2',
        options=['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf']
    )
    bsmt_fin_sf2 = st.number_input(
        'Sótano tipo 2 terminado en pies cuadrados',
        min_value=0,
        value=10,
        step=10
    )
    bsmt_unf_sf = st.number_input(
        'Pies cuadrados no terminados del sótano',
        min_value=0,
        value=0,
        step=10
    )
    total_bsmt_sf = st.number_input(
        'Área total del sótano en pies cuadrados',
        min_value=1,
        value=10,
        step=10
    )
else:
    bsmt_qual = 'NoBasement'
    bsmt_cond = 'NoBasement'
    bsmt_exposure = 'NoBasement'
    bsmt_fin_type1 = 'NoBasement'
    bsmt_fin_sf1 = 0
    bsmt_fin_type2  = 'NoBasement'
    bsmt_fin_sf2 = 0
    bsmt_unf_sf = 0
    total_bsmt_sf = 0


heating = st.selectbox(
    'Tipo de calefacción',
    options=['Floor', 'GasA', 'GasW', 'Grav', 'OthW', 'Wall']
)


heating_qc = st.selectbox(
    'Calidad y condición de calefacción',
    options=['Ex', 'Gd', 'TA', 'Fa', 'Po']
)


central_air = st.selectbox(
    'Aire acondicionado central',
    options=['N', 'Y']
)


electrical = st.selectbox(
    'Sistema electrico',
    options=['SBrkr', 'FuseA', 'FuseF', 'FuseP', 'Mix']
)


first_floor_sf = st.number_input(
    'Pies cuadrados del primer piso',
    min_value=1,
    value=10,
    step=10
)


second_floor_sf = st.number_input(
    'Pies cuadrados del segundo piso',
    min_value=0,
    value=10,
    step=10
)


low_qual_fin_sf = st.number_input(
    'Pies cuadrados terminados de baja calidad',
    min_value=0,
    value=0,
    step=10
)


gr_liv_area = st.number_input(
    'Pies cuadrados de superficie habitable (por encima del nivel del suelo)',
    min_value=1,
    value=10,
    step=10
)


if have_basement:
    bsmt_full_bath = st.number_input(
        'Baños completos en el sótano',
        min_value=0,
        value=0,
        step=1
    )
    bsmt_half_bath = st.number_input(
        'Baños sin terminar en el sótano',
        min_value=0,
        value=0,
        step=1
    )
else:
    bsmt_full_bath = 0
    bsmt_half_bath = 0


full_bath = st.number_input(
    'Baños completos',
    min_value=0,
    value=1,
    step=1
)


half_bath = st.number_input(
    'Baños incompletos',
    min_value=0,
    value=1,
    step=1
)


bedroom_abv_gr = st.slider(
    'Dormitorios por sobre el nivel del suelo',
    min_value=0,
    max_value=10,
    value=1,
    step=1
)


kitchen_abv_gr = st.slider(
    'Cocinas por sobre el nivel del suelo',
    min_value=0,
    max_value=5,
    value=1,
    step=1
)


kitchen_qual = st.selectbox(
    'Calidad de la cocina',
    options=['Ex', 'Gd', 'TA', 'Fa', 'Po']
)


tot_rms_abv_grd = st.slider(
    'Total de habitaciones por sobre el nivel del suelo',
    min_value=0,
    max_value=20,
    value=1,
    step=1
)


functional = st.selectbox(
    'Funcionalidad de la vivienda',
    options=['Typ', 'Min1', 'Min2', 'Mod', 'Maj1', 'Maj2', 'Sev', 'Sal']
)


fireplaces = st.slider(
    'Número de chimeneas',
    min_value=0,
    max_value=3,
    value=0,
    step=1
)


fireplace_qu = st.selectbox(
    'Calidad de la chimenea',
    options=['Ex', 'Gd', 'TA', 'Fa', 'Po', None]
)


has_garage = st.checkbox(
    'La vivienda contiene garage?'
)
if has_garage:
    garage_type = st.selectbox(
        'Tipo de garage',
        options=['2Types', 'Attchd', 'Basment', 'BuiltIn', 'CarPort', 'Detchd']
    )
    garage_yr_blt = st.number_input(
        'Año de construcción del garage',
        min_value=1800,
        max_value=2026,
        value=2000,
        step=1
    )
    garage_finish = st.selectbox(
        'Acabado interior del garage',
        options=['Fin', 'RFn', 'Unf']
    )
    garage_cars = st.slider(
        'Capacidad del garage en autos',
        min_value=1,
        max_value=5,
        step=1
    )
    garage_area = st.number_input(
        'Area del garage, en pies cuadrados',
        min_value=1,
        step=10
    )
    garage_qual = st.selectbox(
        'Calidad del garage',
        options=['Ex', 'Gd', 'TA', 'Fa', 'Po']
    )
    garage_cond = st.selectbox(
        'Condiciones del garage',
        options=['Ex', 'Gd', 'TA', 'Fa', 'Po']
    )
else:
    garage_type = 'NoGarage'
    garage_yr_blt = 0
    garage_finish = 'NoGarage'
    garage_cars = 0
    garage_area = 0
    garage_qual ='NoGarage'
    garage_cond ='NoGarage'


paved_drive = st.selectbox(
    'Camino de acceso pavimentado',
    options=['Y', 'P', 'N']
)


wood_deck = st.number_input(
    'Area de la plataforma de madera, en pies cuadrados',
    min_value=0,
    value=50,
    step=10
)


open_porch = st.number_input(
    'Superficie del porche abierto, en pies cuadrados',
    min_value=0,
    value=25,
    step=10
)


enclosed_porch = st.number_input(
    'Superficie del porche cerrado, en pies cuadrados',
    min_value=0,
    value=25,
    step=10
)


three_season_porch_area = st.number_input(
    'Superficie del porche para 3 estaciones, en pies cuadrados',
    min_value=0,
    value=0,
    step=10
)


screen_porch = st.number_input(
    'Superficie del porche con mosquiteras, en pies cuadrados',
    min_value=0,
    value=0,
    step=10
)


has_pool = st.checkbox(
    'La vivienda tiene piscina?'
)
if has_pool:
    pool_area = st.number_input(
        'Area de la piscina, en pies cuadrados',
        min_value=0,
        value=0,
        step=10
    )
    pool_qc = st.selectbox(
        'Calidad de la piscina',
        options=['Ex', 'Gd', 'TA', 'Fa']
    )
else:
    pool_area = 0
    pool_qc = 'NoPool'


fence = st.selectbox(
    'Calidad de la cerca',
    options=['GdPrv', 'MnPrv', 'GdWo', 'MnWW', 'NoFence']
)


has_misc_feature = st.checkbox(
    'La vivienda contiene alguna otra característica o funcionalidad no mencionada en otras categorías?'
)
if has_misc_feature:
    misc_feature = st.selectbox(
        'Característica/funcionalidad no contemplada en otras categorias',
        options=['Shed', 'Gar2', 'Othr', 'TenC']
    )
    misc_val = st.number_input(
        'Valor de la funcionalidad diversa',
        min_value=1,
        value=100,
        step=100
    )
else:
    misc_feature = 'NoMisceFeat'
    misc_val = 0


mo_sold = st.slider(
    'Mes de venta',
    min_value=1,
    max_value=12,
    value=1,
    step=1
)


yr_sold = st.number_input(
    'Año de venta',
    min_value=1800,
    value=2000,
    step=1
)


sale_type = st.selectbox(
    'Tipo de venta',
    options=['WD', 'CWD', 'VWD', 'New', 'COD', 'Con', 'ConLw', 'ConLI', 'ConLD', 'Oth']
)


sale_condition = st.selectbox(
    'Condición de venta',
    options=['Normal', 'Abnormal', 'AjdLand', 'Alloca', 'Family', 'Partial']
)






if st.button('REALIZAR PREDICCIÓN'):

    json_to_send = {
        'MSSubClass': ms_sub_class,
        'MSZoning': ms_zoning,
        'LotFrontage': lot_frontage,
        'LotArea': lot_area,
        'Street': street,
        'Alley': alley,
        'LotShape': lot_shape,
        'LandContour': land_contour,
        'Utilities': utilities,
        'LotConfig': lot_config,
        'LandSlope': land_slope,
        'Neighborhood': neighborhood,
        'Condition1': condition1,
        'Condition2': condition2,
        'BldgType': bldg_type,
        'HouseStyle': house_style,
        'OverallQual': overall_qual,
        'OverallCond': overall_cond,
        'YearBuilt': year_built,
        'YearRemodAdd': year_remod_add,
        'RoofStyle': roof_style,
        'RoofMatl': roof_mat,
        'Exterior1st': exterior1st,
        'Exterior2nd': exterior2nd,
        'MasVnrType': mas_vnr_type,
        'MasVnrArea': mas_vnr_area,
        'ExterQual': exter_qual,
        'ExterCond': exter_cond,
        'Foundation': foundation,
        'BsmtQual': bsmt_qual,
        'BsmtCond': bsmt_cond,
        'BsmtExposure': bsmt_exposure,
        'BsmtFinType1': bsmt_fin_type1,
        'BsmtFinSF1': bsmt_fin_sf1,
        'BsmtFinType2': bsmt_fin_type2,
        'BsmtFinSF2': bsmt_fin_sf2,
        'BsmtUnfSF': bsmt_unf_sf,
        'TotalBsmtSF': total_bsmt_sf,
        'Heating': heating,
        'HeatingQC': heating_qc,
        'CentralAir': central_air,
        'Electrical': electrical,
        '1stFlrSF': first_floor_sf,
        '2ndFlrSF': second_floor_sf,
        'LowQualFinSF': low_qual_fin_sf,
        'GrLivArea': gr_liv_area,
        'BsmtFullBath': bsmt_full_bath,
        'BsmtHalfBath': bsmt_half_bath,
        'FullBath': full_bath,
        'HalfBath': half_bath,
        'BedroomAbvGr': bedroom_abv_gr,
        'KitchenAbvGr': kitchen_abv_gr,
        'KitchenQual': kitchen_qual,
        'TotRmsAbvGrd': tot_rms_abv_grd,
        'Functional': functional,
        'Fireplaces': fireplaces,
        'FireplaceQu': fireplace_qu,
        'GarageType': garage_type,
        'GarageYrBlt': garage_yr_blt,
        'GarageFinish': garage_finish,
        'GarageCars': garage_cars,
        'GarageArea': garage_area,
        'GarageQual': garage_qual,
        'GarageCond': garage_cond,
        'PavedDrive': paved_drive,
        'WoodDeckSF': wood_deck,
        'OpenPorchSF': open_porch,
        'EnclosedPorch': enclosed_porch,
        '3SsnPorch': three_season_porch_area,
        'ScreenPorch': screen_porch,
        'PoolArea': pool_area,
        'PoolQC': pool_qc,
        'Fence': fence,
        'MiscFeature': misc_feature,
        'MiscVal': misc_val,
        'MoSold': mo_sold,
        'YrSold': yr_sold,
        'SaleType': sale_type,
        'SaleCondition': sale_condition
    }

    # Obtener variable de entorno, si se ejecuta en Docker obtiene API_URL
    # de no ejecutarse en Docker obtiene la dirección 127...
    api_url = os.getenv(
        'API_URL',
        'http://127.0.0.1:8000/predict'
    )

    # Enviar una request con metodo post a la url, esto podría enviarse
    # al servicio de "api" dentro de Docker o a la dirección del propio PC
    response = requests.post(
        api_url,
        json=json_to_send,
        timeout=30
    )

    # Convertimos a json la respuesta
    response_json = response.json()

    # Obtenemos el valor donde la clave es 'prediction', ya que /predict dentro
    # de fastapi devuelve algo como:
    #{
    #   "prediction": prediction
    #}
    response_int = response_json['prediction']

    # Crear metrica y ponerle el precio (metric es para que se vea mejor, podria ser write, title, etc)
    st.metric(
        'Precio estimado',
        value=f'${response_int:.2f}'
    )

    