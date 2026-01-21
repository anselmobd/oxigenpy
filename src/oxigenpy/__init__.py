"""
oxigenpy - utilitários Python da Oxigenai
"""

from importlib.metadata import version as _version

__version__ = _version("oxigenpy")

from . import strings

__all__ = ["strings", "__version__"]
