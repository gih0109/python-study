# Chapter02-01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트 등
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이커 방대해지고 복잡해짐 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리 

# 일반적인 코딩

# 차량1
car_company = 'Ferrari'
car_detail_1 = [
    {'color': 'White'},
    {'horsepower': 400},
    {'price': 8000},
]

# 차량2
car_company = 'BMW'
car_detail_1 = [
    {'color': 'Black'},
    {'horsepower': 270},
    {'price': 5000},
]

# 차량3
car_company = 'Audi'
car_detail_1 = [
    {'color': 'Silver'},
    {'horsepower': 300},
    {'price': 6000},
]
# 수정이나 변동이 있을 시 불편하다

# 리스트 구조 
# 관리가 불편, 인덱스 접근 시 실수 가능, 삭제 불편 
car_company_list = ['Ferrari', 'BMW', 'Audi']
car_detail_list = [
    {'color': 'White', 'horsepower': 400, 'price': 8000},
    {'color': 'Black', 'horsepower': 270, 'price': 5000},
    {'color': 'Silver', 'horsepower': 300, 'price': 6000},
]

# 삭제할려면 인덱스 번호를 통해 접근해야한다.
del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)


# 딕셔너리 구조 
# 코드 반복 지속, 중첩 문제 발생(키), 정렬 문제, 키 조회 예외 처리 등 

car_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color': 'White', 'horsepower': 400, 'price': 8000}}, # 딕셔너리 안에 딕셔너리 있는 형태; 네스티드 딕셔너리 
    {'car_company': 'BMW', 'car_detail': {'color': 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {'color': 'Silver', 'horsepower': 300, 'price': 6000},}
]

# print(car_dicts)

# 삭제 시
# pop(key, default)??? 딕셔너리
del car_dicts[1]
print(car_dicts)

print()
print()


# 클래스 구조 
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용 

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details
    
    # 매직 메소드; 파이썬에서 미리 구현해놓은 메소드 

    def __str__(self): # str 메소드 # 사용자 레벨에서 print 문으로 정보 확인 시 쓰인다
        return f'str : {self._company} - {self._details}'

    def __repr__(self): # 객체의 엄격한 타입, 정보 공식적인 정보를 확인 시 사용
        return f'repr : {self._company} - {self._details}'

car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

# __str__, __repr__ 이 없으면 객체 정보를 표시
print(car1) # __str__ 이 있으면 __str__이 쓰이고 아니면 __repr__이 쓰인다
print(car2)
print(car3)

print(car1.__dict__) # __dict__ 하면 내부 어트리뷰트 속성을 모두 알 수 있다
print(car2.__dict__) 
print(car3.__dict__)

# print(dir(car1)) 

print()
print() 

car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

print()
print()

# 반복문(__str__)
for x in car_list:
    print(x)
    # print(repr(x))