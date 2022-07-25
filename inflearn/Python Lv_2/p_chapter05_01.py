# Chapter05-01
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화 (실행시점 초기화)
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)

# 팩토리얼을 함수로 만들어보기
# 5! = 5 * 4 * 3 * 2 * 1

# 함수 객체

def factorial(n):
    ''' Factorial Funtion -> n : int '''

    if n == 1: # n < 2
        return 1
    return n * factorial(n-1) # 재귀함수

class A:
    pass

# 객체 취급 증명
print(factorial(5))
print(factorial.__doc__) # 주석 확인
print(type(factorial), type(A))
print(dir(factorial)) # '__repr__', '__lt__' 를 가지고 있다 -> 함수지만 객체 취급

print()

print(set(sorted(dir(factorial))) - set(sorted(dir(A)))) # 함수 속성 - 클래스 속성; 함수가 가진 속성만 나온다
print(factorial.__name__)
print(factorial.__code__) 

print()
print()

# 변수 할당 확인
var_func = factorial

print(var_func) # 변수로서 할당됨 ; <function factorial at ~~~~>
print(var_func(10))
print(list(map(var_func, range(1, 11))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Hihger-order funtion)
# map, filter, reduce
# javascript 의 es6 

print(list(map(var_func, filter(lambda x: x % 2, range(1, 6))))) # lambda: 익명함수, filter 의 인수로 전달되었다
print([var_func(i) for i in range(1, 6) if i % 2]) # i % 2 홀수만, 1 ~ 5 까지

print()
print()

# reduce 함수
from functools import reduce
from operator import add

print(sum(range(1, 11)))
print(reduce(add, range(1, 11)))

# 익명함수(lambda)
# 가급적 주석을 작성
# 가급적이면 함수를 작성
# 일반 함수 형태로 리팩토링 권장

print(reduce(lambda x, t: x + t, range(1, 11)))

print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인
print(callable(str)) # 호출가능 -> True
print(callable(A))
print(callable(list), callable(var_func), callable(factorial), callable(3.14))

print()
print()

# partial 사용법 : 인수 고정 -> 콜백 함수 사용
from operator import mul
from functools import partial

print(mul(10, 10))

# 인수 고정
five = partial(mul, 5) # 5 * ?? 두개의 변수 중 하나 고정

print(five(10))
print(five(100))

# 고정 추가
six = partial(five, 6)
print(six()) # 둘 다 고정되었음

print([five(i) for i in range(1, 11)])
print(list(map(five, range(1, 11))))