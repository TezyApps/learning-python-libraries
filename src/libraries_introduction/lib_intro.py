import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def __plot(df: pd.DataFrame):
    plt.hist(x=df['attendance_percent'])
    plt.show() # required in vscode, to display the graph in external window.

def __students_by_gender(df: pd.DataFrame) -> None:
    genders = df["gender"].to_numpy()
    values, counts = np.unique(genders, return_counts = True)
    result = dict(zip(values, counts))
    heading = "Gender\t:\tCount"
    print("\n")
    print("=" * (len(heading) + 8))
    print(heading)
    print("=" * (len(heading) + 8))
    for gender, count in result.items():
        print(f"{gender}\t:\t{int(count)}")
    print("=" * (len(heading) + 8))
    print("\n")

def __get_data() -> pd.DataFrame:
    print("Exploring pandas library")
    data_set = pd.read_csv("resources/datasets/student-performance.csv")
    return data_set

def intro_to_libraries(show: bool = True) -> None:
    if show:
        print("Intro to libraries")
        df = __get_data()
        __students_by_gender(df)
        __plot(df=df)
        print("End intro to libraries\n")