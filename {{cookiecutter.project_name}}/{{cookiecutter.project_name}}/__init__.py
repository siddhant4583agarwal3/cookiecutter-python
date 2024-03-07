import logging

# -- Version -----------------------------------------------------------------

__version__ = "0.0.1"

# -- Define logger and the associated formatter and handler ------------------

formatter = logging.Formatter(
    "%(asctime)s [%(filename)s] %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)

logger = logging.getLogger("{{cookiecutter.project_name}}")
logger.setLevel(logging.INFO)
logger.addHandler(handler)
