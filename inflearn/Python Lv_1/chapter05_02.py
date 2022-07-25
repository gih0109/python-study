# Chapter05-2
# 파이썬 사용자 입력
# Input 사용법
# 기본 타입(str)

# 에제 1
name = input("Enter Your Name : ")
grade = input("Enter Your Grade : ")
company = input("Enter Your Company Name : ")
#
print(name, grade, company)

# 아톰에서 터미널 환경을 지원하는 패키지 설치해서 해보는 것도 좋다

# 예제 2
number = input("Enter number : ")
name = input("Enter name : ")

print("type of number", type(number), number *  3)
print("type of name", type(name))

# 에제 3 (계산)
first_number = int(input("Enter number 1 : "))
second_number = int(input("Enter number 2 : "))

total = first_number + second_number
print("first_number + second_number : ", total)

# 에제 4
float_number = float(input("Enter a float number : "))

print("input float : ", float_number)
print("input type : ", type(float_number))

# 예제 5 (print 에서 바로 input 받기)
print("firtstName - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter second name : ")))

# 파이썬 idle 실행해보는 것도 좋음 
