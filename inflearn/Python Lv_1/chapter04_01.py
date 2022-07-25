# Chapter04-1
# 파이썬 제어문
# IF 실습

# 기본 형식
print(type(True)) # 0 이 아닌 수, 문자 "abc", 데이터 리스트 [1, 2, 3, ...], 튜플 (1, 2, 3, ...), 딕셔너리 등...
print(type(False)) # 0, 빈 문자 "", 빈 리스트 [], 빈 튜플 (), 빈 딕셔너리 {}...

# 예 1

if True: # if 쓰고 엔터 치면 들여쓰기가 된다
    print('Good') # 들여쓰기 중요. 들여쓰기를 하지 않으면 에러

if False:
    print('Good') # if 는 True 일때 실행되고 false 일때 실행되지 않는다

if 'a':
    print('Good') # if '##' 처럼 따옴표 내 문자열 있으면 실행된다 - True 취급

if '':
    print('Good') # if '' 처럼 따옴표 내 문자열 없으면 실행되지 않는다 - false 취급

print()

# 예제 2
if False:
    print('Bad!')
else:
    print('Good!') # if가 실행이 되지 않는다면 else 가 실행된다

if True:
    print('Bad!')
else:
    print('Good!')

print()

# 관계연산자
# >, >=, <, <=, ==, !=
x = 15
y = 10

# 양 변이 같은 경우 참
print(x == y)

# 양 변이 다를 경우 참
print(x != y) # != 는 같지 않다

# 왼쪽이 클 때 참
print(x > y)

# 왼쪽이 크거나 같을 때 참
print(x >= y)

# 오른쪽이 클 때 참
print(x < y)

# 오른쪽이 크거나 같을 때 참
print(x <= y)

city = "" # city 가 빈 값이다
if city:
    print("You are in:", city)
else:
    print("Please enter your city")

city = "Seoul"
if city:
    print("You are in:", city)
else:
    print("Please enter your city")

print()

# 논리 연산자 (중요)
# and, or, not

a = 75
b = 40
c = 50

print('and: ', a > b and b > c) # a > b > c ?
print('or: ', a > b or b > c) # 앞에서 True 라서 뒤에는 연산 안함
print('not: ', not a > b)
print('not: ', not b > c)
print(not True) # 연산이 반대로 된다 True -> False
print(not False)
print()

# 산술, 관계, 논리 우선순위
# 우선순위 : 산술 > 관계 > 논리
print('e1 : ', 3 + 12 > 7 + 3)
print('e2 : ', 5 + 10 * 3 > 7 + 3 * 20)
print('e3 : ', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 : ', 5 + 10 > 0 and not 7 + 3 == 10) # not true -> false 여서 True and False 가 되서 false

print()

score1 = 90
score2 = 'A'

# 예 4
# 복수의 조건이 모두 참일 경우에 실행
if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')

score1 = 70
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')

print()

# 예 5
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')

print()

# 에 6
# 다중 조건문

num = 80

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')

print()

# 예 7
# 충첩 조건문

grade = 'A'
total = 85

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')

print()

# in, not in

q = [10, 20, 30] # 리스트
w = {70, 80, 90, 100} # 집합 (set)
e = {"name": "Lee", "city": "Seoul", "grade": "A"} # 딕셔너리
r = (10, 12, 14) #튜플

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print('Seoul' in e)
print('Seoul' in e.values()) # 값을 검색하려면 values 를 호출하면 된다.
