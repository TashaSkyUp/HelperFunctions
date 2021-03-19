import pytest


def test_null_count():
    from helper_functions import HelperFunctions
    import pandas as pd
    test_df = pd.DataFrame.from_dict   ({'a': [float('nan')], 'b': [float('nan')]})
    assert HelperFunctions.null_count(test_df) == 2
