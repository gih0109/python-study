# Chapter03-6
# 집합(Set) 특징
# 집합(Set) 자료형(순서X, 중복X)

# 선언
a = set()
b = set([1, 2, 3, 4]) # 괄호 안에 원소를 리스트 형식으로 집어넣는다
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate']) # 서로 다른 자료형을 저장할 수 있다
e = {'foo', 'bar', 'baz', 'foo', 'qux'} # 중괄호는 set 에도 사용한다. 리스트를 나열하듯이 선언 가능
# 중복 값 ; 여러개의 중복 값을 넣어도 하나만 표시 된다
f = {42, 'foo', (1, 2, 3), 3.14159} # 튜플도 집어넣을 수 있다

print('a - ', type(a), a, 2 in a) # in 연산자는 사용 가능, 튜플이나 리스트에서 사용가능한 연산자는 모두 사용 가능
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 튜플 변환 ( set -> tuple )
t = tuple(b) # 튜플로 형변환
print('t - ', type(t), t)
print('t - ', t[0], t[1:3]) # 슬라이싱 가능
print()

# 리스트 변환 ( set -> list )
l = list(c)
l2 = list(e)

print('l - ', l)
print('l2 - ', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))
print()

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print('s1 & s2 : ', s1 & s2) # "&" 는 교집합
print('s1 & s2 : ', s1.intersection(s2)) # "&" 의 함수는 intersection 이다

# 합집합
print('s1 | s2 : ', s1 | s2) # "|"(shift 누르고 \) 는 합집합
print('s1 | s2 : ', s1.union(s2)) # 합집합의 함수

# 차집합
print('s1 - s2 : ', s1 - s2) # "-"는 차집합
print('s1 - s2 : ', s1.difference(s2))

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2)) # isdisjoint 는 교집합이 있으면 false, 없으면 True

# 부분 집합 확인
print('subset : ', s1.issubset(s2)) # issubset 은 부분 집합인지 확인
print(s2.issubset(s1))
print('superset : ', s1.issuperset(s2))
print()

# 추가 & 제거
s1 = set([1, 2, 3, 4])

s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)
# remove 로 없는 원소를 삭제할려고 하면 keyerror 가 발생

s1.discard(3)
print('s1 - ', s1)
# discard 로 없는 원소를 삭제하려고 해도 에러 발생 X. 예외 발생 하지 않는다.

s1.clear() # 모두 삭제, list 도 clear 사용 가능
print('s1 - ', s1)



print()
