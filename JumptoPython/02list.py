a = [1, 2, ['a', 'b', ['life', 'is']]]
print(a[2][2][0])

b = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(b[2:5])
print(b[3][2])

a = [1, 2, 3]
a[2] = 4
print(a)

del a[1]
print(a)

a = [1, 2, 3, 4, 5, 6]
del a[1:3]
print(a)

a.append(7)
print(a)
a.append([11, 12])
print(a)

print(a.index(6))
a.insert(1, 2)
print(a)
a.remove(5)
print(a)
a.pop()
print(a)
a.extend([8, 9])
print(a)
