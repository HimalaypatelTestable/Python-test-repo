"""Testable demo package: secure, well-tested utility modules.

This package showcases secure-by-default Python patterns and is designed
to score well on the Testable whitebox metric suite.
"""

from testable_demo.calculator import (
    add,
    clamp,
    divide,
    factorial,
    mean,
    median,
    multiply,
    subtract,
)
from testable_demo.data_flow import (
    group_by_category,
    running_total,
    summarize_orders,
)
from testable_demo.http_client import fetch_json
from testable_demo.security import (
    generate_token,
    hash_password,
    parse_literal_config,
    run_command,
    safe_load_yaml,
    select_user_by_id,
    write_temp_file,
)
from testable_demo.strings import (
    count_words,
    is_palindrome,
    normalize_whitespace,
    reverse_words,
    slugify,
    truncate,
)

__version__ = "1.0.0"

__all__ = [
    "__version__",
    "add",
    "clamp",
    "count_words",
    "divide",
    "factorial",
    "fetch_json",
    "generate_token",
    "group_by_category",
    "hash_password",
    "is_palindrome",
    "mean",
    "median",
    "multiply",
    "normalize_whitespace",
    "parse_literal_config",
    "reverse_words",
    "running_total",
    "run_command",
    "safe_load_yaml",
    "select_user_by_id",
    "slugify",
    "subtract",
    "summarize_orders",
    "truncate",
    "write_temp_file",
]
