# Chapter04-01
# 시퀀스형(순서있음)
# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 리스트 및 튜플 고급
# 지능형 리스트(Comprehending list)
chars = '+_)(*&&^^%$#@!'
# chars[2] = 'h' # 재할당 불가능; str은 불변형

code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

print(code_list1)

# 지능형 리스트
code_list2 = [ord(s) for s in chars] # 컴프리헨션 ; for 보다 살짝 더 빠르다

print(code_list2)

# Comprehending list + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

# 전체출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()

# 제네레이터(Generator) 생성

import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지X)
tuple_g = (ord(s) for s in chars) # 대괄호 대신 소괄호 사용
array_g = array.array('I', (ord(s) for s in chars))

print(tuple_g)
print(type(tuple_g))

# 다음 값 반환
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))

# array
print(array_g)
print(type(array)) # 형태 확인
# array 를 list 로 반환
print(array_g.tolist())

print()
print()

# 제네레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)

print()
print()

# 리스트 주의
# 깊은 복사 얕은 복사

marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~'] * 3] * 4 # 하나의 주소값이 4개가 복사됨

print(marks1)
print(marks2)

# 수정할 시
marks1[0][1] = 'x'
marks2[0][1] = 'x' # 다른 요소까지 다 수정된다

print(marks1)
print(marks2)

print([id(i) for i in marks1]) # id 값이 다름
print([id(i) for i in marks2]) # id 값이 모두 동일