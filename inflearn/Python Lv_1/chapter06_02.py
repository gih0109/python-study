# Chapter06-2
# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

# 사칙연선 모듈 만들어보기

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    return x / y

def power(x, y):
    return x ** y

# ctrl + / 키 하면 주석처리

# print('-' * 15)
# print('called! inner!') # 내부 테스트
# print(add(5, 5))
# print(subtract(15, 5))
# print(multiply(5, 5))
# print(devide(10, 2))
# print(power(5, 3))

# __name__ 사용 ; 모듈 테스트 시 사용, 다른 곳에서는 실행 안됨
if __name__ == "__main__":
    print('-' * 15)
    print('called! __main__!')
    print(add(5, 5))
    print(subtract(15, 5))
    print(multiply(5, 5))
    print(devide(10, 2))
    print(power(5, 3))
