from datetime import datetime as dt
from functools import wraps
from logging import Logger, getLogger
from typing import Any, Callable

_logger: Logger = getLogger(__name__)


def timeit[**P, R](func: Callable[P, R], /) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start, func_name = dt.now(), func.__name__  # ty:ignore[unresolved-attribute]
        _logger.debug(f"{func_name} started")
        result = func(*args, **kwargs)
        _logger.debug(f"{func_name} took: {str(dt.now() - start)}")
        return result

    return wrapper
