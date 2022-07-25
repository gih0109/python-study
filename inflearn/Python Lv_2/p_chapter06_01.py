# Chapter06-01
# 병행성(Concurrency)
# 이터레이터(Iterator), 제네레이터(Generator)

# 파이썬 반복 가능한 타입
# callections, text, list, Dict, Set, Tuple, unpacking, *args, ....
# -> iterable(반복 가능)

t = 'ABCDEFG'

# print(dir(t))
for c in t:
    # print(c, end=' ')
    pass

# 반복 가능한 이유 -> 내부적으로 iter(x) 함수 호출

w = iter(t)
# print(dir(w)) # __next__ 가 있다
print(next(w)) # A
print(next(w)) # B
print(next(w)) # C ... : 다음에 나올 것을 기억한다

# while 로 구현
while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()

# 반복형 확인
print(hasattr(t, '__iter__')) # True가 나온다 ; dir 중 __iter__ 가 있다

# 반복형 확인 또 다른 방법
from collections import abc
print(isinstance(t, abc.Iterable)) # Iterable 을 상속 받았는지 확인

print()
print()

# 클래스 기반 제네레이터 구현

# next 사용
# 클래스 매직 메소드 next 구현
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        # print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.') # 예외처리 해야함
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wi = WordSplitter('Do today what you could do tomorrow')

print(wi)
print(next(wi)) # class 지만 iterable 하다
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))

print()
print()

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 생성 가능 -> 데이터 양 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Corotine) 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self): # iter 메소드 사용하여 제네레이터 구현
        for word in self._text:
            yield word # 제네레이터 # yield 에서 다음 위치 상태를 기억함
        return # return 굳이 사용할 필요 없음

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wg = WordSplitGenerator('Do today what you could do tomorrow')

wt = iter(wg)

print(wt)
print(wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))