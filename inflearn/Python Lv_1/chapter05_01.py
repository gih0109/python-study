# Chapter05-1
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(Lamda)

# 함수 정의 방법
# def function_name(parameter): 파라메터가 있는 함수도 있고 없는 함수도 있다
#   code

# 함수형 프로그래밍, 일반 명령형 프로그래밍 관해 좀 더 알아보면 좋음

# 예제 1
def first_func(w1): # funtion 을 줄여서 func 라고 적기도 한다, 파라메터는 함수 내부에서 임의로 쓰는 변수
    print("Hello, ", w1)

word = "Goodboy"

first_func(word) # 함수 호출 , 괄호를 안 열면 아무 일도 일어나지 않는다

print(first_func) # first_func 자체가 하나의 객체
print()

# 예제 2

def return_func(w2):
    value =  "Hello, " + str(w2) # w2 에 숫자 등 다른 형식이 올 수 있기 때문에 형변환
    return value
#   return = "hello," + str(w2) 처럼 간단하게 쓸 수도 있다
# 내가 원하는 값을 value 로 만든 다음 return 으로 반환

x = return_func('Goodboy2') # 반환받은 값을 출력
print(x)

print()

# 예제 3 (다중반환)

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)

print(x, y, z)

# 튜플 리턴
def func_mu2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mu2(20)

print(type(q), q, list(q))

# 리스트 리턴
def func_mu2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

p = func_mu2(20)

print(type(p), p, set(p))

# 딕혀너리 리턴

def func_mu3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2': y2, 'v3': y3}

d = func_mu3(30)

print(type(d), d, d.get('v2'), d.items(), d.keys())
print()

# 중요
# *args, **kwargs

# *args(언팩킹)
def args_func(*args): # 매개변수 이름은 자유, 꼭 args 사용 안해도 됨, * 붙은 것이 중요
    for i, v in enumerate(args): # i 는 인덱스(index), v 는 실제 값(value), 이것읆 만들어주는 함수 enumerate
        print('Result : {}'.format(i), v)
    print('-------')
# 매개 변수가 가변으로 온다(정해지지 않음)
# for 로 언팩킹 함, 주로 튜플 형태

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

print()

# **kwargs(언팩킹) ; 딕셔너리형 자료 언팩킹
def kwargs_func(**kwargs): # ** 붙은 것이 중요 , 매개 변수명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-------')

kwargs_func(name1 = 'Lee')
kwargs_func(name1 = 'Lee', name2 = 'Park')
kwargs_func(name1 = 'Lee', name2 = 'Park', name3 = 'Cho')

# 전체 혼합 예제
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', 'Cho', age1=20, age2=30, age3=40)
# 함수를 유연하게 사용할 수 있다.

print()


# 중첩 함수 (함수 안에 함수가 있는 형태)
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 100)

nested_func(100)
# func_in_func(100) # 이 함수는 실행불가
# 함수 내 함수를 호출하면 에러가 난다

print()

# 람다식 예제 (장단점이 있음)
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수 (Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

# 비교
# def mul_func(x, y):
#    return x * y

#lambda x, y: x*y # 함수명이 없어서 따로 변수 선언해야 한다

# 일반적 함수 -> 할당
def mul_func(x, y):
    return x * y

print(mul_func(10, 50))

mul_fun_var = mul_func
print(mul_fun_var(20, 50))

# 람다 함수 -> 할당
lambda_mul_func = lambda x, y: x * y

print(lambda_mul_func(50, 50))

def func_final(x, y, func):
    print('>>>>', x * y * func(100, 100))

func_final(10, 20, lambda x, y: x * y)
# 일시적으로 그 자리에서 함수가 필요할 때 간단하게 람다 함수 사용 가능

# func_final(10, 20, lambda_mul_var)

# 함수 hint 부분은 예제파일 읽어보기


print()
