# Chapter04-3
# 파이썬 반복문
# While 실습

# While <expr>:  expression 줄여서 expr
#   <statement(s)>
# if 와 사용법이 똑같다. 조건을 만족할때까지 반복

# 예제 1

n = 5
while n > 0:
    print(n)
    n = n - 1 # 이 조건이 없으면 n = 5 > 0 이므로 무한 반복 실행되어 컴퓨터 다운될 수 있음
# 내가 의도하지 않은 대로 무한 반복 실행 가능하기 때문에 주의해야함
# 중간 중간 확인 및 디버깅 필수

print()

# 예제 2
a = ['foo','bar', 'baz']

while a: # while a 자체가 true 상태이므로 무한이 반복 실행될 수 있다
    print(a.pop())

a = ['foo','bar', 'baz']

while a:
    print(a.pop(-1)) # -1 을 써서 명시적으로 표현 가능

print()

# 예제 3
# break, continue
n = 5
while n > 0:
    n -= 1 # n = n - 1 과 동일
    if n == 2:
        break
    print(n)
print('Loof Ended.')

# 예제  4
m = 5
while m > 0:
    m -= 1 # n = n - 1 과 동일
    if m == 2:
        continue # n = 2 일때 패스된다
    print(m)
print('Loof Ended.')

print()

# if 중첩
# 예제 5
i = 1

while i <= 10:
    print('i = ', i)
    if i == 6:
        break
    i += 1

print()

# while - else 구문
# 예제 6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')

print()

n = 10
while n > 0:
    n -= 1
    print(n)
else:
    print('else out.') # while 구문이 끝나는 것을 확인

# 예제 7
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'

i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list.')

a = ['foo', 'bar', 'baz', 'qux']
s = 'kim'

i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list.')

# 무한반복 조심
# while true:
#   print('Foo')

# 예제 8
a = ['foo', 'bar', 'baz', 'qux']

while True:
    if not a:
        break
    print(a.pop())


print()
