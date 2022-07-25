# Chapter08-1
# 파이썬 내장(Built-in) 함수
# 자주 사용하는 함수 위주로 실습
# 사용하다 보면 자연스럽게 숙달
# str(), int(), tuple() 형변환 이미 학습

# 절대랎
# abs()
print(abs(-3))

# all : iterable 요소 검사 (참, 거짓) ; 모두 True 이어야 True, 하나라도 False 이면 False
print(all([1,2,3]))
print(all([0,2,3])) # 0 -> false
print(all([0,2,''])) # 빈문자열 -> false

# any ; 하나라도 True 이면 True
print(any([1,2,3]))
print(any([0,2,3]))
print(any([1,2,'']))

# chr : 아스키코드 -> 문자, ord : 문자 -> 아스키 (중요, 자주사용)
print(chr(67))
print(ord('C'))

# enumerate : 인덱스 + iterable 객체 생성 (중요, 자주사용)
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)

# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출 (중요, 자주사용)
def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
# 람다식으로
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))

# id : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(4))

# Len : 요소의 길이 반환
print(len('abcdefg'))
print(len(([1,2,3,4,5,6,7])))

# max, min : 최대값, 최소값
print(max([1,2,3]))
print(max('python study'))
print(min([1,2,3]))
print(min('pythonstudy'))

# map : 반복 가능한 객체 요소를 지정한 함수를 실행 후 추출 (중요, 자주사용)
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1,-3,2,0,-5,6])))
# 람다
print(list(map(lambda x: abs(x), [1,-3,2,0,-5,6])))

# pow : 제곱값 반환
print(pow(2,10))

# range : 반복가능한 객체(Iterable) 반환
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))

# round : 반올림
print(round(6.5781, 2)) # round(소수, 반올림해서 나타낼 소수 자리 수)
print(round(5.6))

# sorted : 반복가능한 객체(Iterable) 정렬 후 반환
print(sorted([6,7,4,3,1,2]))
a = sorted([6,7,4,3,1,2])
print(a)
print(sorted(['p', 'y', 't', 'h', 'o', 'n'])) # 알파벳 순서대로 정렬됨

# sum : 반복가능한 객체(Iterable) 합 반환
print(sum([6,7,8,9,10]))
print(sum(range(1,101)))

# type : 자료형 확인
print(type(3))
print(type({}))
print(type(()))
print(type([]))

# zip : 반복가능한 객체(Iterable)의 요소를 묶어서 반환
print(list(zip([10,20,30], [40,50,60])))
print(list(zip([10,20,30], [40,50,]))) # 짝이 안 맞을 경우 짝이 맞는 것만 반환
print(type(list(zip([10,20,30], [40,50,60]))[0])) 






print()
