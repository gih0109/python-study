# Chapter06-3
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분활 된 개별적인 모듈로 구성
# __init__.py : Python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# 상대경로 명령 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용

# 예제 1
import sub.sub1.module1 # 같은 경로???
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1() # 경로를 다 적어서 실행
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print('--------')
print()

# 예제 2
from sub.sub1 import module1
from sub.sub2 import module2 as m2 # as = alias ; 별명 지정

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print()
print('--------')
print()

from sub.sub1 import * # * ; 패키지 경로 내 모든 모듈을 실행, 왠만하면 사용하지 말 것 , 하위에 있는 모든 파일 접근 가능
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()
