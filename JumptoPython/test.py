# with open('./test.txt', 'a') as f:
#     f.write(input('입력 : '))
#     f.write('\n')

# 문제 7
with open('./test.txt', 'r') as f3:
    body = f3.read()

body2 = body.replace('java', 'python')

with open('./test.txt', 'w') as f4:
    f4.write(body2)
