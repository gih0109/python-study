# Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서 O, 중복 O, 수정 O, 삭제 O)

# 선언
a = [] # 빈 리스트는 대괄호로 선언
print(type(a)) # 리스트라고 표시해줌

b = list() # 빈 리스트의 또다른 선언 방식
c = [70, 75, 80, 85] # 4 가지 원소를 가지고 있다
print(len(c))

d = [1000, 10000, 'Ace', 'Base', 'Captine'] # 서로 다른 자료형을 한 리스트에 담을 수 있다
e = [1000, 10000, ['Ace', 'Base', 'Captine']] # 리스트 안에 또 다른 리스트를 넣을 수 있다. 3번째
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱 - 원하는 데이터를 꺼내오는 과정
print('>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1]) # d[1] 은 d 내 1번을 가져오는 명령 0,1,2,3 중 2번
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1]) # 마이너스는 오른쪽 끝에서부터 -1, -2, -3, -4 ...
print('e - ', e[-1][1]) # e[-1] 은 ['Ace', 'Base', 'Captine'] 이고 여기서 [1] 은 base 이다
print('e - ', list(e[-1][1])) # 리스트 형태로 형변환 Base -> B, a, s, # -*- coding: utf-8 -*-

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3]) # e[-1] 은 ['Ace', 'Base', 'Captine'] 이고 [1:3] 은 1부터 3-1까지이기 때문에 1 - base, 3-1=2 - captine /??

# 리스트 연산 : 집합 더하기 집합은 집합
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
# print("'Test' + c[0]", 'Test' + c[0]) <- 에러가 난다 : 형변환 시켜주면 된다
print("'Test' + c[0]", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:]) # 값 비교 ==
print(c)
print(c[:3] + c[3:])
print()

# Identity(id)

temp = c
print(temp, c)
print(id(temp))
print(id(c)) # 변수 할당 시 똑같은 id 가 나온다
print()

# 리스트 수정, 삭제
c[0] = 4 # c의 첫 번째 리스트를 4로 바꾼다
print('c - ', c)
c[1:2] = ['a', 'b' ,'c'] # 1 부터 2-1=1 까지 항목을 바꾼다 -> 1 의 항목을 바꾼다.
# 슬라이싱 했을떄는 'a', 'b', 'c' 가 원소로 들어간다
#  c[1:2] = [['a', 'b' ,'c']] (대괄호 2개)가 되면 리스트 안에 리스트가 들어간다. 두번째 항목이 리스트가 된다.
print('c - ', c)
c[1] = ['a', 'b' ,'c'] # c[1] = ['a', 'b' ,'c'] 할 때는 리스트로 들어간다
print('c - ', c)
c[1:3] = [] # 리스트 부분이 삭제된다, 이렇게 제거하지는 않는다
print('c - ', c)
del c[2] # 제거 함수
print('c - ', c)
print()


# 리스트 제공 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
# a[5] = 10 # 이런 방식으로 뒤에 리스트를 추가할 수 없다
# print('a - ', a)
a.append(10) # 마지막 끝부분에 데이터 삽입 시 쓰는 함수
print('a - ', a)
a.sort() # 오름차순으로 정렬
print('a - ', a)
a.reverse() # 데이터를 반대로 정렬
print('a - ', a)
print('a - ', a.index(3), a[3]) # 인덱스를 가져오는 방법 a.index(), 생략시 a[]
a.insert(2, 7) # 삽입 함수, 2번째 자리에 7을 넣는다
print('a - ', a)
a.reverse()
print('a - ', a)
# del a[6] # 6번째 지우기, 일일이 찾기 귀찮다
a.remove(10) # 리스트 중 10 제거
print('a - ', a)
print('a - ', a.pop()) #마지막에 있는 원소를 꺼내온 뒤 리스트에서 제거한다
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4)) # 4 의 개수를 찾는다. count - 해당 데이터의 숫자를 찾을 때 쓰는 함수
ex = [8, 9]
a.extend(ex) # 연장 함수
print('a - ', a)
print()

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)





print()
