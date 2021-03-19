class HelperFunctions:
    def __init__(self):
        pass

    @staticmethod
    def null_count(df):
        return df.isnull().sum().sum()

    @staticmethod
    def list_2_series(list_2_series, df):
        df['list'] = list_2_series
        return df
