
from .matplot import matplot_example as mp

student_performance_csv_data = 'resources/datasets/student-performance.csv'
mtcars_csv_file_path = 'resources/datasets/mtcars.csv'

def mtcar_examples():
    plt_obj = mp.PyPlotExample(mtcars_csv_file_path)
    # plt_obj.data_overview(show_records=True, describe = True)
    # plt_obj.univariate_analysis('mpg')

    plt_obj.bivariate_analysis()

    # plt_obj.multivariate_analysis()

def main() -> None:
    print("Hello from Charts 📊 !")
    mtcar_examples()
