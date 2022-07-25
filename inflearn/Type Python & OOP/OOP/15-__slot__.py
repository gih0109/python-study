"""
# 객체 내에 있는 변수들은 __dict__을 통해 관리가 된다.
# __slots__를 통해 변수를 관리 :
# 파이썬 인터프리터에게 통보 해당 클래스가 가지는 속성을 제한한다
# __dict__ 를 통해 관리되는 객체의 성능을 최적화한다 -> 다수의 객체 생성시 메모리 사용 공간이 대폭 감소

"""


class WithoutSlotClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


wos = WithoutSlotClass("amamov", 12)

print(wos.__dict__)

wos.__dict__["hello"] = "world"

print(wos.__dict__)


# 객체가 가진 속성을 제한하면 성능이 더 좋아지지 않을까?
class WithSlotClass:
    # __dict__ 아닌 __slots__ 로 관리
    __slots__ = ["name", "age"]  # 리스트 형태로 관리

    def __init__(self, name, age):
        self.name = name
        self.age = age


ws = WithSlotClass("amamov", 12)

# print(ws.__dict__) # 에러 발생

print(ws.__slots__)


# 성능 테스트
import timeit

# 메모리 사용량 비교


def repeat(obj):
    def inner():
        obj.name = "amamov"
        obj.age = 222
        del obj.name
        del obj.age

    return inner


use_slot_time = timeit.repeat(repeat(ws), number=99999)
no_slot_time = timeit.repeat(repeat(wos), number=99999)

print("use slot : ", min(use_slot_time))
print("no slot : ", min(no_slot_time))
