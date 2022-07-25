# Chapter04-2
# 파이썬 반복문
# For 실습

# 코딩의 핵심
# for in <collection> ; collection <- 집합의 형태
#   <Loop body>

for v1 in range(10):
    print('v1 is : ', v1) # v1 : for 문 내부에서 사용할 변수 선언
#range 함수. range(N) 은 0 부터 N-1 까지 출력
print()

for v2 in range(1, 11): # 1 ~ 10
    print('v2 is : ', v2)
print()

for v3 in range(1, 11, 2): # 2개씩 스킵하면서 1 ~ 10 까지 : 1, 3, 5, ...
    print('v3 is : ', v3)
print()

# 1 ~ 1000 합 구하기
sum1 = 0

for v in range(1, 1001):
    sum1 += v
# sum1 += v 는 sum1 = sum1 + v 축약어

print('1 ~ 1000 Sum : ', sum1)

print('1 ~ 1000 Sum : ', sum(range(1, 1001)))

print(range(1, 11)) # range 자체가 자료형이 - 연속적인 데이터를 담고 있음

print(type(range(1, 11)))

# 1 ~ 1000 사이 4의 배수의 합
print('1 ~ 1000 4의 배수의 합 : ', sum(range(4,1001,4)))

print()

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제 1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for name in names:
    print('You are : ', name) # 내부 원소를 모두 출력

print()

# 예제 2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Current number : ", n)

word = "Beautiful"

for s in word:
    print('word : ', s)

# 예제 4
my_info = {
    "name": 'Lee',
    "Age": 33,
    "City": "Seoul"
}

for key in my_info:
    print('key : ', my_info[key])

for v in my_info.values():
    print('value : ', v)

print()

# 예제 5
name = 'FineAppleE'

for n in name:
    if n.isupper(): # isupper 는 대분자인지 검사
        print(n)
    else:
        print(n.upper())

#한 줄로 나오도록 만들어보기
print()

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:
        print('Found : 34!')
    else:
        print('Not found : ', num)
# 34 를 찾은 이후에도 실행된다
print()

for num in numbers:
    if num == 4:
        print('Found : 34!')
        break
    else:
        print('Not found : ', num)
# 4를 찾은 이후 실행 정지
print()

# continue

# 자료형 중 숫자만 표시하고 싶을 떄 스킵할려면
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool: # 자료형을 대조할 때는 = 아닌 is를 쓴다 ; is not 도 있다
        continue # 불린은 스킵하게된다.
    print("current type : ", v, type(v))
    print("multiply by 2", v * 3)

print()

# for - else
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 24:
        print("Found : 24")
        break
else:
    print('Not Found : 24')

for num in numbers:
    if num == 49:
        print("Found : 49")
        break
else:
    print('Not Found : 49')
# for 문을 모든 원소에 대해 반복했을 경우 else 가 실행된다
print()


# 구구단 출력

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end = '')
    print()

print()

# 변환 예제

name2 = 'Ace man'

print('Reversed', reversed(name2)) # id 값이 나온다
print('List', list(reversed(name2))) # 리스트로 형변환 하면 제대로 나온다
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2))) # 집합이라 순서가 없다







print()
