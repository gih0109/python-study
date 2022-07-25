"""
* [property]
* 인스턴스 변수 값을 사용해서 적절한 값으로 보내고 싶을 떄
* 인스턴스 변수 값에 대한 유효성 검사 및 수정
"""

# 모든 속성을 private 로 변경
# 모든 속성이 private 일 때 속성에 접근하는 방법 : property


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
        return a + b

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


droid = Robot("yes", 8)

print(droid.age)  # private 상태인 __age 를 읽을 수 있다

droid.age = 7
# setter 가 없을때 AttributeError: can't set attribute

droid.age += 1
# droid.age = -99 # setter 에서 유효성 검사 하여 TypeError 를 일으키가 만든다

print("droid age : ", droid.age)

print(droid.name)
