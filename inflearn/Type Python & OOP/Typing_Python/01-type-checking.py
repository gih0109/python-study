from typing import List, Tuple, Dict

# 타입 힌트
int_var: int = 88
# int_var: str = 88  # 다른 타입을 적어놓아도 에러가 나지 않는다 : 힌트
str_var: str = "hello world"
float_var: float = 88.9
bool_var: bool = True


list_var_1: list = [1, 2, 3]
list_var_2: List[int] = [1, 2, 3]  # 리스트 내부에 어떤 타입의 데이터가 있는지 표시
list_var_3: List[str] = ["1", "2", "3"]

tuple_var: Tuple[int, int, int] = (1, 2, 3)

dic_var: Dict[str, int] = {"hello": 47}  # key : str, value: int 라는 힌트


# 타입힌트를 쓰는 이유
# 예시 : 타입힌트 없음
def cal_add(x, y):
    # code
    return x + y  # 의도 : int 더하기


# # 의도한 활용법
print(cal_add(1, 3))

# 의도와는 다르게 다른 형태의 데이터를 집어넣을 수 있다
print(cal_add("1", "3"))
print(cal_add([1, 3], [2, 4]))


# 타입힌트 쓴 예시
# isinstance(obj, class) : object 가 class에 대한 인스턴스인지 확인
# isinstance 를 통해 typechecking 을 한다
def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error : {typer}")


def cal_add(x: int, y: int) -> int:  # 타입 힌트
    # code
    type_check(x, int)
    type_check(y, int)
    return x + y  # 의도 : int 더하기


print(cal_add(1, 3))
# print(cal_add("1", "3")) # TypeError 일으키게 함
# print(cal_add([1, 3], [2, 4]))
