# Chapter08-2
# 파이썬 외장(External)함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time, tandom 등

# 예제 1
import sys
print(sys.argv) # sys.argv 구글에서 검색해보기

# 예제 2 (강제종료)
# sys.exit() # 사용 주의

# 예제 3 (파이썬 패키지 위치)
print(sys.path)

# pickle : 객체 파일 읽기&쓰기, 파이썬에서 쓸 수 있는 객체들을 저장장치에 쓰고 읽을 때 사용하는 함수
import pickle

# 예제 4 (쓰기)

f = open("test.obj", 'wb') # w : write , b : binary (바이너리)
obj = {1: 'python', 2:'study', 3:'basic'} # 작성할 파이썬 바이너리
pickle.dump(obj, f) # pickle 에 dump 를 호출하면 쓴다. object 를 쓰고 파일을 연결한 open 함수는 f
f.close() # open 했으면 반드시 닫아줘야 한다.
# 계속 열고 닫지 않으면 언젠간 connection fool 같은 에러가 날 수 있다. 반드시 내가 쓴 리소스는 반환해야 한다

# 예제 5 (읽기)
f = open('test.obj', 'rb') # r : read, b : binary
data = pickle.load(f) # 읽을때는 load
print(data, type(data))
f.close()

# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir, rmdir(비어 있으면 삭제), rename

# 예제 6
import os
print(os.environ) # 내가 사용하는 컴퓨터의 정보가 나온다
print(os.environ["USERNAME"])
print(os.environ["ATOM_HOME"])

# 예제 7
print(os.getcwd()) # 현재 파이썬이 실행되고 있는 경로를 표시

# time : 시간 관련 처리
import time

# 예제 8
print(time.time()) # 현재 시간, 시분초, 밀리세컨드까지 나온다

# 예제 9 (형태 변환)
print(time.localtime(time.time())) # 보기 편하게 변환해주는 메소드

# 예제 10 (간단 표현)
print(time.ctime()) # 일반적으로 시간 표현으로 변환

# 예제 11 (형식 표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) # 원하는 형식대로 표현 가능

# 예제 12 (시간 간격 발생)
# for i in range(5):
#     print(i)
#     time.sleep(1) # 1초마다 쉬었다가 for 문을 실행

# random : 난수 리턴
import random

# 예제 13
print(random.random()) # 0 ~ 1 사이의 실수

# 예제 14
print(random.randint(1, 100)) # randint(x1, x2) : x1 과 x2 사이 정수 랜덤
print(random.randrange(1, 100)) # randrange(x1, x2) : x1 과 x2-1 사이 정수 랜덤

# 예제 15(섞기)
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)

# 예제 16 (무작위 선택)
c = random.choice(d) # 리스트 중 무작위로 하나 선택
print(c)

# webbrowser : 본인 OS 의 웹 브라우저 실행
import webbrowser

# webbrowser.open("http://google.com")
#
# webbrowser.open_new("http://google.com") # 새 창으로 열기

print()
