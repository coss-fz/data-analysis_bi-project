
"""
Script que contiene el módulo para la clase 'DataAnalyzer'
"""


import warnings
warnings.filterwarnings("ignore")

import pandas as pd




class DataAnalyzer:
    """
    Clase que instancia un objeto como DataFrame
    """
    
    def __init__(self, df:pd.core.frame.DataFrame) -> None:

        if not isinstance(df, pd.core.frame.DataFrame):
            raise TypeError("Se esperaba un objeto DataFrame de Pandas")
        
        self.df = df
        