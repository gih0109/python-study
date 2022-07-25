# Chapter02-03
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트 등
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이커 방대해지고 복잡해짐 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리 


class Car():
    """
    Car class
    Author : Song
    Date:2022.02.07
    Description : Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0

    # 인스턴스 변수 선언 
    def __init__(self, company, details):
        self._company = company # 인스턴스 변수 
        self._details = details
    
    # 매직 메소드; 파이썬에서 미리 구현해놓은 메소드 

    def __str__(self): # str 메소드 # 사용자 레벨에서 print 문으로 정보 확인 시 쓰인다
        return f'str : {self._company} - {self._details}'

    def __repr__(self): # 객체의 엄격한 타입, 정보 공식적인 정보를 확인 시 사용
        return f'repr : {self._company} - {self._details}'

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    # Self 의 의미 
    # 클래스를 기반으로 생성된 인스턴스 자기 내부 고유의 값을 저장하기 위한 지시어, 예약어

    def detail_info(self):
        print(f'Current ID : {id(self)}')
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method
    @classmethod # 클래스 메소드라는걸 잘 표시하기 위해 붙인다
    def raise_price(cls, per): # 첫 번째 인자로 cls를 받는다
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print('Sucessed! price increased.')

    # Static Method
    # 메소드를 유연하게 호출할 수 있다
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return f'OK! This car is {inst._company}'
        return 'Sorry. This car is not BMW.'



car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})

# 전체 정보
car1.detail_info()
car2.detail_info()

# 가격 정보 (직접 접근)
# 직접 인스턴스 변수에 접근하는 것은 좋지 않은 방법
print(car1._details.get('price'))
print(car2._details['price'])
# 보통 메소드를 만들어서 접근한다

# 가격 정보 (인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 정보 (클래스 메소드 미사용)
# 직접 접근해서 수정하는 것은 좋지 않은 방법
Car.price_per_raise = 1.4

# 가격 정보 (인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 가격 인상 (클래스 메소드 사용)
Car.raise_price(1.6)

# 가격 정보 (인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# static method
# 인스턴스로 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# 클래스로 호출
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))