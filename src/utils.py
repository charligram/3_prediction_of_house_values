import pandas as pd


def simple_report(df: pd.DataFrame, feature: str, show_categories: bool = False):
    """
    Genera un reporte simple con la cantidad de nulos, el dtype y el número de categorías totales.
    Opcionalmente se pueden mostrar las categorías posiibles.

    Args:
        df (DataFrame): DataFrame que contiene la información
        feature (str): Nombre de la columna a investigar
        show_categories (bool): Por defecto False. Con True la función muestra las categorías dentro del feature

    Returns:
        Imprime el siguiente formato:

            Nulls: {nulls_count}

            Dtype: {type_of_feature}

            Total categories: {total_categories}

            Categories: {categories}
    """


    nulls_count = df[feature].isna().sum()
    type_of_feature = df[feature].dtype
    total_categories = df[feature].nunique()

    if show_categories:
        categories = df[feature].unique()

        if type_of_feature == 'str':
            categories = list(categories)

        print(f"""
Nulls: {nulls_count}
Dtype: {type_of_feature}
Total categories: {total_categories}
Categories: {categories}
""")
        
    else:
        print(f"""
Nulls: {nulls_count}
Dtype: {type_of_feature}
Total categories: {total_categories}
""")

