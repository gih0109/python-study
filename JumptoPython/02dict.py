dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}

d = dict(
name = 'pey',
phone = '0119993323',
birth = '1118'
)

print(d)

d['hometown'] = 'Busan'

print(d)

del d['name']
print(d)

a = {"김연아":"피겨스케이팅", "류현진":"야구", "박지성":"축구", "귀도":"파이썬"}

print(a['류현진'])

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())
print(list(a.keys()))

print(a.items())
print(a.get('name'))
print(a.get('hometown'))
