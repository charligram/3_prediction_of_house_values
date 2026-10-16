from pydantic import BaseModel, Field


# Detalle: Se añade alias a algunos atributos debido a que el atributo original empieza por un número
class PredictionInput(BaseModel):
    MSSubClass: str
    MSZoning: str
    LotFrontage: float
    LotArea: int
    Street: str
    Alley: str | None
    LotShape: str
    LandContour: str
    Utilities: str
    LotConfig: str
    LandSlope: str
    Neighborhood: str
    Condition1: str
    Condition2: str
    BldgType: str
    HouseStyle: str
    OverallQual: int
    OverallCond: int
    YearBuilt: int
    YearRemodAdd: int
    RoofStyle: str
    RoofMatl: str
    Exterior1st: str
    Exterior2nd: str
    MasVnrType: str | None
    MasVnrArea: float | None
    ExterQual: str
    ExterCond: str
    Foundation: str
    BsmtQual: str
    BsmtCond: str
    BsmtExposure: str
    BsmtFinType1: str
    BsmtFinSF1: int
    BsmtFinType2: str
    BsmtFinSF2: int
    BsmtUnfSF: int
    TotalBsmtSF: int
    Heating: str
    HeatingQC: str
    CentralAir: str
    Electrical: str
    first_floor_square_feets: int = Field(alias='1stFlrSF')
    second_floor_square_feets: int = Field(alias='2ndFlrSF')
    LowQualFinSF: int
    GrLivArea: int
    BsmtFullBath: int
    BsmtHalfBath: int
    FullBath: int
    HalfBath: int
    BedroomAbvGr: int
    KitchenAbvGr: int
    KitchenQual: str
    TotRmsAbvGrd: int
    Functional: str
    Fireplaces: int
    FireplaceQu: str | None
    GarageType: str
    GarageYrBlt: float
    GarageFinish: str
    GarageCars: int
    GarageArea: int
    GarageQual: str
    GarageCond: str
    PavedDrive: str
    WoodDeckSF: int
    OpenPorchSF: int
    EnclosedPorch: int
    three_season_porch_area: int = Field(alias='3SsnPorch')
    ScreenPorch: int
    PoolArea: int
    PoolQC: str | None
    Fence: str
    MiscFeature: str
    MiscVal: int
    MoSold: int
    YrSold: int
    SaleType: str
    SaleCondition: str