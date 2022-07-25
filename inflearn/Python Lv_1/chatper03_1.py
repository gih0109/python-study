#형 변환 연습
a = 3. # 3.0 에서 0을 생략
b = 6
c = .7 # 0.7 에서 0 생략
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b)) # b 는 6 - int였는데 6.0 - float 로 형 변환됨
print(int(c)) # c 는 0.7 float 였는데 0 int 로 형 변환됨
print(int(d)) # d 는 12.7 로 float 였는데 12 - int 로 형 변환됨
print(int(True)) # True : 1 , False : 0 을 의미
print(float(False)) # False는 0 인데 float 로 형변환되어 0.0 ehla
print(complex(3))
print(complex('3')) # 문자형 3 이 숫자형 3으로 변환되어 실행됨
print(complex(False))

print()

# 수치 연산 함수
print(abs(-7)) # 절대값

x, y = divmod(100, 8) # 100을 8로 나눈다 x 는 몫, y 는 나머지 할당됨
print(x, y)

print(pow(5, 3), 5 ** 3) # 거듭제곱 함수

# 외부 모듈
import math

print(math.pi) # math 모듈을 호출에서 pi 값 나옴
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수를 찾는다 - 6 나옴
