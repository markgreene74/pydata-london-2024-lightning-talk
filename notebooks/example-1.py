# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Example 1 - Jupyter notebook -> Python file

# %% [markdown]
# This example is taken from the Seaborn documentation (https://seaborn.pydata.org/examples/multiple_regression.html)

# %%
import seaborn as sns
sns.set_theme()

# Load the penguins dataset
penguins = sns.load_dataset("penguins")

# Plot sepal width as a function of sepal_length across days
g = sns.lmplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="species",
    height=5
)

# Use more informative axis labels than are provided by default
g.set_axis_labels("Snoot length (mm)", "Snoot depth (mm)")

# %% [markdown]
# Make some changes to the notebook and check the output of `pre-commit`, for example try un-commenting all the lines in the cell below and then run it.
#
# The first line should trigger `flake8`, while the following lines should trigger `black`.

# %%
# import re
# print(
#     (
#     "Hello"
#     "World"
# )                 )

# %% [markdown]
# And then run the next cell to execute `pre-commit`.

# %%
# !pre-commit run --files example-1.py

# %% [markdown]
# The output of `pre-commit` will show that `black` and `flake8` failed:
#
# ```
# black....................................................................Failed
# - hook id: black
# - exit code: 1
#
# would reformat notebooks/example-1.py
#
# Oh no! 💥 💔 💥
# 1 file would be reformatted.
#
# flake8...................................................................Failed
# - hook id: flake8
# - exit code: 1
#
# notebooks/example-1.py:44:1: F401 're' imported but unused
# notebooks/example-1.py:47:5: E122 continuation line missing indentation or outdented
# notebooks/example-1.py:48:5: E122 continuation line missing indentation or outdented
# notebooks/example-1.py:49:1: E122 continuation line missing indentation or outdented
# notebooks/example-1.py:49:18: E202 whitespace before ')'
# ```
