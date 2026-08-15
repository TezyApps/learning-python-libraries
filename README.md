# Libraries

Set of functions, modules, and classes where it has pre-written codes to perform some tasks.

> [!TIP]
> what's `pip`
> pip - Preffered Installer Programmer

## Learnings so far

A snapshot of what's been covered in this project (see commit history for the full trail):

- **Project setup** — scaffolded with `uv`, added `pandas`, `numpy`, and `matplotlib` as
  dependencies (`Add pandas as dependencies`, `Adding numpy as deps`, `Adding matplotlib deps`),
  and fixed up `.gitignore`.
- **Core data structures** — revisited plain Python `list` (indexing, including negative
  indices) and `set` (unordered, unique values — duplicate `.add()` calls are silently
  ignored) in `data_structures.py`.
- **Reading real data** — loaded a CSV sample dataset (`resources/datasets/student-performance.csv`)
  with `pandas.read_csv()` as the first hands-on pandas exercise.
- **First numpy + pandas combo** — pulled a DataFrame column out as a numpy array
  (`df["gender"].to_numpy()`) and used `np.unique(..., return_counts=True)` to count students
  per gender, then pretty-printed the result as a table (`lib_intro.py`).
- **First plot** — used `matplotlib.pyplot.hist()` to visualize the `attendance_percent`
  column as a histogram, calling `plt.show()` to render it (needed explicitly in VS Code).
- **Datatypes classification** — learned the discrete vs. continuous distinction for data
  (see below).
- **Modularizing the code** — extracted the ad-hoc examples into their own modules
  (`data_structures.py`, `lib_intro.py`) and added a small `utils` module with `log_title()`
  for consistent section headers in console output.
- **Pandas deep dive** — scaffolded a dedicated `pandas_deep_dive` package
  (`lesson.py` + `__init__.py`) with reusable functions for exploring a DataFrame:
  - `load_data()` — read a CSV into a DataFrame
  - `describe_data()` — summary statistics via `DataFrame.describe()`
  - `check_for_data_quality()` — duplicate rows (`.duplicated().sum()`) and missing values
    (`.isnull().sum()`) per column
  - `show_cols_data_types()` — inspect column dtypes via `.dtypes`
  - Wired together in `explore_data_set()`, using `utils.log_title()` to label each step's
    output.
- **Dataset resources** — collected a list of places to find free sample datasets (Excel
  and CSV) for further pandas practice (see below).

## Pandas library:

```py
# For Data Analysis
import pandas as pd

# For playing with numbers or numerical installations
import numpy as np

# for data visualization - matplotlib, Seaborn, plotly
from matplotlib import pyplot as plt
# or
import matplotlib.pyplot as plt
```

## Types of Datatypes:

1. Discrete  - Countable, it will never have any units, you can't measure that
2. Continuos - It will have units, it's measurable

## DataSets - Resources

Free sample datasets for practicing with `pandas` (many available as Excel/`.xlsx`):

- [Kaggle](https://www.kaggle.com/datasets) — huge variety, most downloadable as CSV, many also as Excel; good filters for size/format.
- Microsoft's own sample data — the classic "Financial Sample.xlsx" and other sample workbooks bundled with Excel (File → New → search "sample data" in templates), also downloadable from Microsoft's docs/support pages.
- [data.gov](https://data.gov) — US government datasets, many offer XLSX export alongside CSV/JSON.
- [UCI Machine Learning Repository](https://archive.ics.uci.edu) — mostly CSV, but small enough to open/convert in Excel easily.
- [World Bank Open Data](https://data.worldbank.org) — has an "Excel" download option for most indicators.
- [Our World in Data](https://ourworldindata.org) — CSV primarily, but easy to open in Excel.
- [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets) — curated GitHub list across many domains/formats.

For pandas practice, `pandas.read_excel()` works directly off any `.xlsx` downloaded from these — Kaggle and Microsoft's sample workbooks are the fastest way to get a realistic multi-sheet Excel file to experiment with (pivoting, merges, multiple sheets via `sheet_name=None`, etc.).
