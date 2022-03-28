from types import NoneType

from multipledispatch import dispatch


@dispatch(int, int)
def add(x, y):
    return x + y


@dispatch(int)
def add(x):
    return x


@dispatch(NoneType)
def add(x):
    return 'its None'


@dispatch(object, object)
def add(x, y):
    return "%s + %s" % (x, y)


if __name__ == '__main__':
    print(add(1, 2))
    print(add(1, 'hello'))
    print(add(1))
    print(add(None))
