# Chpter03-2
# 파이썬 문자형
# 문자형 중

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4)) # len 함수 : 문자열의 길이

# 빈 문자열
str1_t1 = '' # 따옴표 안에 아무것도 안적으면 빈 문자열로 선언됨 나중에 선언 가능
str2_t2 = str() # 빈 문자열 생성

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 escape 문자 사용 ; 구글에서 파이썬 이스케이프 검색
# I'm Boy

# print("I'm Boy")
# print('I'm boy')
print('I\'m Boy') # \를 눌러서 ' 표시해야 오류없음

print('a \t b') # \t 는 Tap 누른 것과 동일
print('a \n b') # \n 는 줄바꿈 ; Enter 누른 것과 동일
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String ; 역 슬러시 '\' 를 신경안씀 ; escape 기능 사용안함
raw_s1 = r'D:\python\test'

print(raw_s1)

# 멀티라인 입력
#multi_str = "okaokodkodakvnaldcnmankdjfnakdflasdkfjalsdfasnflakdnflkdncakslnvaldfjadfaopdfkapfdklasndk"
# 많을 텍스트롤 보기 좋게 적을려면
"""
문자열
멀티라인 입력
테스트
"""
multi_str = '''
string
Multi line
Test
'''

multi_str = \
'''
string
Multi line
Teest
'''

print(multi_str)

# 문자열 연산
str_o1 = 'python'
str_o2 = 'Apple'
str_o3 = 'How are you doing'
str_o4 = 'Seouol Deajeon Busan Jinju'

print(str_o1 * 3) # str_o1 문자열이 3번 반복된다
print(str_o1 + str_o2)
print('y' in str_o1) # str_o1 문자열 안에 'y' 가 있는지 묻는다 - Ture
print('n' in str_o1)
print('P' not in str_o2) # str_o2 문자열 안에 대문자 P가 없는지 묻는다 - Ture
print()

# 문자열 형 변환
print(str(66), type(str(66))) # 66는 숫자가 아니라 문자 66 이다
print(str(10.1))
print(str(True), type(str(True)))
print()

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)
print("Capitalize: ", str_o1.capitalize()) # Capitalize 함수는 소문자를 대문자로 바꿔주는 함수
print("endswith?: ", str_o2.endswith("s")) # 마지막 문자가 s 로 끝나는지 물어보는 함수 - false
print("replace", str_o1.replace("thon", 'good')) # "@@@" 내 문자를 '###' 문자로 바꾼다
print("sorted: ", sorted(str_o1)) # sorted 함수는 어떤 기준으로 문자가 정렬되서 나온다
print("split: ", str_o4.split(' ')) # '##' 를 기준으로 문장이나 단어를 분리한다
print()

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__ 가 있으면 반복할 수 있다

#출력
for i in im_str:
    print(i)

# 슬라이싱
str_s1 = "Nice Python"

print(len(str_s1))

# 슬라이싱 연습
print(str_s1[0:3]) # 3-1 0 1 2???
print(str_s1[5:11]) # [5:] 하면 5부터 끝까지 가져오라는 소리
print(str_s1[:len(str_s1)]) # str_s1[:11] 과 동일, 끝부분 숫자를 모를 때 len함수 사용하면 유용
print(str_s1[:len(str_s1)-1]) # str_s1[:10] 과 동일, 끝부분에서 -1
print(str_s1[1:4:2]) # 1 부터 4 까지 가져오는데 2칸씩 뛰기 스킵
print(str_s1[1:9:2]) # 1 부터 9 까지 가져오는데 2칸씩 뛰기
print(str_s1[-5:]) # 음수는 오른쪽에서 왼쪽으로 읽는다
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1])
print()

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a)) # 문자를 아스키 코드로 변환
print(chr(122)) # 아스키코드를 문자로 변환





print()
