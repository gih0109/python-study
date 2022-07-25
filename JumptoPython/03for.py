
import time
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
#    time.sleep(1)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

# for 문의 응용
marks = [90, 25, 67, 45, 80]

# "총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고
# 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오."
numbers = 0
for b in marks:
    numbers += 1
    if b >= 60:
        print('Student {} is Pass'.format(numbers))
    else:
        print('Student {} is Fail'.format(numbers))

#앞에서 for문 응용 예제를 그대로 사용해서 60점 이상인 사람에게는 축하 메시지를 보내고
#나머지 사람에게는 아무 메시지도 전하지 않는 프로그램을 에디터를 사용해 작성해 보자.

numbers = 0
for b in marks:
    numbers += 1
    if b >= 60:
        print('congratuation! {} is passed'.format(numbers))
    else:
        continue
print()

range1 = range(10)
print(range1)
range2 = range(0, 10)
print(range2)

# 1 부터 10 까지 더하기

add = 0
for i in range(1, 11):
    add = add + i

print(add)
print()

# 구구단
for i in range(2, 10):
    for j in range(2, 10):
        print(i * j, end = ' ')
    print(' ')
print()

# 리스트 내포 사용하기
a = [1, 2, 3, 4]
result1 = []
for num in a:
    result1.append(num * 3)
print(result1)

a = [1, 2, 3, 4]
result2 = [numbers * 3 for numbers in a]
print(result2)

a = [1, 2, 3, 4]
result3 = [num for num in a if num % 2 == 0]
print(result3)

a = [1, 2, 3, 4]
result4 = []
for num in a:
    if num % 2 != 0:
        result4.append(num)
print(result4)

a = [1, 2, 3, 4]
result5 = [num for num in a if num % 2 != 0]
print(result5)

print()
