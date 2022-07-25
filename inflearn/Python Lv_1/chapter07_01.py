# Chapter07-1
# 파이썬 예외 처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError, ...
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)에서 발생하는 예외 중요
# 1. 예외는 반드시 처리해야 한다
# 2. 로그는 반드시 남긴다
# 3. 예외는 던져진다. 다른곳으로 처리 위임 가능
# 4. 예외 무시 가능 (추천 X)

# SyntaxError : 문법 오류
# print('error)
# print('error'
# if True
#     pass

# NameError : 참조 없음
# a = 10
# b = 15
# print(c)

# ZeroDivisionError

# print(100 / 0)

# IndexError

# x = [50, 70, 90]
# print(x[1])
# print(x[5])
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())

# KeyError

# dic = {'Name': 'Lee', 'Age': 41, 'City': 'Busan'}
# # print(dic['hobby'])
# print(dic.get('hobby')) # 딕셔너리를 가져올 시 get 을 사용하면 예외 발생 X

# 예외 없는 것을 가능하고 프로그램을 작성 -> 런타임 예외 발생 시 예외 처리 권장 (EAFP)

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2())

# ValueError : 참조값 없음

# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200)

# FileNotFoundError

# f = open('test.txt')

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
# x = [1, 2]
# y = (1, 2)
# z = 'test'

# print(x + y)
# print(x + z)
# print(y + z)

# print(x + list(y))
# print(x + list(z))

# 예외 처리 기본 (가장 중요)
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1 : 여러개 가능
# except 에러명2 :
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

name  = ['Kim', 'Lee', 'Park']

# 예제 1
# try:
#     z = 'Kim' # 'Cho' 등 다른 단어로 바꿔보기
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except ValueError: # 예외를 정확히 처리하는게 가장 좋음
#     print('Not found it! : Occured ValueError!')
# else:
#     print('OK! else.')
#
# print()
# print('Pass')

# 예제 2
# try:
#     z = 'Cho' # 'Cho' 등 다른 단어로 바꿔보기
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except Exception: # ValueError 삭제 : 모든 에러 예외 처리, 하지만 정확히 어떤 에러가 발생하는지 알 수 없음
# # except: 처럼 쓸 수도 있음
#     print('Not found it! : Occured Exception!')
# else:
#     print('OK! else.')
#
# print()
# print('Pass')

# 예제 3
# try:
#     z = 'Cho' # 'Cho' 등 다른 단어로 바꿔보기
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except Exception as e:
#     print(e) # 에러 내용 표시
#     print('Not found it! : Occured Exception!')
# else:
#     print('OK! else.')
# finally: # 예외가 발생하던 안하던 실행해야 하는 구문을 finally 로 실행한다
#     print('OK! finally!')
#

# 예제 4
# 예외 임의로 발생시키기 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Park'
    if a == 'Kim':
        print('OK! Pass!')
    else:
        raise ValueError
except ValueError:
    print('Occurred! Exception!')
else:
    print('OK! else!')
