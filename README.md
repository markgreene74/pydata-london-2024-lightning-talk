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

In this example the notebook `example-1.ipynb` was created in Jupyter. The Python file (`example-1.py`) was not created manually, but instead was created by Jupytext the first time I saved the notebook.

Try to make changes to the notebook and see the same changes reflected into the `.py` file as soon as the notebook is saved.

## Example 2 - Python file -> Jupyter notebook
