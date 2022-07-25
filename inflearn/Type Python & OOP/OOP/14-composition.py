"""
# composition
# 다른 클래스의 일부 메소드를 사용하고 싶지만, 상속은 하고 싶지 않을 경우
# 1. 부모 클래스가 변하면 자식 클래스는 계속 수정되어야 한다
# 2. 부모 클래스의 메소드를 오버라이딩 하는 경우 내부 구현 방식의 얕은 이해로 오류가 생길 가능성이 증가한다.

"""


class Robot:  # Robot(object) 를 생략한 것
    """
    [robot class]
    Author : Song
    Role : ... ...
    """

    # 클래스 변수 : 인스턴스들이 공유하는 변수
    __population = 0

    # 생성자 함수
    def __init__(self, name, age):
        self.__name = name
        # self.age = age  # public
        self.__age = age  # private 화 : 앞에 __ 를 붙인다
        Robot.__population += 1

    @property  # private 에 접근해 읽을 수 있게 한다
    def age(self):
        return self.__age

    @property
    def name(self):
        return f"yoon {self.__name}"

    @age.setter  # private 값을 우회해서 수정 가능하게 만든다
    def age(self, new_age):
        # setter 에서 값 판별 가능하게 할 수 있다(유효성 검사)
        if new_age < 0:
            # if new_age - self.__age == 1:
            raise TypeError("invaild range to age")
        else:
            print(new_age)
            self.__age = new_age

    # 인스턴스 메서드
    def say_hi(self):
        # code...
        print(f"Greetings, my master call me {self.__name}.")

    def cal_add(self, a, b):
        return a + b + 1

    def die(self):
        print(f"{self.__name} is being destroyed")
        Robot.__population -= 1
        if Robot.__population == 0:
            print(f"{self.__name} was the last one.")
        else:
            print(f"There are still {Robot.__population} robots working.")

    @classmethod
    def how_many(cls):
        print(f"we have {cls.__population} robots.")

    @staticmethod
    def this_is_robot_class():
        print("yes")

    def __str__(self):
        return f"{self.__name} robot!!"  # 메소드 오버라이팅

    # droid1 이 호출 가능하도록 해보기
    def __call__(self):
        print("call")
        return f"{self.__name} call!!"


class BixbyCal:

    # 컴포지션 하기 위해서 __init__ 에서 아래를 해야한다.
    def __init__(self, name, age):
        self.Robot = Robot(name, age)

    def cal_add(self, a, b):
        return self.Robot.cal_add(a, b)  # 상속 없이 Robot의 메소드를 가져올 수 있다.
