def add1(a, b):
    return a + b

a1 = 123
b1 = 324
c1 = add1(a1, b1)
print(c1)
print()

def add2(a, b):
    value = a + b
    return value

a2 = 2325
b2 = 8783
c2 = add2(a2, b2)
print(c2)
print()

def say():
    return('Hi')

a3 = say()
print(a3)

# 결과값이 없는 함수
def add3(a, b):
    print('{}, {}의 합은 {} 입니다.'.format(a, b, a + b))

add3(3, 4)
a4 = add3(3, 4)
print(a4)
print()

# 여러 개의 입력값을 받는 함수 만들기
def add_many(*args):
    value = 0
    for i in args:
        value = value + i
    return value

a5 = add_many(1,2,3)
print(a5)
a6 = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(a6)
print()

def add_mul(choice, *args):
    if choice == 'add':
        value = 0
        for i in args:
            value = value + i
    elif choice == 'mul':
        value = 1
        for i in args:
            value = value * i
    return value

a7 = add_mul('add', 1,2,3,4,5)
print(a7)
a8 = add_mul('mul', 1,2,3,4,5)
print(a8)

# def args_func(*args):
#     for i, v in enumerate(args):
#         print('Result : {}'.format(i), v)
#     print('-------')

def args_func(*args):
    for i, v in enumerate(args):
         print('Result : {}'.format(i), v)
    print('------')
#        value = 'Result : {}'.format(i) + ' ' + v
#    return value

args_func('Lee')
# print(a9)
args_func('Lee', 'Park')

args_func('Lee', 'Park', 'Kim')

# 키워드 파라메터 kwargs
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 1)
print_kwargs(name = 'foo', age = 3)
print()

def say_nick(nick):
    if nick == 'A':
        return
    print('you are fail')

say_nick('A')
say_nick('B')
print()

def say_myself(name, old, man = True):
    print('나의 이름은 {} 입니다.'.format(name))
    print('나이는 {}살 입니다'.format(old))
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

say_myself("박응용", 27)
say_myself("박응용", 27, True)
print()

# 람다
print(3, 4, lambda a, b: a + b)






print()
