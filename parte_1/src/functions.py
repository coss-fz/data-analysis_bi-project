
"""
Script que contiene todas las clases y funciones
que serán utilizadas en el código principal
"""


import warnings
warnings.filterwarnings("ignore")

import pandas as pd




def filtro_numeros_pares(lista_inicial:list) -> list:
    """
    Esta función filtra una lista para dejar solo
    los números pares en ella

    Parameters:
        lista_inicial: lista con los números iniciales

    Returns:
        lista_filtrada: lista solo con los números pares
    """

    lista_pares = []
    for num in lista_inicial:
        if num % 2 == 0:
            lista_pares.append(num)
    return lista_pares


class DataAnalyzer:
    """
    Clase que instancia un objeto como DataFrame
    """
    
    def __init__(self, df:pd.core.frame.DataFrame) -> None:

        if not isinstance(df, pd.core.frame.DataFrame):
            raise TypeError("Se esperaba un objeto DataFrame de Pandas")
        
        self.df = df
