"""
#* 추상화 : abstraction
#* 불필요한 정보는 숨기고 중요한(필요한) 정보만 표현
#* 공통의 속성값이나 행위(methods)를 하나로 묶어 이름을 붙이는 것
"""

# 시리 로봇 만들어보기
siri_name = "siri"
siri_code = 21039788127


def siri_say_hi():
    # code...
    print("say hello!! my name is siri")


def siri_add_cal():
    return 2 + 3


def siri_die():
    # code....
    print("siri die")


# 자비스 로봇 만들어보기
javis_name = "javis"
javis_code = 101002093

# .....


# 클래스로 구현
class Robot:

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


print(Robot.population)

siri = Robot("siri", 21039788127)

print(Robot.population)

javis = Robot("javis", 394092891)

print(Robot.population)

bixby = Robot("bixby", 12344566)

print(Robot.population)

bixby2 = Robot("bixby2", 12344566)

print(siri.name)
print(siri.code)

siri.say_hi()
siri.cal_add(2, 3)

javis.die()

Robot.how_many()
