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
# This example is taken from the Seaborn documentation (https://seaborn.pydata.org/examples/regression_marginals.html)

# %%
import seaborn as sns

sns.set_theme(style="darkgrid")

tips = sns.load_dataset("tips")
g = sns.jointplot(
    x="total_bill",
    y="tip",
    data=tips,
    kind="reg",
    truncate=False,
    xlim=(0, 60),
    ylim=(0, 12),
    color="m",
    height=7,
)
