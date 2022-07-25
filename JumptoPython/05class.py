class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print()

# 사칙연산 하는 FourCal 클래스 만들기

class FourCal1:
    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        value = self.num1 + self.num2
        return value

    def mul(self):
        value = self.num1 * self.num2
        return value

    def sub(self):
        value = self.num1 - self.num2
        return value

    def div(self):
        value = self.num1 / self.num2
        return value

a = FourCal1()
a.setdata(4, 2)
print(a.num1)
print(a.num2)
print('.......')

a = FourCal1()
b = FourCal1()

a.setdata(4, 2)
print(a.num1)
b.setdata(3, 7)
print(b.num1)

print('>>>> 더하기 테스트')
print(a.add())
print(b.add())
print('테스트')
print(b.mul())
print(a.sub())
print(b.div())
print()



class FourCal2:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        value = self.num1 + self.num2
        return value

    def mul(self):
        value = self.num1 * self.num2
        return value

    def sub(self):
        value = self.num1 - self.num2
        return value

    def div(self):
        value = self.num1 / self.num2
        return value

a2 = FourCal2(5, 6)
print('>>>>>FourCal2 매개변수 확인')
print(a2.num1)
print(a2.num2)
print('>>>>>FourCal2 테스트')
print(a2.add())
print(a2.mul())
print(a2.sub())
print(a2.div())

# 클래스 상속
class MoreFourCal(FourCal2):
    def pow(self):
        return self.num1 ** self.num2

print('>>>> 클래스 상속 확인')
a3 = MoreFourCal(5, 3)
print(a3.add())
print(a3.sub())
print(a3.pow())

# 메소드 오버라이딩
class SafeFourcal(FourCal2):
    def div(self):
        if self.num2 == 0:
            return 0
        else:
            return self.num1 / self.num2

print('>>>> 메소드 오버라이딩 테스트')
a4 = SafeFourcal(4, 0)
print(a4.div())
print()

# 클래스 변수
class Family:
    lastname = '김'

print(Family.lastname)
