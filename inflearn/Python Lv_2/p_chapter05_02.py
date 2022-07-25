# Chapter05-02
# 일급 함수(일급 객체)
# 클로저 기초

# 파이썬 변수 범위(scope)

# 예 1
def func_v1(a):
    print(a)
    print(b)

# func_v1(10) # NameError: name 'b' is not defined

print()

# 예 2
b = 20

def func_v2(a):
    print(a)
    print(b) # 글로벌 변수를 받는다

func_v2(10) # 글로벌 변수 b 를 받아서 a, b 모두 출력된다

print()

# 예 3
c = 30

# def func_v3(a):
#     print(a)
#     print(c) # 아래 로컬 변수 c 를 인식한다 -> 예외 발생
#     c = 40 # 로컬 변수

# func_v3(10) # UnboundLocalError: local variable 'c' referenced before assignment

def func_v3(a):
    c = 40
    print('local a : ', a)
    print('local c : ', c) # 로컬 변수 출력

print('global c : ', c) # 글로벌 변수 출력
func_v3(10) 

print()

# 예 4
c = 30

def func_v4(a):
    global c
    print('local a : ', a) 
    print('local c : ', c) # 글로벌 변수 출력
    c = 40 # 글로벌 변수 c 를 40 으로 치환

print('global c : ', c) # 함수 실행 전 ; 30 출력
func_v4(10)
print('c?? : ', c) # 로컬 변수 출력

print()
print()

# Closure(클로저) 
# 상태를 기억한다 (불변 상태)
# 서버 프로그래밍 -> 동시성 제어(Concurrency)제어 -> 한정된 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock)
# 데드락 회피 방법 -> 메모리를 공유하지 않고 메세지 전달로 처리 -> Erlang 등 
# 클로저는 공유하되 변경되지 않는(Immutable, Read Only) 적극적으로 사용 -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그래밍에 강점

a = 100

print(a + 100)
print(a + 1000)

# 결과 누적(함수 사용)
print(sum(range(1, 51)))
print(sum(range(51, 101)))

print()

# 클래스 이용 클로저 구현
# 평균 구현
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v): # 함수처럼 호출 가능
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성
averager_cls = Averager()

print(dir(averager_cls))

# 누적
print(averager_cls(10)) # 10
print(averager_cls(30)) # 20
print(averager_cls(50)) # 30
print(averager_cls(70))