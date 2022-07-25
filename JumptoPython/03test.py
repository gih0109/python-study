# 문제 1
# shirt 가 나온다

# 문제 2
# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
q2 = 0
result2 = 0
while q2 <= 1000:
    q2 += 1
    if q2 % 3 != 0:
        continue
    result2 = result2 + q2
print(result2) # 166833
print()

# 문제 3
# while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
q3 = 1
while q3 < 6:
    print('*' * q3)
    q3 += 1

print()


# 문제 4
# for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
for q4 in range(1, 101):
    print(q4, end=" ")
print('')

# 문제 5
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.
a5 = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

a = 0
for q5 in a5:
    a = a + q5
print(a/len(a5))

# 문제 6
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
print(result)

result6 = [n*2 for n in numbers if n % 2 == 1]
print(result6)



print()
