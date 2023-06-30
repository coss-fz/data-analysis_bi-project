
"""
Script in charge to realize the unit tests
for "functions.py"
"""


import sys
sys.path.append("./")

import pytest

import pandas as pd

from src.functions import DataAnalyzer




def test_DataAnalyzer():
    """
    This function tests the Class 'DataAnalyzer'
    """

    ##Valid DataFrame
    df = pd.DataFrame(
        {
            'col_1': [1, 2, 3, 4],
            'col_2': [5.0, 5.1, 5.2, 5.3],
            'col_3': [True, False, None, False],
            'col_4': ["str_1", "str_2", "str_3", "str_4"],
        }
    )
    analyzer = DataAnalyzer(df)
    assert isinstance(analyzer.df, pd.core.frame.DataFrame)

    ##Object tha is not a DataFrame
    not_df = {"key_1":"value", "key_2":2.7}
    with pytest.raises(TypeError):
        DataAnalyzer(not_df)
