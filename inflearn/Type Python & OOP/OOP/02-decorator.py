# decorator

# 아래 실행 함수에 저작권 표시를 데코레이터를 이용해서 붙여보기

# 기존 함수 재정의
def copyright(func):  # 함수의 인자로 함수를 받는다
    def new_func():
        print("@ copyright ABC")  # 기존 함수가 실행되기 전 실행된다
        func()  # 기존 함수 실행

    return new_func


@copyright  # 함수 재정의
def smile():
    print("😊")


@copyright
def angry():
    print("😣")


@copyright
def love():
    print("😍")


@copyright
def sad():
    print("😥")


@copyright
def happy():
    print("😄")


@copyright
def soso():
    print("😐")


# 함수 재정의해서 쓰기 -> 일일이 적어넣어야 한다
# smile = copyright(smile)
# angry = copyright(angry)
# love = copyright(love)


# 이모티콘 표시
smile()
angry()
love()
