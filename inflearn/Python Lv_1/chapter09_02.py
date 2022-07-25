# Chapter09-2
# CSV 파일 읽기 및 쓰기

# CSV : MEME - text/csv ; csv 타입 표시

import csv

# 예제 1
with open('./resource/test1.csv', 'r') as f: # 인코딩이 utf-8 이라 생략
    reader = csv.reader(f) # csv 패키지 읽어올 때는 reader 로 연결 해 주면 된다. 파일과 연결된 오픈 함수에서의 변수를 reader 에다 인자로 넘겨주면 csv 파일을 사용할 준비가 되었다는 것
    # next(reader) # Header skip ; 해더 스킵
    # 객체 확인
    print(reader)
    # 타입 확인
    print(type(reader))
    # 속성 확인
    print(dir(reader)) # __iter__ 가 있음 ; 반복 가능 ; for 사용 가능
    print()

    for c in reader:
        # print(c)
        # 타입 확인
        # print(type(c))
        # list to str ; 리스트를 문자열로 바꾸기
        print(' : '.join(c)) # 공백 한칸 띄워짐 ; 포맷 마음대로 변경 가능

# 예제 2
with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|') # delimiter 는 구분자 표시 ; 기본은 ','

    for c in reader:
        print(c)

# 예제 3
with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        # print(c)
        for k, v in c.items():
            print(k, v)
        print('-----------------')

# 예제 4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]] # 중첩 리스트

with open('./resource/write1.csv', 'w', encoding='utf-8') as f:
    print(dir(csv))
    wt = csv.writer(f)
    # dir 확인
    # print(dir(wt))
    # 타입 확인
    # print(type(wt))

    for v in w:
        wt.writerow(v)

# 확인
with open('./resource/write1.csv', 'r') as f:
    check = csv.reader(f)
    print(check)
    for a in check:
        print(' , '.join(a))

# 예제 5
with open('./resource/write2.csv', 'w', encoding='utf-8') as f:
    # 필드명
    fields = ['One', 'Two', 'Three']

    # Dict Writer
    wt = csv.DictWriter(f, fieldnames=fields)
    # Header writerowwt
    wt.writeheader()

    for v in w:
        wt.writerow({'One': v[0], 'Two': v[1], 'Three': v[2]})


print()
