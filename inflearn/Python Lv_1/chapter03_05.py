# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용 (JSON 형태)
# 딕셔너리 자료형 (순서X, 키 중복 X, 수정O, 삭제O)

# 선언
a = {'name': 'kim', 'phone': '01033337777', 'birth': '870514'} # 딕셔너리는 중괄호 사용
# a = {키: 값} ; {key: value}형태
#a = {'name': 'kim', 'name': 'Lee'} 같은 중복 형태 허용 X
b = {0: 'Hello Python'} # 키는 숫자, 문자 등 모든 표현형 가능
c = {'arr': [1, 2, 3, 4]} # 값은 모든 형식 가능

d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': "A",
    'Status': True
}

# 많은 양일 경우 표현
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', "A"),
    ('Status', True)
])
# 명시적이고 원칙적인 정확한 선언  - FM대로 선언
# dict 내 리스트 내 튜플 형태로 넣는다 - : 대신 , 을 넣는다

f = dict(
    Name='Niceman',
    City='Seoul',
    Age='33',
    Grade='A',
    Status=True
)
# 또 다른 선언 방법, 좀 더 편하게 작성 가능

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 출력
print('a - ', a['name'])
# print('a - ', a['name1']) <- 존재하지 않으면 에러가 난다
print('a - ', a.get('name')) # 좀 더 안전한 방법
print('a - ', a.get('name1')) # 에러가 나지 않는다, 존재하지 않으면 None 으로 처리된다
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))
print()

# 딕셔너리 추가
a['address'] = 'seoul' # 그냥 이렇게 하면 추가된다
print('a - ', a)
# a['name'] = 'seoul' # 기존값을 수정한다
a['rank'] = [1,2,3]
print('a - ', a)

# 딕셔너리 길이
print('a - ', len(a)) # len 은 키의 갯수를 센다
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))
print()

# dict_keys, dict_values, dic_items : 반복문(__iter__) 에서 사용 가능

print('a - ', a.keys()) # 키 만 가져온다
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', list(a.keys())) # 리스트로 변환 dict key 들을 리스트로 뽑아올 수 있다
print('b - ', list(b.keys()))

print()

print('a - ', a.values()) # 값 만 가져온다
print('b - ', b.values())
print('c - ', c.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))

print()

print('a - ', a.items()) # 키와 값을 모두 가져올 수 있다
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items())) # 리스트로 변환해서 보여준다
print('b - ', list(b.items()))

print()

print('a - ', a.pop('name'))
print('a - ', a)

print('c - ', c.pop('arr'))
print('c - ', c)

print()

print('f - ', f.popitem()) #  무작위(? 더 알아봐야됨) item(키+값) 을 꺼낸 후 제거
print('f - ', f) # 해당 값이 사라졌다
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)

print()

print('a - ', 'birth' in a)
print('d - ', 'City' in d)

print()

# 수정
a['test'] = 'test_dict'
print('a - ', a)

a['address'] = 'dj'
print("a - ", a)

a.update(birth='910904') # 정석적인 수정 방법
print('a - ', a)

temp = {'address': 'Busan'} # 또다른 수정 방법
a.update(temp)
print('a - ', a)
