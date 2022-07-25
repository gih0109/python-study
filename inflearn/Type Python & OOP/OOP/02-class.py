# class로 사칙연선 만들어보기

# 절차적으로 사칙연산 구현
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


# print(add(1, 2))
# print(sub(1, 2))
# print(mul(1, 2))

# 클래스 이용
class Cal:

    # __init__ : 생성자, 클래스로 인슽턴스를 만들었을때(메모리에 올라갔을때) 즉시 실행되는 함수
    def __init__(self, a, b):  # self : 클래스로 인스턴스를 만들었을때 그 인스턴스를 지칭
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


cal1 = Cal(1, 2)
cal2 = Cal(3, 4)

print(cal1.a)
print(cal1.b)
print(cal1.add())
print(cal1.sub())
# print(cal1.mul())
# print(cal1.div())
print()

print(cal2.a)
print(cal2.b)
print(cal2.add())
print()

# 인스턴스 변수를 외부에서 수정 가능
cal1.a = 7

print(cal1.a)
print(cal1.b)
print(cal1.add())
print(cal1.sub())
