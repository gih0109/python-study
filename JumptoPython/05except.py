try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except IndexError:
    print('인덱싱 할 수 없습니다.')

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)

# 오류 일부러 발생시키기
class Bird:
    def fly(self):
#        raise NotImplementedError
        print("very fast")

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()
print()


class MyError(Exception):
    pass

def say_nick(nick):
    if nick == 'Good':
        raise MyError()
    print()

# say_nick('Bad')
# say_nick('Good')

try:
    say_nick('Bad')
    say_nick('Good')
except MyError as e:
    print(e)
