# 필요한 기능은? 메모 추가하기, 메모 조회하기
# 입력 받는 값은? 메모 내용, 프로그램 실행 옵션
# 출력하는 값은? memo.txt

# python memo.py -a "Life is too short" 적을 시 메모를 추가할 수 있도록 만들기

import sys

option = sys.argv[1]

# print(option)
# print(memo)

# if option == '-a':
#     memo = sys.argv[2]
#     f = open('./memo.txt', 'a')
#     f.write(memo)
#     f.write('\n')
#     f.close()
# elif option == '-v':
#     f = open('./memo.txt')
#     memo = f.read()
#     f.close()
#     print(memo)

if option == '-a':
    memo = sys.argv[2]
    with open('./memo.txt', 'a') as f:
        f.write(memo)
        f.write('\n')
elif option == '-v':
    with open('./memo.txt', 'r') as f:
        memo = f.read()
        print(memo)
