# 구구단 n단 구현하기

# 테스트 숫자
num = 2

result = []

for i in range(1, 10):
    mul = num * i
    result.append(mul)

print(result)

def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1
    return result

print(GuGu(2))
