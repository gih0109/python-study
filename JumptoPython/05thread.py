# thread_test

# none multi thread
# import time
#
# def long_task1():
#     for i in range(5):
#         time.sleep(1)
#         print('workting {} \n'.format(i))
#
# print('Start')
#
# for i in range(5):
#     long_task1()
#
# print('END')

# with multi thread
import time
import threading

def long_task2():
    for i in range(5):
        time.sleep(1)
        print('working {} \n'.format(i))

print('Start')

thread = []
for i in range(5):
    t = threading.Thread(target = long_task2())
    thread.append(t)

for t in thread:
    t.start()

print("END")
# ?????
