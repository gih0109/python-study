food = 'Python\'s favorite food is perl'
print(food)

text = \
'''
Life is too short
You need python
'''
print(text)

a = 'Life is too short, You need Python'
print(len(a))

print(a[3])
print(a[-4])
print(a[5:7])
print(a[19:])

a = '20010331Rainy'
date = a[0:8]
weather = a[8:]
print('Today is {}, weather is {}'.format(date, weather))
year = a[0:4]
month = a[4:6]
day = a[6:8]
print('Today is {}.{}.{}, today\'s weather is {}'.format(year, month, day, weather))

a = 'Pithon'
print(a[0:1] + 'y' + a[2:])
print(str(a[0:1] + 'y' + a[2:]))

a = 3
print('I eat {} apples'.format(a))
print("I eat %d apples." % 3)
print("I eat %s apples." % 'five')

number = 10
day = 'three'
print('I ate %d apple. so I was sick for %s days' % (number, day))
print('I ate {} apple. so I was sick for {} days'.format(number, day))

print("Error is %d%%" % 98)
print("Error is {}%".format(98))

print("%10s" % "hi")
print("%-10sjain." % "hi")
print("%0.4f" % 3.141592)

print('{0:<10}'.format('hi'))
print('{0:>10}'.format('hi'))
print('{0:^10}'.format('hi'))
print('{0:=^10}'.format('hi'))

print('{0:10.4f}'.format(3.141592))

a = "hobby"
print(a.count('b'))

a = 'Python is the best choice'
print(a.find('b'))
print(a.find('k'))

a = 'Life is too short'
print(a.index('t'))
# print(a.index('k'))

a = ' hi '
print(a.lstrip())
print(a.rstrip())
print(a.strip())

a = 'Life is too short'
print(a.replace('Life', 'Your leg'))
print(set(a.split()))

b = 'a:b:c:d'
print(list(b.split(':')))
