import functools
import logging
import pdb
import sys
import time
from threading import Lock


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        print(f"[TIMER] Function '{func.__name__}' executed in {elapsed:.4f} seconds.")
        return result

    return wrapper


def rate_limit(max_per_second):
    """
    Decorator that limits the rate at which a function can be called.

    :param max_per_second: Maximum number of allowed calls per second.
    """
    min_interval = 1.0 / float(max_per_second)
    lock = Lock()

    def decorator(func):
        last_called = [0.0]  # Using a mutable object to hold state.

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with lock:
                elapsed = time.time() - last_called[0]
                wait_time = min_interval - elapsed
                if wait_time > 0:
                    time.sleep(wait_time)
                result = func(*args, **kwargs)
                last_called[0] = time.time()
            return result

        return wrapper

    return decorator


def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    time.sleep(delay)
            raise Exception(
                f"Function {func.__name__} failed after {max_attempts} attempts"
            )

        return wrapper

    return decorator


def log_decorator(level=logging.DEBUG, logger=None):
    """
    A decorator for logging function calls.

    :param level: The logging level to use (default: logging.DEBUG)
    :param logger: Optional logger instance. If not provided, uses the logger for the current module.
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Only build the log message if this level is enabled
            if logger.isEnabledFor(level):
                logger.log(
                    level, f"Entering {func.__name__} with args={args}, kwargs={kwargs}"
                )
            try:
                result = func(*args, **kwargs)
                if logger.isEnabledFor(level):
                    logger.log(level, f"Exiting {func.__name__} with result={result}")
                return result
            except Exception as e:
                logger.exception(f"Exception in {func.__name__}: {e}")
                raise

        return wrapper

    return decorator


def singleton(cls):
    """A decorator that makes a class a Singleton."""
    instances = {}

    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


def debug_on_exception(func):
    """
    Launches pdb post-mortem debugging if the decorated function raises an exception.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            _, _, tb = sys.exc_info()
            print("Exception occurred, launching debugger...")
            pdb.post_mortem(tb)
            raise

    return wrapper
