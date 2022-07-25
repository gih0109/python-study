# Chapter04-02
# 시퀀스형(순서있음)
# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# Tuple Advanced
# Unpacking

# b, a = a, b

print(divmod(100, 9))
print(divmod(*(100, 9))) # tuple 은 앞에 * 을 붙여야 unpacking 되서 함수가 실행된다
print(*(divmod(100, 9))) # (11, 1) 이 unpacking 되어서 11, 1 로 프린트됨

print()

# x, y, rest = range(10) # error 발생 ; too many values to unpack
x1, y1, *rest1 = range(10) # * 붙여서 unpacking
print(x1, y1, rest1)
x2, y2, *rest2 = range(2)
print(x2, y2, rest2)
x3, y3, *rest3 = 1, 2, 3, 4, 5
print(x3, y3, rest3)

print()
print()

# Mutable(가변) vs Immutable(불변)

l = (15, 20, 25) # 튜플 선언
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(l, id(l)) # id 값이 다르다
print(m, id(m)) # id 값이 다르다

l *= 2
m *= 2

print(l, id(l)) # id 값이 다르다
print(m, id(m)) # id 값이 같다 ; 같은 id 에 재할당됨 ; 메모리 절약??

print()
print()

# 파이썬 정렬
# sort vs sorted
# reverse, key=len, key=str.lower, key=func...

# sorted : 정렬 후 새로운 객체 반환 (원본 수정 X)
# sort : 정렬 후 객체 직접 변경 (원본 수정 O)

# 원본
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

# sorted
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True))
print('sorted - ', sorted(f_list, key=len))
print('sorted - ', sorted(f_list, key=lambda x: x[-1])) # 끝 알파벳 기준 정렬
print('sorted - ', sorted(f_list, key=lambda x: x[-1], reverse=True))
print('orginal - ', f_list)

# sort
# 반환 값 확인(None)
print('sort - ', f_list.sort(), f_list)
print('sort - ', f_list.sort(reverse=True), f_list)
print('sort - ', f_list.sort(key=len), f_list)
print('sort - ', f_list.sort(key=lambda x: x[-1]), f_list)
print('sort - ', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)

# List vs Array 설명
# 리스트 기반 : 융통성, 다양한 자료형, 벙용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환) 
