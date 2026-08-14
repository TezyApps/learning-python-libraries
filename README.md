# Libraries

Set of functions, modules, and classes where it has pre-written codes to perform some tasks.

![TIP]: 
> what's `pip`
> pip - Preffered Installer Programmer

## Pandas library:

- For Data Analysis

```py
import pandas as pd
```

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