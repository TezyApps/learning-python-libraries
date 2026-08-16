
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
# import matplotlib.pyplot as plt

from utils import log_title as lt, log_body as lb

class PyPlotExample():
    
    def __init__(self, csv_file_path) -> None:
        self.__csv_file_path = csv_file_path
        self.__data = pd.read_csv(csv_file_path)

    @property
    def data(self) -> pd.DataFrame:
        return self.__data
    
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

    def univariate_analysis(self, col: str):
        self.__hist_mpg(col)

    def bivariate_analysis(self):
        self.__bar_chart('cyl', 'mpg')

    def multivariate_analysis(self):
        self.__pairplot()

    #region - Private methods
    
    def __hist_mpg(self, col: str):
        plt.hist(x = self.data[col])
        plt.show()

    def __bar_chart(self, x_axis_discrete: str, y_axis_continuous: str):
        # plt.bar(self.data[x_axis_discrete], height=self.data[y_axis_continuous])
        sns.barplot(self.data, x=x_axis_discrete, y=y_axis_continuous)
        plt.show()

    def __pairplot(self):
        sns.pairplot(self.data)
        plt.show()

    #endregion