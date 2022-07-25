"""
# polymorphism
# 여러 형태를 가질 수 있도록 한다. 즉 객체를 부품화 할 수 있도록 한다
# 같은 형태의 코드가 다른 동작을 하도록 하는 것

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


# 같은 형태의 코드가 다른 의미를 같도록 만드는 것 - 다형성(polymorphism)


class Siri(Robot):
    def say_apple(self):
        print("hello my apple")


class SiriKo(Robot):
    def say_apple(self):
        print("안녕하세요")


class Bixby(Robot):
    def say_samsung(self):
        print("안녕하세요.")
