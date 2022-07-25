"""
* public vs private
"""


class Robot:  # Robot(object) 를 생략한 것
    """
    [robot class]
    Author : Song
    Role : ... ...
    """

    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0

    # 생성자 함수
    def __init__(self, name, age, code):
        self.name = name
        # self.age = age  # public
        self.__age = age  # private 화 : 앞에 __ 를 붙인다
        self._code = code  # 암묵적인 표시
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        # code...
        print(f"Greetings, my master call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    def die(self):
        print(f"{self.name} is being destroyed")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    @classmethod
    def how_many(cls):
        print(f"we have {cls.population} robots.")

    @staticmethod
    def this_is_robot_class():
        print("yes")

    def __str__(self):
        return f"{self.name} robot!!"  # 메소드 오버라이팅

    # droid1 이 호출 가능하도록 해보기
    def __call__(self):
        print("call")
        return f"{self.name} call!!"


class Siri(Robot):
    def __init__(self, name, age, code):
        super().__init__(name, age, code)
        print(self.name)
        # print(self.__age) # Robot 클래스의 __age 는 속성이 은닉되어서 에러
        # private 는 상속받을 시 사라진다
        self.__age = 999
        print(self.__age)
        self._code = code
        # _*** : 파이썬의 private 는 강력하다. 타 언어의 protected 가 없다
        # 따라서 앞에 _ 를 붙이면 private 로 암묵적으로 간주하기도 한다


ss = Robot("yes", 8, 123123)

# print(ss.age)

# 외부에서 임의로 인스턴스 속성 변경
# ss.age = -10
# print(ss.age)

# private 메소드 : 외부에서 임의로 인스턴스 속성 변경하는것을 막음

ss._code  # 접근가능

ssss = Siri("iphone9", 9, 345345)
