# Chapter05-03
# 일급함수(일급객체)
# 클로저 기초
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능

# Closure 사용 (함수 형태)
def closure_ex1():
    # Free variable (자유 변수) ; 내가 사용하려는 함수 바깥에 선언된 변수
    # 클로저 영역
    series = [] # 함수 호출이 끝나도 기억한다

    def averager(v): # 함수 내 함수가 있는 형태
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)

    return averager # 함수 자체를 리턴

avg_closure1 = closure_ex1()

print(avg_closure1) # <function closure_ex1.<locals>.averager at ~~~ > 함수가 리턴됨

print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print()
print()

# function inspection
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__)) # co 가 붙은것들이 나온다
print(avg_closure1.__code__.co_freevars) # 자유변수 출력 : series 나온다
print(dir(avg_closure1.__closure__[0].cell_contents)) # ??????

print()
print()


# 잘못된 클로저 사용
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager2(v):
        cnt += 1
        total += v
        return total / cnt
    
    return averager2

avg_closure2 = closure_ex2()
# print(avg_closure2(10)) # 예외 발생 
# UnboundLocalError: local variable 'cnt' referenced before assignment

# 위 클로저 함수 실행
def closure_ex3():
    # Free variable
    cnt = 0
    total = 0

    def averager3(v):
        nonlocal cnt, total # cnt, total 을 free variable 로 만든다
        cnt += 1
        total += v
        return total / cnt
    
    return averager3

avg_closure3 = closure_ex3()

print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))