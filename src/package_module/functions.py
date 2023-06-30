
"""
Script that contains all the Classes and functions
that will be used in the project
"""


import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt




def even_numbers_filter(lista_inicial:list) -> list:
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

    @staticmethod
    def dispersion_graph(x_data:pd.core.series.Series, y_data:pd.core.series.Series) -> None:

        plt.figure(figsize=(10,6))

        plt.title("Dispersion Graphic")
        plt.xlabel(x_data.name)
        plt.ylabel(y_data.name)

        plt.scatter(x_data, y_data)

        plt.show()

        return None

    @staticmethod
    def histogram(data:pd.core.series.Series) -> None:

        plt.figure(figsize=(10,6))

        plt.title(f"Histogram for the distribution of '{data.name}'")
        plt.xlabel(data.name)
        plt.ylabel("Quantity")

        data.hist(figsize=(10,6))

        plt.show()

        return None
