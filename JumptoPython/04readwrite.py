# f = open('./readandwrite.txt', 'w', encoding='UTF-8')
# f.close()
#
# # writedata
# f = open('./readandwrite.txt', 'w', encoding='UTF-8')
# for i in range(1, 11):
#     data = '{}번째 줄입니다.\n'.format(i)
#     f.write(data)
# f.close
#
# # readline 함수를 사용하여 읽기
# f = open('./readandwrite.txt', 'r', encoding="UTF-8")
# line = f.read()
# print(line)
# f.close()

# 파일에 새로운 내용 추가하기
# f = open('./readandwrite.txt', 'at')
# for i in range(11, 21):
#     data = '{}번째 줄입니다.\n'.format(i)
#     f.write(data)
# f.close()
#
# print()

# with open('./readandwrite.txt', 'w') as f:
#     f.write('Life is too short, you need python')
