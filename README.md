# cookiecutter-python

A simple template for my own personal Python3.6+ projects utilizing black + isort +
flake8 + poetry + mypy + bandit + bugbear + more goodness. Best used
with [cruft](https://cruft.github.io/cruft/)

* To use:

```
cruft create https://github.com/timothycrosley/cookiecutter-python/
```

* Linking an existing project

```
cruft link https://github.com/timothycrosley/cookiecutter-python/
```

* Update a project

```
cruft update
```

optionally, one can manage update rules on `tool.cruft` section of
your `pyproject.toml` file.

* Compute the difference

```
cruft diff
```
