import pandas as pd

def __test_pandas_lib() -> None:
    print("Exploring pandas library")
    data_set = pd.read_csv("resources/datasets/student-performance.csv")
    print(type(data_set))

def main() -> None:
    print("Hello from libraries-introduction!")
    __test_pandas_lib()
