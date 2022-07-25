# 모듈 사용 실습

import sys

print(sys) # built in ; 파이썬 내부적으로 사용하는 모듈이라고 표시됨
print(sys.path) # 해당 모듈이 어느 경로에 있는지 확인 가능

print(type(sys.path))

# 모듈 경로 삽입
# sys.path.append('C:\math')

# print(sys.path)

# import test_module

# 모듈 사용
# print(test_module.power(10, 3))

import chapter06_02

print(chapter06_02.add(10, 1000))
