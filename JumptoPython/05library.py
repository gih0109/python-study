# library

# sys
import sys
print(sys.argv)




# pickle

# import pickle
# with open('./test2.txt', 'wb') as f:
#     data = {1: 'pythion', 2: 'you need'}
#     pickle.dump(data, f)
#
# print('write test2.txt complete!')

import pickle
with open('./test2.txt', 'rb') as f:
    data = pickle.load(f)
    print(data)
print()

# OS
import os
print(os.environ)
print(os.environ['PATH'])

# print(os.system('dir'))

# glob 특정 디렉토리 내 파일 이름 모두 알아내는 기능
import glob
a1 = glob.glob('C:/Python Basic/chapter*')
print(a1)

# tempfile 임시파일 만들기

# time
import time
print(time.time())
print(time.localtime())
print(time.asctime())
print(time.ctime())

# calendar
import calendar
print(calendar.calendar(2021))

# randaom
import random
print(random.random())
print(random.randint(1, 10))
print()

def random_pop1(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop1(data))
print()

def random_pop2(data):
    number = random.choice(data)
    data.remove(number)
    return number

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop2(data))

# webbrowser
# import webbrowser
# webbrowser.open('http://google.com')
