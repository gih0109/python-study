# abs (절댓값)
print(abs(5))
print(abs(-7))
print(abs(-9.2))

# all
a1 = all([1, 2, 3])
print(a1)
a2 = all([1, 2, 3, 0])
print(a2)

# any
a3 = any([1, 2, 0])
print(a3)

# chr
print(chr(97))
print(chr(44032))

a4 = dir([1, 2, 3])
print(a4)

a5 = divmod(7, 3)
print(a5)

# enumerate
a6 = enumerate(['foo', 'bar'])
print(a6)

a7 = ['A', 'B', 'C', 'D']
for i, chr1 in enumerate(a7):
    print(i, chr1)

# eval (실행 가능한 문자열을 입력으로 받아 결과값을 돌려준다 )
a8 = eval('1 + 2')
print(a8)
a9 = eval("'hi' + 'a'")
print(a9)
a10 = eval('divmod(4, 3)')
print(a10)
print()

# filter
def positive1(x):
    result = []
    for i in x:
        if i > 0:
            result.append(i)
    return result

a11 = [1,-3,2,0,-5,6]
print(positive1(a11))
print(positive1([1,-3,2,0,-5,6]))

def positive2(x):
    value = x > 0
    return value

print(list(filter(positive2, [1,-3,2,0,-5,6])))

# hex
print(hex(234))
print(hex(3))
print()

# isinstance
class test1:
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def test_func1(self):
        print('t1 = {}, t2 = {}'.format(t1, t2))

a = test1(1, 2)
print(isinstance(a, test1))
b = 3
print(isinstance(b, test1))

# map
def two_times1(numberlist):
    result = []
    for number in numberlist:
        result.append(number * 2)
    return result

a12 = two_times1([1, 2, 3, 4])
print(a12)

def two_times2(x):
    return x * 2

print(list(map(two_times2, [1, 2, 3, 4])))
print(list(map(lambda a: a * 2, [1, 2, 3, 4])))
