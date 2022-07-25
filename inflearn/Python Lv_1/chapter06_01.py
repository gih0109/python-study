# Chapter06-1
# 파이썬 클래스
# OOP (객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 클래스 AND 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 모든 인스턴스가 공유하는 속성 
# 인스턴스 변수 : 객체마다 별도 존재
# 메소드가 뭔지 알아보기**

# 예제 1
class Dog(object): # 클래스 생성, (object) 생략 가능, object 상속 ; class Dog():, class Dog: 가능
    # 클래스 속성
    species = 'firstdog' # 클래스 변수

    # 초기화/인스턴스 속성 ; 모든 클래스는 초기화 메소드를 갖는다
    def __init__(self, name, age): # 파이썬에는 클래스가 초기화될때 반드시 __init__(self, ... ) 를 한 번 호출한다
        self.name = name # (self 뒤 클래스를 가지고 사용할 변수와 속성들을 지정 할 수 있다
        self.age = age # self 가 붙은 것은 나만의 인스턴스 변수
# 이것들이 객체이다, class 형태
# 인스턴스는 객체의 한 종류???

# 클래스 정보
print(Dog) # 만든 클래스 표시

print()

# 인스턴스화
a = Dog("mikky", 2) # 변수 = 인스턴스 이름(속성1, 속성2, ...) 형태, self 는 생략 가능
b = Dog("baby", 3)
c = Dog("mikky", 2)

# 인스턴스는 코드로 구현해서 메모리에 올라간 그 시점 ,어떤 변수로 활용할수 있는 대상

# 비교
print(a == b, id(a), id(b), id(c)) # 내부 속성이 같더라도 모두 다른 id 를 가진다

# 네임스페이스
print('dog1', a.__dict__) # 클래스가 가지고 있는 속성과 값을 확인 가능 ; 딕셔너리 형태
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species) # 클래스로 접근 가능
print(a.species) # 인스턴스로 접근 가능
print(b.species)

print()

# 예제 2
# self의 이해
class SelfTest:
    def func1(): #func1 은 클래스 메소드 ; 매개변수 없음 ; 클래스 직접 호출
        print('Func1 called')
    def func2(self): # self 가 붙은 것은 인스턴스 메소드 ; 인스턴스로 넘기거나 인스턴스로 호출
        print(id(self))
        print('Func2 called')
# 클래스를 만들 때 __init__를 생략해도 된다. 파이썬이 자체적으로 만들어준다

f = SelfTest()

# print(dir(f)) # 맨 뒤에 'func1' 과 'func2' 가 있는 것을 확인 가능
print(id(f))
# f.func1() # 에러 발생 ; func1 에는 메개변수가 없는데 무언가 넘어왔다
f.func2()

# self 는 인스턴스를 요구한다. self 에 f 가 넘어간 것이다
# 클래스를 인스턴스 시킨 f 의 id 값과 self 로 넘어온 id 값이 동일
# 클래스 내부 매개변수를 선언하는데 self 가 없다는 것 -> 클래스 메소드 ; f 값이 func1 에서 받지 않아서 예외 발생

# func1 호출 방법
SelfTest.func1() # 클래스로 바로 접근
# func2 를 동일하게 호출한다면?
# SelfTest.func2() # 예외 발생
SelfTest.func2(f) # f 를 넣어주면 func2 가 호출된다

# 예제 3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0 # 재고

    def __init__(self, name):
        #인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1 # 객체가 만들어질 떄 1 증가

    def __del__(self): # __del__ 은 객체가 소멸할 때 자동으로 호출하는 함수
        Warehouse.stock_num -= 1 # 객체가 소멸 할 때 1 감소

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
# Warehouse.stock_num = 50 # 직접 수정 가능하지만 추천X

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)
print('>>>>', user1.stock_num)

del user1
print('after del user1', Warehouse.__dict__)

print()

#에제 4
class Dog(object):
    # 클래스 속성
    species = 'firstdog' # 클래스 변수

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 메소드 : 클래스가 하는 행동??
    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)

# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))


print()
