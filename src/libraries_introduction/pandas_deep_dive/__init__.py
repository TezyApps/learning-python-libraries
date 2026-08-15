
from . import lesson as l
from .. import utils as ut

def explore_data_set(file_path: str):
    student_performance_dataframe = l.load_data(file_path)

    ut.log_title("Loaded students data")
    print(student_performance_dataframe)

    ut.log_title("Describing data")
    l.describe_data(student_performance_dataframe)

    ut.log_title("Check for Data Quality")
    l.check_for_data_quality(student_performance_dataframe)

    ut.log_title("Describe the data types")
    l.show_cols_data_types(student_performance_dataframe)

    print("\n")