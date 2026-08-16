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
- **OOP fundamentals** — see the dedicated [OOP section](#oop---object-oriented-programming)
  below for the class-encapsulation exercise and the four-pillars vehicle rental exercise.

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

## ML / DS - Terminologies

For a pandas DataFrame of shape `(1000, 12)` (1000 rows, 12 columns):

- ✅ **"1000 observations & 12 features"** — standard ML/DS terminology. Rows = observations
  (also called samples/instances), columns = features (also called variables/attributes/
  predictors).
- ⚠️ **"1000 records & 12 parameters"** — half right:
  - "records" for rows is fine (a common, more database-flavored synonym for observations).
  - "parameters" for columns is a common mix-up. In ML/statistics, a **parameter** is a value
    the *model learns* during training (e.g. regression coefficients, neural net weights) —
    not an input column. Columns should be called **features**, never parameters.

| Term | Refers to |
|---|---|
| observation / sample / record / instance | a row |
| feature / variable / attribute / predictor | a column (input) |
| parameter | a value the model learns (e.g. weights, coefficients) |
| hyperparameter | a value *you* set before training (e.g. learning rate, `k` in k-NN) |

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

## OOP - Object Oriented Programming

### `Office` — encapsulation warm-up (`oops_intro.py`)

A small class modelling a manager/employee with private user data, built before moving
on to the four pillars:

```
        Office
 ─────────────────────
 - __user_data: dict
 - __name: str          (private property, derived from __user_data['name'])
 ─────────────────────
 + __init__(user_data: dict)
 + login(password: str) -> None
 + view_tasks() -> list
 + add_task(task: str) -> None   (role-gated: only 'manager' can add tasks)
```

- `__user_data` is a private (name-mangled) instance attribute — there's no way to reach it
  from outside as `office.__user_data`; Python rewrites it to `office._Office__user_data`.
- `__name` is a private `@property`, computed on the fly from `__user_data['name']` rather
  than stored separately.
- `add_task()` demonstrates role-based access control purely through a plain `if` check on
  the object's own private state — no inheritance needed for this one.

### Vehicle Rental — all four pillars (`exercise/vehicle_rental.py`)

```
        <<abstract>>
          Vehicle
 ─────────────────────────
 - brand: str
 - _speed: int
 - __battery_level: int
 + total_vehicles: int = 0        (class variable, shared across all instances)
 ─────────────────────────
 + __init__(brand: str)
 + speed (property getter/setter, clamped 0–200 via _clamped())
 + battery_level (property getter/setter, clamped 0–200 via _clamped())
 + abstract make_sound() -> str
 + abstract fuel_type() -> str
 + describe() -> str                    (concrete, calls make_sound() + fuel_type())
 + classmethod get_total_vehicles() -> int
        △
        │ inherits
   ┌────┴────┐
   │         │
  Car       Bike
 ──────    ──────
 + doors: int      + has_carriers: bool
 + make_sound()    + make_sound()
 + fuel_type()     + fuel_type()
```

Module-level helper (outside the class, so it isn't name-mangled):
```py
def _clamped(value: int, min_value: int = 0, max_value: int = 200) -> int:
    return max(min_value, min(value, max_value))
```

Built up over several commits (`Define Vehicle Abstract Class` → `Partial implementation`
→ `Fix constructors in child classes` → `Fix dunder __init(...) typo` → name-mangling fix
→ `Fix smell in property setters` → `Test the OOPS implementation`), debugging real mistakes
along the way instead of getting it right on the first try:

- **Abstraction** — `Vehicle(ABC)` with `@abstractmethod` on `make_sound()`/`fuel_type()`.
  Trying `Vehicle("test")` directly raises `TypeError: Can't instantiate abstract class
  Vehicle...` — verified in `__oops_practice()` with a `try`/`except TypeError`.
- **Encapsulation** — `speed` and `battery_level` are real `@property`/`@x.setter` pairs
  backed by `_speed` / name-mangled `__battery_level`, both routed through the shared
  `_clamped()` helper so out-of-range values (e.g. `speed=220`) get silently clamped
  instead of accepted as-is.
- **Inheritance** — `Car` and `Bike` both extend `Vehicle`, call `super().__init__(brand)`,
  add their own field (`doors` / `has_carriers`), and reuse the concrete `describe()`
  method for free.
- **Polymorphism** — `make_sound()`/`fuel_type()` are overridden per subclass. Looping over
  `[car, bike]` and calling `.describe()` on each — the exact same method call — prints
  `"vroom, Petrol"` for the car and `"dubudubu, Petrol"` for the bike.
- **Class-level shared state** — `total_vehicles` is a class attribute incremented in
  `Vehicle.__init__`, exposed both directly (`Vehicle.total_vehicles`) and via
  `Vehicle.get_total_vehicles()` (a `@classmethod`) — confirmed both report the same shared
  count regardless of whether the instances were `Car`s or `Bike`s.

**Bugs hit and fixed along the way** (the actual learning, not just the final code):

- `def __init(self, ...)` (missing a trailing underscore) silently isn't the constructor —
  Python only special-cases the exact name `__init__`. Classes fell back to `object`'s
  default constructor, so `Car("Mazda 3", 4, 220, 90)` failed with
  `TypeError: Car() takes no arguments`.
- `super.__init__(brand)` (missing `()` after `super`) references the `super` type itself,
  not a bound proxy to the parent — needs `super().__init__(brand)`.
- `total_vehicles: int` is a type **annotation only** — it declares the type but creates no
  attribute. Needed `total_vehicles = 0` (an actual assignment) before `Vehicle.total_vehicles`
  could be read at all.
- **Name mangling isn't limited to `self.__attr`** — any bare `__name` identifier that
  textually appears inside a class body gets rewritten to `_ClassName__name` by the
  compiler, even a call to an unrelated module-level function. A module-level
  `def __clamped(...)` called from inside `Vehicle` as `__clamped(value)` became a lookup
  for `_Vehicle__clamped`, which never existed → `NameError`. Fixed by using a single
  leading underscore (`_clamped`) for module-private helpers, since single-underscore names
  are just a convention and aren't mangled.
- Bare `except:` around the abstract-instantiation check would swallow *any* exception, not
  just the expected `TypeError` — narrowed to `except TypeError:` so unrelated bugs aren't
  silently hidden.
