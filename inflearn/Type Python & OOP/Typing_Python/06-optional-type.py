# Optional-type
# Union type 과 비슷하다
# 있을수도 있고 없을수도 있을때 가능

from typing import Union, Optional


def foo(name: str) -> Optional[str]:
    if name == "amamov":
        return None
    else:
        return name


xxx: Union[str, None] = "amamov"
xxx: Optional[str] = foo("amamov")
print(xxx)

xxx = None
print(foo(xxx))
