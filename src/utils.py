import pandas as pd


def simple_report(df: pd.DataFrame, feature: str, show_categories: bool = False):

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

