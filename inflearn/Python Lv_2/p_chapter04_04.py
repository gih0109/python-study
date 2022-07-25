# # Chapter04-04
# 시퀀스형(순서있음)
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> 키 중복 허용 x, set -> 중복 허용 x

# Dict 및 set 심화

# immutable Dict (수정 불가능 Dict) ; 읽기 전용

from types import MappingProxyType

d = {'key1': 'value1'}

# Read Only
d_frozen  = MappingProxyType(d) #

print(d, id(d))
# print(hash(d)) # 예외 발생
print(d_frozen, id(d_frozen))
# print(hash(d_frozen)) # 예외 발생

# 수정 불가
# d_frozen['key2'] = 'value2' # 예외 발생, 수정 불가

# 수정 가능
d['key2'] = 'value2'
print(d)

print()
print()

# set 선언
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set() # not {}
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}) # 읽기 전용 set

# set 에 요소 추가
s1.add('Melon')
print(s1)

# 추가 불가
# s5.add('Melon') # 예외 발생

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
from dis import dis

# 선언 방법에 따른 최적화 차이
print('-----------')
print(dis('{10}')) # 3단계 실행 # 미세하게 더 빠르다
print('-----------')
print(dis('set([10])')) # 5단계 실행 

# 지능형 집합(Comprehending Set)

print('-----------')

from unicodedata import name

# print({name(chr(i), '') for i in range(0, 256)})