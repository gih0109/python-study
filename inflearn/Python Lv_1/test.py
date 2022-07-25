print('Test calculater')
print('input number A and B and +,-,*,/')

# def add(x, y):
#     return x + y
#
# def subtract(x, y):
#     return x - y
#
# def multiply(x, y):
#     return x * y
#
# def devide(x, y):
#     return x / y


x1 = int(input('Enter Number 1 : '))
x2 = int(input('Enter Number 2 : '))
x3 = input('+,-,*,/ : ')

#if type(x1) == str:
#    print('please input numbers')

# if not x3 == '+' and not x3 =='-' and not x3 == '*' and not x3 == '/':
#     print('please input +,-,*,-')

if x3 == '+':
        print(x1 + x2)
elif x3 == '-':
        print(x1 - x2)
elif x3 == '*':
        print(x1 * x2)
elif x3 == '/':
        print(x1 / x2)
else:
    print('Error!')
    print('please input +,-,*,-')
