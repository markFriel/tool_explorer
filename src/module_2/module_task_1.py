from src.utils.decorators import log_decorator  # Note: decorators is plural
from src.utils.logger import get_logger

logger = get_logger(__name__)  # Will be 'src.module_1.module_task_1'


@log_decorator(logger=logger)
def example_function_mod_2(arg1: str, arg2: str) -> str:
    """
    An example function

    args:
        arg1: example parameter
        arg2: example parameter

    return:
        returns a string variable
    """

    hello_world = "This is an example function from module two"
    print(hello_world)
    return hello_world
