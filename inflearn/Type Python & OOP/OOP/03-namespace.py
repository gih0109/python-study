"""
#* namespace : 개체를 구분할 수 있는 범위.
#* __dict__ : 네임스페이스를 확인 할 수 있다.
#* dir() : 네임스페이스의 key 값을 확인 할 수 있다
#* __doc__ : 클래스의 주석을 확인한다.
#* __class__ : 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다.
"""


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


siri = Robot("siri", 21039788127)

javis = Robot("javis", 394092891)

bixby = Robot("bixby", 12344566)

print(Robot.__dict__)
print(siri.__dict__)
print(javis.__dict__)

print(siri.name)
print(bixby.name)

siri.cal_add(2, 3)

print(siri.population)

siri.how_many()

Robot.say_hi(siri)
siri.say_hi()

# print(dir(siri))
# print(dir(Robot))

print(Robot.__doc__)

print(siri.__class__)
