def add(a, b, c=30):
    return a + b + c


# 位置传参
print(add(10, 20))
# 混合传参
print(add(10, b=20))
# 关键字传参
print(add(a=10, b=20))
print(add(a=10, b=20, c=40))


def add2(x=1):
    x += 1
    print(x)


add2()
add2()
add2()


def add2(x=1):
    x += 1
    print(x)


def add3(x=None):
    if x is None:
        x = []
    x.append(1)
    print(x)


add3()
add3()
add3()


def add4(x=[]):
    x.append(1)
    print(x)


add4()
add4()
add4()
add4()

print(max(1, 2, 3))
