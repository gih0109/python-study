# 10 번 찍으면 넘어가는 나무

# import time
# treehit = 10

# while treehit > 0:
#     print('나무가 넘어갈 때 까지 {}번 찍어야 합니다'.format(treehit))
#     treehit -= 1
#     time.sleep(1)
#     print('나무 1번 찍음!')
#     time.sleep(1)
#     if treehit == 0:
#         print('나무가 넘어갑니다!')
# print()

# prompt = \
# '''
# 1. Add
# 2. Del
# 3. list
# 4. Quit
#
# '''
#
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input('Enter Number : '))

# coffee = 5
#
# while True:
#     money = int(input('Please input 10$ : '))
#     if money > 10:
#         print('take your coffee, and get your {}$ change.'.format(money - 10))
#         coffee -= 1
#         print('We have {} cup of coffee'.format(coffee))
#     elif money == 10:
#         print('take your coffee.')
#         coffee -= 1
#         print('We have {} cup of coffee'.format(coffee))
#     else:
#         print('please input {} more money'.format(10 - money))
#
#     if coffee == 0:
#         print('Out of stock, Sorry')
#         break


# coffee = 10
# while True:
#     money = int(input("돈을 넣어 주세요: "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee -1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
#         coffee = coffee -1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break

a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)
