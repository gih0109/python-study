# Chapter05-04
# 데코레이터(Decorater)

# 장점
# 1. 중복제거, 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성체크 -> 공통 함수
# 3. 조립해서 사용 용이

# 단점
# 1. 가독성 감소할 수 잉ㅆ음
# 2. 특정 기능에 한정된 함수 -> 단일 함수로 작성하는 것이 유리
# 3. 디버깅 불편

# 데코레이터 실습

import time

def perf_clock(func):

    def per_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 함수 설정
        result = func(*args) # 부모에서 넘어온 함수가 여기서 실행된다
        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))

        return result

    return per_clocked


# 테스트 할 함수

def time_func1(seconds):
    time.sleep(seconds)

def sum_func1(*numbers):
    return sum(numbers)

# 데코레이터 미사용

none_deco1 = perf_clock(time_func1)
none_deco2 = perf_clock(sum_func1)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco1.__code__.co_freevars)

print('-' * 40, 'Called None Decorator -> time_func1')
print()
none_deco1(1.5)
print('-' * 40, 'Called None Decorator -> sum_func1')
print()
none_deco2(100 + 200 + 300 + 400 + 500)

print()
print()

# 데코레이터 사용

@ perf_clock
def time_func2(seconds):
    time.sleep(seconds)

@ perf_clock
def sum_func2(*numbers):
    return sum(numbers)

print('-' * 40, 'Called Decorator -> time_func2')
print()
none_deco1(1.5)
print('-' * 40, 'Called Decorator -> sum_func2')
print()
none_deco2(100 + 200 + 300 + 400 + 500)