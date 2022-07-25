s2 = set("Hello")
print(s2)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)

s1.add(7)
print(s1)
s1.update([8, 9, 10])
print(s1)
s1.remove(5)
print(s1)
print()

a = [1, 2, 3, 4]

while a:
    a.pop()
    print(a)

print()

b = [1, 2, 3, 4, 5]

while len(b) > 0:
    b.pop()
    print(b)

a = [1, 2, 3, 4]
b = a[:]
print(a)
print(b)
print(id(a) == id(b))

from copy import copy
a = [1, 2, 3, 4, 5]
b = copy(a)
print(a)
print(b)
print(id(a) == id(b))
