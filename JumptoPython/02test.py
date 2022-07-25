# 문제 1
q1 = {
'국어': 80,
'영어': 75,
'수학': 55
}

print(q1)
print(list(q1.values()))

q11 = list(q1.values())
print(q11[0])
print()
print((q11[0] + q11[1] + q11[2]) / len(q11))
print()

# 문제 2
q2 = 13
if q2 % 2:
    print('{} 는 홀수이다'.format(q2))
else:
    print('{} 는 짝수이다'.format(q2))

# 문제 3
s3 = '881120-1068234'
year = s3[0:2]
month = s3[2:4]
date = s3[4:6]
pcode = s3[7:]
print('홍길동의 생일은 {0}년 {1}월 {2}일 이고 주민번호 뒷자리는 {3} 이다.'.format(year, month, date, pcode))

# 문제 4
pin = "881120-1068234"
print(pin[7])
print()

# 문제 5
a = "a:b:c:d"
b = a.replace(":", ",")
print(b)
print()

# 문제 6
q6 = [1, 3, 5, 4, 2]
q6.sort()
q6.reverse()
print(q6)
print()

# 문제 7
q7 = ['Life', 'is', 'too', 'short']
print(" ".join(q7))
print()

# 문제 8
q8 = (1, 2, 3)
# q81 = list(q8)
# q81.append(4)
# print(tuple(q81))
q81 = q8 + (4,)
print(q81)

print()

# 문제 9
# 2, 자료형이 세트라서?

# 문제 10
a = {'A':90, 'B':80, 'C':70}
q10 = list(a.items())
print(q10[1][1])
q101 = list(a.values())
print(q101[1])
valueB = a.pop('B')
print(valueB)


# 문제 11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
q11 = set(a)
print(q11)
