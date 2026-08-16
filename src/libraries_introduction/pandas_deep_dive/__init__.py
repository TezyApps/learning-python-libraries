
from . import lesson as l
from utils import log_title as lt

def explore_data_set(file_path: str):
    student_performance_dataframe = l.load_data(file_path)

    lt("Loaded students data")
    print(student_performance_dataframe)

    lt("Describing data")
    l.describe_data(student_performance_dataframe)

    lt("Check for Data Quality")
    l.check_for_data_quality(student_performance_dataframe)

    lt("Describe the data types")
    l.show_cols_data_types(student_performance_dataframe)

    print("\n")