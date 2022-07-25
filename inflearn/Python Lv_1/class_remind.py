# OOP: 객체지향 프로그래밍
# 왜 쓰는가? 장점이 무엇인가?
# 생산성이 향상된다. 절차지향에 비해 장점 있음 
# 재사용 극대화 
# 상속 개념 
# chapter06-1

# OOP, Self, 인스턴스 메소드, 인스턴스 변수 

# 클래스 and 인스턴스 차이 이해 
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유한다
# 인스턴스 변수 : 객체마다 별도 존재 (self 가 붙은 것들)

# 예제 1

class Dog: # 모든 클래스는 상속받음
    # 클래스 속성
    species = 'firstdog'

    # 모든 클래스는 초기화/인스턴스 속성을 가진다
    # 클래스 초기화 함수
    def __init__(self, name, age): # name, age : 클래스를 가지고 지정할 변수들 
        self.name = name # self.name 등 임의로 지정 가능, name 과 age 만 정확히 맵핑하면 된다
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화 
a = Dog('mikky', 2) # 클래스에 변수를 집어넣어 구현된 객체를 인스턴스라 한다
b = Dog('baby', 3)
c = Dog('mikky', 2)

# 비교
print(a == b, id(a), id(b))
print(a == c, id(a), id(c)) # 인스턴스화 된 객체들은 모두 다르다

# 네임스페이스 
print('dog1', a.__dict__) # 객체가 가지고 있는 속성을 알 수 있다
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print(f'{a.name} is {a.age} and {b.name} is {b.age}')

# 클래스 변수에 접근 가능한가?
if a.species == 'firstdog':
    print(f'{a.name} is a {a.species}')

# 클래스 변수에 직접 접근 가능한가?
print(Dog.species) # 접근 가능
# 클래스 변수에 인스턴스화 된 변수로 직접 접근이 가능한가?
print(a.species) # 가능

# 예제 2
# self 이해 

class SelfTest:
    # __init__ 메소드가 없음
    # 이 코드가 내부적으로 클래스를 만들 때 파이썬이 알아서 실행해줌

    def func1(): # self 가 없으면 클래스 메소드
        print('Func1 called')
    def func2(self): # self 가 있으면 인스턴스 메소드
        # self 에 f 가 온다
        print(self)
        print(id(self)) # self의 id  값이 f 와 동일하다 
        print('Func2 called')

f = SelfTest()

print(dir(f)) # 사용할 수 있는 메소드 확인가능 맨 끝에 func1, func2 있는걸 확인가능 
print(id(f))

# 클래스를 인스턴스 화 시킨 이후 내부 메소드 호출

# f.func1() # 예외: func1 은 매게변수가 없는데 하나가 넘어와서 오류
f.func2() # 

SelfTest.func1() # 클래스로 직접 접근해서 func1 호출 가능
SelfTest.func2(f) # 


# 예제 3
# 클래스 변수, 인스턴스 변수

class Warehouse:
    # 클래스 변수 
    stock_num = 0

    def __init__(self, name):
        #인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self): # 객체가 소멸 시 호출되는 함수
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

# Warehouse.stock_num = 50 # 클래스 변수를 직접 수정 가능

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print(user1.stock_num) # 2 출력된다. 클래스 메소드는 공유된다. 

del user1 
print('after', Warehouse.__dict__)


# 예제 4

class Dog2: 

    species = 'firstdog'

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    # 메소드???
    def info(self):
        return f'{self.name} is {self.age} years old'
    
    def speak(self, sound):
        return f'{self.name} says {sound}!'

# 인스턴스 생성
c = Dog2('july', 4)
d = Dog2('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))