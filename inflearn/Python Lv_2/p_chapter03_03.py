# Chapter03-03
# Special Method (Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Funtions), Class(함수)
# 클래스 안에 정의할 수 있는 특별한(Built in) 메소드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체는 id, type 확인 가능 -> value 이다

# 일반적인 튜플 
# 두 점 사이 거리 구하기 
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt # sqrt 루트를 씌워주는 함수

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)


# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y') # 선언 방법 중 하나

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3)
print(pt3[0], pt3.x)
print(pt4)

# l_leng2 = sqrt((pt3[0] - pt4[0]) ** 2 + (pt3[1] - pt4[1]) ** 2) # 인덱스로 접근; 좋지 않은 방법
l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2) # 키로 접근 ; 명시적으로 알 수 있음
print(l_leng2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) # x 키 중복, class 는 예약어, rename 의 defalt = false, rename = True 해야함


# 출력
print(Point1, Point2, Point3, Point4) 

# Dic to unpacking
temp_dict = {'x': 75, 'y': 55} # 임의의 딕셔너리 객체 생성


# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict) # 딕셔너리로 되 있던 것이 알아서 네임드 튜플 형식으로 변환(언패킹) 된다

print()

print(p1)
print(p2)
print(p3)
# rename 테스트
print(p4) #  Point(x=10, y=20, _2=30, _3=40) 로 _2, _3 으로 난수 생성해서 표시
# dict unpacking
print(p5)

# 사용
print(p1[0] + p2[1])
print(p1.x + p2.y)

x, y = p3 # 네임드 튜플 언팩킹
print(x, y)

# 네임드튜플 메소드
temp = [52, 38]

# _make : 새로운 객체 생성
p4 = Point1._make(temp) # 리스트를 네임드 튜플로 만듬

print(p4)

# _field : 필드 네임 확인
print(p1._fields, p2._fields, p3._fields) # 네임드 튜플에서 키 값 조회

# _asdict() : OrderedDict 반환 (정렬된 딕셔너리)
print(p1._asdict())
print(p4._asdict())

# 실 사용 실습
# 한반 당 20명, 4개의 반(A, B, C, D) ex)B14, C19 로 할당 가능

Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

print(numbers)
print(ranks)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(len(students))
print(students) 

# 추천
students2 = [Classes(rank, number) 
            for rank in 'A B C D'.split() 
            for number in [str(n) 
                for n in range(1, 21)]]

print(len(students2))
print(students2) 

# 출력
for s in students2:
    print(s)