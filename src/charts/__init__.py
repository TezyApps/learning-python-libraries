
from pydoc import describe

from .matplot import matplot_example as mp

student_performance_csv_data = 'resources/datasets/student-performance.csv'
mtcars_csv_file_path = 'resources/datasets/mtcars.csv'

def pyplot_examples():
    plt_obj = mp.PyPlotExample(mtcars_csv_file_path)
    plt_obj.data_overview(show_records=True, describe = True)


def main() -> None:
    print("Hello from Charts 📊 !")
    pyplot_examples()