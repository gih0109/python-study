# Chapter03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형 (순서O, 중복O, 수정X, 삭제X) # 불변

# 선언

a = () # 소괄호로 묶어주면 선언
b = (1,) # 원소가 하나일 때는 , 를 찍어나야 튜플로 인식
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

#인덱싱
print('>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1])) #튜플을 리스트로 형변환 가능
print()

# 수정 가능 확인
# d[0] = 1500 # 에러가 난다

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])
print()

# 튜플 연산
print('>>>>>')
print('c + d', c + d) # 덧셈 가능
print('c * 3', c * 3) # 곱셈 가능
print()

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))
print()

# 팩킹 & 언팩킹 (Packing & Unpacking)

# 팩킹 - 하나로 묶는다
t = ('foo', 'bar', 'baz', 'qux') # 이것 자체가 4개의 원소를 하나로 묶은 패킹이다
# 튜플을 선언하는 것과 마찬가지이다

print(t)
print(t[0])
print(t[-1])

# 언패킹 1 - 묶여있던 것을 푸는 것
(x1, x2, x3, x4) = t # 정석
# x1, x2, x3, x4 = t 처럼 괄호 생략 가능,
# 하나로 묶여있던 원소들을 각각 x1, x2, x3, x4에 할당

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4) # 하나로 묶여있던 원소들을

# 팩킹, 언팩킹
t2 = 1, 2, 3 # 튜플 선언, 괄호 생략해도 튜플 선언이다
t3 = 4, # 원소가 1개일때는 , 넣어야 튜플 선언된다
x1, x2, x3 = t2 # 언패킹
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)





print()
