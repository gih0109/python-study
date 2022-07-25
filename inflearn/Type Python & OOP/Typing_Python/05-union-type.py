# union type
from typing import Union

# 한 변수에 여러 타입을 할당해야할 때
# 예
# 처음
xxx: int = 3
# 이후
xxx = "17"

# 유니언 타입을 써야 한다
xxx: Union[int, str] = 3  # 대괄호 내 올 수 있는 타입을 모두 적어야 함

xxx = "17"


# 함수에서도 사용 가능
def foo(x: Union[int, str]) -> None:
    print(x)


foo(xxx)
