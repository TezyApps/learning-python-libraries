
import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    print(f"Loading data for : {file_path}")
    student_performance = pd.read_csv(file_path)
    return student_performance

def describe_data(student_dataframe: pd.DataFrame):
    result = student_dataframe.describe()
    print(result, "\n", type(result))

def check_for_data_quality(data: pd.DataFrame):
    print(data.duplicated().sum())
    print(data.isnull().sum())

def show_cols_data_types(data: pd.DataFrame):
    print(data.dtypes)