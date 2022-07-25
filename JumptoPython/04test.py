# 문제 1
# 주어진 자연수가 홀수인지 짝수인지 판별해주는 함수(is_odd)를 작성해 보자.
def is_odd(q1):
    if q1 % 2 == 0:
        print('{}는 짝수입니다.'.format(q1))
    else:
        print('{}는 홀수입니다.'.format(q1))

is_odd(2)
is_odd(5)
print()

# 문제 2
# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
# (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
def average_func(*args):
    sum = 0
    for i in args:
        sum = sum + i
    value = sum / len(args)
    return value

q2_1 = average_func(1, 2, 3, 4, 5)
print(q2_1)
q2_2 = average_func(2, 4, 6, 8, 10)
print(q2_2)
print()

# 문제 3
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print('두 수의 합은 {} 입니다'.format(total))
print()

# 문제 4 - 3

# 문제 5
with open("./test.txt", 'w') as f1:
    f1.write("Life is too short")

f2 = open("test.txt", 'r')
print(f2.read())

# 문제 6
with open('./test.txt', 'a') as f2:
    f2.write(input())

# 문제 7
with open('./test.txt', 'r') as f3:
    body = f3.read()

body2 = body.replace('java', 'python')

with open('./test.txt', 'w') as f4:
    f4.write(body2)




print()
