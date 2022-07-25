money = 2000

if money >= 3000:
    print('택시')
else:
    print('도보')
print()

money = 2000
card = True

if money >= 3000 or card == True:
    print('택시')
else:
    print('도보')
print()

pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print('taxi')
else:
    print('walk')

# 조건문 아무것도 안하기
if 'money' in pocket:
    pass
else:
    print('walk')
print()

# 다중조건문
pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print('taxi')
elif 'card' in pocket:
    print('taxi')
else:
    print('walk')
