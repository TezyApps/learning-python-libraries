#region imports

import pandas as pd
from matplotlib import pyplot as plt
# import matplotlib.pyplot as plt

from utils import log_title as lt, log_body as lb

#endregion

#region PyPlotExample Class

class PyPlotExample():

    #region - Constructor
    
    def __init__(self, csv_file_path) -> None:
        self.__csv_file_path = csv_file_path
        self.__data = pd.read_csv(csv_file_path)

    #endregion

    #region - Properties

    @property
    def data(self) -> pd.DataFrame:
        return self.__data

    #endregion

    #region - Public Methods

    def data_overview(
            self, 
            show_records: bool = False, 
            show_shape = True, 
            describe = False, 
            show_data_types = False
        ) -> None: 
        lt(f"Data : {self.__csv_file_path}")
        if show_records:
            lt('Top 5 Records')
            lb(self.data.head())
            # print(self.data.head(), end="\n\n")
        if show_shape:
            lt('Data Shape')
            lb(self.data.shape)
        if describe:
            lt('Describe the Data')
            lb(self.data.describe())
        if show_data_types:
            lt('Data Types')
            lb(self.data.dtypes)

    def univariate_analysis(self):
        pass

    def bivariate_analysis(self):
        pass

    def multivariate_analysis(self):
        pass

    #endregion
    
    #region - Private Methods

    #endregion

#endregion