"""functools.wrapsを使って関数デコレータを定義する
"""

def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r})'
            f'-> {result!r}')
        return result
    return wrapper

@trace # デコレータがラップする関数を引数として呼び出す → 戻り値を同じスコープの元々の各前に代入する
# => fibonacci = trace(fibonacci)
def fibonacci(n):
    """Return the n-th Fibonacci number
    """
    if n in (0, 1):
        return n
    return (fibonacci(n-2) + fibonacci(n - 1))

fibonacci(4)

# functoolsを使用する

from functools import wraps
def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r})'
            f'-> {result!r}')
        return result
    return wrapper

@trace
def fibonacci(n):
    """Return the n-th Fibonacci number
    """
    if n in (0, 1):
        return n
    return (fibonacci(n-2) + fibonacci(n - 1))

help(fibonacci)