# 문제 1

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

# 위 클래스를 상속하는 UpgradeCacultor 를 만들고 뺄셈 메소드 추가

class UpgradeCacultor(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCacultor()
cal.add(10)
cal.minus(7)
print(cal.value)

# 문제 2

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
        else:
            return self.value

cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기
print(cal.value) # 100 출력

# 문제 3 다음 결과 예측
# all([1, 2, abs(-3)-3])  - False
# chr(ord('a')) == 'a' - True

# 문제 4
# filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.
print(list(filter(lambda a: a > 0, [1, -2, 3, -5, 8, -3])))

# 문제 5
print(int(0xea))

# 문제 6
# map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.
print(list(map(lambda a: a * 3, [1, 2, 3, 4])))

# 문제 7 최대값, 최소값의 합
q7 = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(q7) + min(q7))

# 문제 8
print(round(17/3, 4))

# 문제 9



# 문제 11
import sys
import glob
print(glob.glob('./*.py'))

# 문제 12
import time

# print(list(time.localtime()))
q12 = list(time.localtime())
print('{}/{}/{} {}:{}:{}'.format(q12[0], q12[1], q12[2], q12[3], q12[4], q12[5]))
q12_1 = time.strftime("%Y/%m/%d %H:%M:%S")
print(q12_1)


# 문제 13
# random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개) 를 생성해 보자. 단 중복 X

import random

data = list(range(1, 46))
# print(data)
# print(random.choice(data))

count = 6
lotto_result = []

while count != 0:
    num = random.choice(data)
    lotto_result.append(num)
    data.remove(num)
    count -= 1

print(lotto_result)
