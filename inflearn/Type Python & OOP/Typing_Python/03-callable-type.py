# https://mypy.readthedocs.io/en/stable/kinds_of_types.html#callable-types-and-lambdas
""" Callable types """
from typing import Callable


def add1(a: int, b: int) -> int:
    return a + b


# 리턴값이 없으면 -> 이 없다
def add2(a: int, b: int):
    print(a + b)


print(add1(1, 3))


# 함수를 인자로 받을 때 타입힌트
# foo(func: Callable[[받는 인자], 리턴되는 타입])
def foo(func: Callable[[int, int], int]) -> int:
    return func(2, 3)


print(foo(add1))
