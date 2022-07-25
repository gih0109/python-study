# self 의 이해
"""
** self 는 인스턴스 객체이다!
** 클래스 안에 있는 self의 주소와 만들어진 인스턴스의 주소는 같다! 즉, self는 인스턴스 그 자체이다
"""


class SelfTest:

    # 클래스 변수
    name = "amamov"

    def __init__(self, x):
        self.x = x

    # 클래스 메소드
    @classmethod
    def func1(cls):
        print(f"cls: {cls}")
        print("func1")

    # 인스턴스 메소드
    def func2(self):
        print(f"self : {self}")
        print("class 안의 self 주소 : ", id(self))
        print("fucn2")


test_obj = SelfTest(17)
print()
test_obj.func2()
print()
SelfTest.func1()
print()

print("인스턴스의 주소: ", id(test_obj))
print()

"""
self : <__main__.SelfTest object at 0x000001D07B833FA0>
class 안의 self 주소 :  1994937024416
fucn2

cls: <class '__main__.SelfTest'> # cls 는 class 자체를 가르킨다
func1

인스턴스의 주소:  1994937024416 # 클래스 내 self 주소와 인스턴스의 id 가 같다
"""

test_obj.func1()
print()
