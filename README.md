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

4. Change python version in `Dockerfile`, `.pre-commit-config.yml` and CI/CD workflows if necessary.

then you are ready to go.

For existing projects
---------------------
For existing projects that were not generated through *cruft* nor *cookiecutter*, one could make it
compatible with *cruft* with following steps,

1. Run the following cmd from the parent directory of current project, e.g. run from `~/projects/`
   if the repo is placed under path `~/projects/{repo_name}`.
    ```
    cookiecutter https://github.com/tanlin2013/cookiecutter-python -f -v
    ```
   **Warning**: This will overwrite existing files (`-f`), please commit all changes beforehand.
   Then you have to sort out all conflicts manually.

2. Now we can link the repo with *cruft*,
    ```
    cruft link https://github.com/tanlin2013/cookiecutter-python
    ```

3. Commit new changes in `.pre-commit-config.yaml`, and it will automatically update/install hooks.
