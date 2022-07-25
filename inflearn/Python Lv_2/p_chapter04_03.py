# # Chapter04-02
# 시퀀스형(순서있음)
# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 해시테이블
# key에 value를 저장하는 구조 
# 파이선 - dict 해쉬 테이블 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 -> 해시 주소 -> key 에 대한 value 참조

# Dict 구조
# print(__builtins__.__dict__)

# hash 값 확인

t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1)) # hash 함수는 불변형이어야 사용 가능
# print(hash(t2)) # 예외 발생

print()
print()

# Dict Setdefault 예제; 속도가 빠르다
source = (('k1', 'val1'), # 2중 튜플 형태
        ('k1', 'val2'),
        ('k2', 'val3'),
        ('k2', 'val4'),
        ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# Not use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print(new_dict1)

# use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v) # value 에 append
print(new_dict2)

# 주의
new_dict3 = {k: v for k, v in source}
print(new_dict3) # 나중 값이 이전 값을 덮어씌운다