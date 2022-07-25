# __ABC__ : 매직 메소드
# 각 매직 메소드마다 고유의 역할이 있다.


class Robot:
    """
    [robot class]
    Author : Song
    Role : ... ...
    """

    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0

    # 생성자 함수
    def __init__(self, name, code):
        self.name = name  # 인스턴스 변수
        self.code = code  # 인스턴스 변수
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


droid1 = Robot("R2-D2", 123123)
droid1.say_hi()

# print(dir(droid1))
print(droid1)  # <__main__.Robot object at 0x000001B21F928A30>
print()
print(droid1.__str__)  # <method-wrapper '__str__' of ....>
print()
print(droid1.__str__())  # <__main__.Robot object at 0x000001B21F928A30>
print()

# 파이썬은 모두 객체로 다룬다
# -> 함수도 객체이다

# 함수 뒤 () : 실행할 수 있다 (callable 객체)

droid1()
