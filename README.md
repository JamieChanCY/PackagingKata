# Script / Library Separation Kata

In this exercise, we practice importing modules from scripts in other directories,
working up to buliding a Python package that can be installed and imported from anywhere.


## Exercises

### 1. Write the Script 

Follow the directions in `compute_norm_stats.py`, leaving the modules in the project root directory alone

*Tip*: To get the script to import the modules, set the working directory to the project root directory.


### 2. Make a Python Package `stats_utils` out of the modules

Put the modules into a directory in the project root called `stats_utils` and add an `__init__.py` module,
importing the relevant functions.

Update the scrpit to use the package intead of the modules.

Before:
```
from plots import scatter_plot
from gen_data import generate_random_normal
```

After:

```
from stats_utils import scatter_plot, generate_random_normal
```

### 3. Make a `setup.py` file that can install the `stats_utils` package.

(will do together)