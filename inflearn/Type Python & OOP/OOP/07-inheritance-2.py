"""
[클래스 상속]

1. 부모 클래스가 갖는 모든 메소드와 속성이 자식 클래스에 그대로 상속된다

2. 자식 클래스에서 별도의 메소드나 속성을 추가할 수 있다.

3. 메소드 오버라이딩

4. super()

5. Python의 모든 클래스는 object 클래스를 상속한다: 모든것은 객체이다.

6. MyClass.mro() -> 상속 관계를 보여준다.

"""

# 부모클래스


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


# 자식메소드
# Robot 클래스를 상속받는 Siri 클래스 만들기
class Siri(Robot):
    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        return a * b

    @classmethod
    def hello_apple(cls):
        print(f"{cls} hello apple!!")


siri = Siri("iphone9", 456456)

siri.call_me()

print(siri.cal_mul(7, 8))

Siri.hello_apple()
