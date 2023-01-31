# cookiecutter-python

A simple template for my own personal Python3.8+ projects utilizing black + isort +
flake8 + poetry + mypy + bandit + bugbear + more goodness. Best used
with [cruft](https://cruft.github.io/cruft/)

* To use,
    ```
    cruft create https://github.com/tanlin2013/cookiecutter-python/
    ```

* Linking an existing *cookiecutter* project,
    ```
    cruft link https://github.com/tanlin2013/cookiecutter-python/
    ```

* Update a project,
    ```
    cruft update
    ```
  optionally, one can manage update rules at the section `tool.cruft` in
  `pyproject.toml`.


* Compute the difference,
    ```
    cruft diff
    ```

Development guideline
---------------------
Once a project is generated from the cruft template, there are fewer steps to go,

1. Initialize the directory as a Git repository.
    ```
    git init -b main
    git remote add origin <REMOTE_URL>
    ```

2. Install pre-commit hook on localhost (first time only).
    ```
    pre-commit install --hook-type commit-msg --hook-type pre-push
    ```

3. Set up CI secrets in GitHub settings of this repo, `secrets and variables`/`actions`,
   and click `New repository secrets`.

then you are ready to go.

For existing projects
---------------------
For existing projects that were not generated through *cruft* nor *cookiecutter*, one could make it
compatible with *cruft* with following steps,


