# 모듈 2

PI = 3.141592

class Math:
    def __init__(self, r):
        self.r = r

    def solv(self):
        return PI * (self.r ** 2)

    # def solv(self, r):
    #     return PI * (r ** 2)

def add(a, b):
    return a + b


print()

if __name__ == "__main__":
    print(add(1, 2))
    test1 = Math(2)
    print(test1.solv())
