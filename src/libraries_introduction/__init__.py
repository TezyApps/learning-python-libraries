# from .datastructures import list_example as ls_example
from . import data_structures as ds
from . import lib_intro as li
from .pandas_deep_dive import lesson as pddl # or simply
# from . import lesson as pddl # with __init__.py in pandas_deep_dive/ folder

def main() -> None:
    li.intro_to_libraries(show = False)
    ds.all_examples(show = False)
    pddl.test()