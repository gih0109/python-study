# class types
# 클래스를 타이핑하는 방법


class Hello:
    def world(self) -> int:
        return 7


class World:
    pass


# 인스턴스를 만들 때 타입힌트 쓰는 법
hello: Hello = Hello()  # 변수 옆에 : 클래스명 을 쓰면 된다
# world: World = World()


def foo(ins: Hello) -> int:  # ins : instance
    return ins.world()


print(foo(hello))
# print(foo(world))
