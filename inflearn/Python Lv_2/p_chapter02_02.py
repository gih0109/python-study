# Chapter02-02
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트 등
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이커 방대해지고 복잡해짐 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리 


class Car():
    """
    Car class
    Author : Song
    Date:2022.02.03
    사용법: ....
    """

    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0



    # 인스턴스 변수 선언 
    def __init__(self, company, details):
        self._company = company # 인스턴스 변수 
        self._details = details
        Car.car_count += 1 # __init__ 매소드가 호출될때마다 car_count 1씩 증가
    
    # 매직 메소드; 파이썬에서 미리 구현해놓은 메소드 

    def __str__(self): # str 메소드 # 사용자 레벨에서 print 문으로 정보 확인 시 쓰인다
        return f'str : {self._company} - {self._details}'

    def __repr__(self): # 객체의 엄격한 타입, 정보 공식적인 정보를 확인 시 사용
        return f'repr : {self._company} - {self._details}'

    def __del__(self):
        print('del')
        Car.car_count -= 1

    def detail_info(self):
        print(f'Current ID : {id(self)}')
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

# Self 의 의미 
# 클래스를 기반으로 생성된 인스턴스 자기 내부 고유의 값을 저장하기 위한 지시어, 예약어

car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company) # False 
print(car1 is car2) # False

# dir & __dict__ 확인

# dir
print(dir(car1))
print(dir(car2))
# dir
# 해당 객체가 가지는 모든 어트리뷰트를 리스트로 표시

print()
print()

# __dict__ 내부 값을 알 수 있다.
print(car1.__dict__)
print(car2.__dict__) 

# Doctring
print(Car.__doc__) # 처음 설명, 주석 표시 
print()

# 실행 
car1.detail_info()
car2.detail_info()

# 비교 
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__), id(car3.__class__)) # 같은 클래스로 생성되었기 때문에 id 가 같다
print(id(car1.__class__) == id(car2.__class__) == id(car3.__class__))

# 에러 
# Car.detail_info() # 에러가 난다 
Car.detail_info(car1)  # 클래스 이름으로 접근할때는 () 내에 명시적으로 표시해야함

# 클래스 변수 공유 확인 
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__) 
print(dir(car1)) # car_count 가 나온다

# 접근
print(car1.car_count)
print(Car.car_count)

# car2 지우기 
del car2 

# 삭제 확인 
print(Car.car_count)

# 인스턴스 네임스페이스(dir, __dict__)에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능 ( 인스턴스 검색 후 -> 상위(클래스 변수, 부모클래스 변수))

