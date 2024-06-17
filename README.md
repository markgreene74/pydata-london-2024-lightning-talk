# pydata-london-2024-lightning-talk
Lightning talk @ [PyData London 2024](https://pydata.org/london2024/home) - [Version Control + Notebooks (The tale of a group project)](https://london2024.pydata.org/cfp/talk/MXMELB/)

This repo contains the slides and some [Jupytext](https://github.com/mwouts/jupytext) examples.

- [Setup](#setup)
- [Example 1 - Jupyter notebook -> Python file](#example-1---jupyter-notebook---python-file)
- [Example 2 - Python file -> Jupyter notebook](#example-2---python-file---jupyter-notebook)

## Setup

- install the requirements (`jupyterlab`, `seaborn`, `jupytext`, `pre-commit`)
    ```shell
    pip install -r requirements.txt
    ```
- install the `pre-commit` hooks
    ```shell
    pre-commit install
    ```
- start Jupyter
    ```shell
    jupyter-lab
    ```

## Example 1 - Jupyter notebook -> Python file

In this example the notebook `example-1.ipynb` was created in Jupyter. The Python file (`example-1.py`) was not created manually, but instead was created by Jupytext the first time the notebook was saved.

In Jupyter open the notebook `example-1`, make changes to the notebook and see the same changes reflected into the `.py` file as soon as the notebook is saved.

Example 1 also shows how the `pre-commit` hooks will be applied to the `.py` file.

## Example 2 - Python file -> Jupyter notebook

In this example the notebook was not created in Jupyter. The example shows how it is possible to re-create a notebook (locally) from a Jupytext `.py` files (for example, if working on the same notebook and only the Python file is commited to the git repo).

In Jupyter right-click on the `example-2.py` file, select `Open With` and then `Notebook`. The `.ipynb` file will be created, after which it will be possible to close the `.py` file and start working directly on the notebook.

Example 2 also shows how changes to the notebook file wil be displayed as diff when you look at the commit history for `example-2.py`. See for example the diff between `44333b27` and `3edca83c` [here](https://github.com/markgreene74/pydata-london-2024-lightning-talk/commit/3edca83c0bd8784ffc488813ee873c542029fc3a).
