
"""
Script that contains all the Classes and functions
that will be used in the project
"""


import warnings
warnings.filterwarnings("ignore")

import pandas as pd




def filtro_numeros_pares(lista_inicial:list) -> list:
    """
    This functions filters a list in order to 
    maintain only the even numbers

    Parameters:
        lista_inicial: lista with the initial numbers

    Returns:
        lista_filtrada: lista with only even numbers
    """

    lista_pares = []
    for num in lista_inicial:
        if num % 2 == 0:
            lista_pares.append(num)
    return lista_pares


class DataAnalyzer:
    """
    Class that initialize an object as DataFrame
    """
    
    def __init__(self, df:pd.core.frame.DataFrame) -> None:

        if not isinstance(df, pd.core.frame.DataFrame):
            raise TypeError(f"A Pandas DataFrame is expected, got a {type(df)}")
        
        self.df = df
