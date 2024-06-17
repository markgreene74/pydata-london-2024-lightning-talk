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
# # Example 2 - Jupyter notebook -> Python file

# %% [markdown]
# This example is taken from the Seaborn documentation (https://seaborn.pydata.org/examples/scatter_bubbles.html)

# %%
import seaborn as sns

sns.set_theme(style="white")

mpg = sns.load_dataset("mpg")
sns.relplot(
    x="horsepower",
    y="mpg",
    hue="origin",
    size="weight",
    sizes=(40, 400),
    alpha=0.5,
    palette="muted",
    height=6,
    data=mpg,
)
