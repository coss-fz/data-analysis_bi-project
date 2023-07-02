
"""
Script in charge to realize the unit tests
for "functions.py"
"""


import sys
sys.path.append("./")

import pytest

import pandas as pd

from src.package_module.functions import DataAnalyzer, even_numbers_filter




def test_even_numbers_filter():
    """
    This function tests the function 'even_numbers_filter'
    """

    initial_list = [-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10,11,12]
    expected_output = [-12, -10, -8, -6, -4, -2, 2, 4, 6, 8, 10, 12]

    list_even = even_numbers_filter(initial_list)
    
    assert isinstance(list_even, list)
    assert even_numbers_filter(list_even) == expected_output


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
