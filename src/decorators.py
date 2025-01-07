from functools import wraps
from typing import Any


def log(filename: Any = None) -> Any:
    """Декоратор автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""
    def decorator(my_func: Any) -> Any:
        @wraps(my_func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = my_func(*args, **kwargs)
            if not filename:
                print(f'{my_func.__name__} started')
                try:
                    print(f'{my_func.__name__} ok')
                    print(f'{my_func.__name__} finished')
                except Exception as e:
                    print(f'{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}')
            else:
                try:
                    with open(filename, 'w') as file:
                        file.write(f'{my_func.__name__} ok')
                except Exception as e:
                    with open(filename, 'w') as file:
                        file.write(f'{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}')
            return result
        return wrapper
    return decorator
