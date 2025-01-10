import os
from typing import Any


def log(filename: Any = None) -> Any:
    """Декоратор автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""
    def wrapper(func: Any) -> Any:
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    print(f"{func.__name__} ok")
                else:
                    if len(filename) > 0:
                        path_to_file = os.path.join(os.path.dirname(__file__), "../logs", filename)
                        with open(path_to_file, "w", encoding="utf-8") as file:
                            file.write(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename is None:
                    print(f"{func.__name__} error: {e}. Inputs: ({args}), {kwargs}")
                else:
                    path_to_file = os.path.join(os.path.dirname(__file__), "../logs", filename)
                    with open(path_to_file, "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: ({args}), {kwargs}")
        return inner
    return wrapper
