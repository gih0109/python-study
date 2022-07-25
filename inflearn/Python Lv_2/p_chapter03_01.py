# Chapter03-01
# Special Method (Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Funtions), Class(함수)
# 클래스 안에 정의할 수 있는 특별한(Built in) 메소드

# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(float))
print(dir(float))

n = 10

print(type(n))

print(n + 100)

print(n.__add__(100))
# print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

print()
print()


# 클래스 예제 1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return f'Fruit Class Info : {self._name} , {self._price}'

    def __add__(self, x):
        print('Called __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('Called __sub__')
        return self._price - x._price

    def __le__(self, x): # 대소비교(오른쪽이 더 크다)
        print('Called __le__')
        if self._price <= x._price:
            return True
        else:
            return False
    
    def __ge__(self, x): # 대소비교(왼쪽이 더 크다)
        print('Called __ge__')
        if self._price >= x._price:
            return True
        else:
            return False



# 인스턴스 생섣ㅇ
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# 매직 매소드 없이 계산
print(s1._price + s2._price)

# 매직 매소드로 계산
print(s1 + s2) # + 가 내부적으로 __add__메소드 호출된다

# 매직메소드
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)