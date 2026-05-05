"""testable_demo package — DEV branch.

This package intentionally contains issues for whitebox analyzer validation.
"""

import json  # unused — pylint W0611 should flag this

from .calculator import add, subtract  # re-exports
from .strings import slugify_loose_dup  # re-export

__all__ = ["add", "subtract", "slugify_loose_dup"]
__version__ = "0.1.0-dev"
