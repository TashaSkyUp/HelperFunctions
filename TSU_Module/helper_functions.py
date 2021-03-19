"""Helper functions for datascience
    -By Natasha Upchurch
"""
class HelperFunctions:
    """Base Class
    """

    def __init__(self):
        pass

    @staticmethod
    def null_count(df):
        """:param df pandas.DataFrame to count nulls on
        """
        return df.isnull().sum().sum()

    @staticmethod
    def list_2_series(list_2_series, df):
        """ adds a new column named "list" to the dataframe with contents being list_2_series
        :param df pandas.DataFrame to count nulls on
        :param list_2_series list to add as feature/ column of the dataframe
        """
        df['list'] = list_2_series
        return df
