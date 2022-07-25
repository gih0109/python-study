# chater09-1
# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기 모드 : w, 추가 모드 : a, 텍스트 모드 : t, 바이너리 모드 : b
# 상대 경로('../, ./'), 절대 경로('C:\Django\example..')

# 파일 읽기(Read)
# 예제 1
# f = open('C:\Python Basic\resource\it_news.txt') # 절대 경로
f = open('./resource/it_news.txt', 'r', encoding='UTF-8') # t 가 기본값이고 생략가능 ; rt , 인코딩 형식 : encoding

# 속성 확인
print(dir(f))

# 인코딩 확인
print(f.encoding)

# 파일 이름
print(f.name)

# 모드 확인
print(f.mode) # 읽기 모드가 나온다
cts = f.read()
print(cts)
f.close() # 반드시 닫기

# 예제 2 (with 문, 많이 사용)
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))
# with 문에서는 close 생략 가능 ; 내부적으로 자동으로 리소스가 닫힌다.
print()

# 예제 3
# read(): 전체 읽기, read(10) : 10byte 만 읽기 ; 해당 숫자만큼만 읽는다
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20) # 20byte 만큼 읽는다
    print(c)
    c = f.read(20) # 앞에서 읽은 이후부터 읽는다, 내부적으로 읽은 곳을 기억한다
    print(c)
    f.seek(0, 0) # seek(0, 0) : 커서가 처음으로 돌아간다 , seek 찾아보기
    c = f.read(20)
    print(c)

print()

# 예제 4
# readline : 한 줄 씩 읽기
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

print()

# 예제 5
# readlines : 문서 전체를 읽은 후 라인 단위를 리스트로 저장
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')

print()

# 파일 쓰기 (write)

# 예제 1
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')

# 예제 2
with open('./resource/contents1.txt', 'at') as f: # a : append ; 추가
    f.write('I love python2\n')

# 예제 3
# writelines : 리스틀 되어 있는 것을 파일로 쓰기
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

print()

# 예제 4
with open('./resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file=f) # 프린트문이 콘솔에 출력하는 대신 연결된 파일에 쓰여진다
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)




print()
