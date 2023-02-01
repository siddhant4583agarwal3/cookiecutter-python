import logging
from importlib import metadata


# -- Version -----------------------------------------------------------------

__version__ = metadata.version(__name__)

# -- Define logger and the associated formatter and handler ------------------

{{cookiecutter.description}}
"""
__version__ = "{{cookiecutter.version}}"
