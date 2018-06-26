

def gen1(obj, args=[]):
    """docstring for gen1"""
    for _ in args:
        yield obj(_)


def fib(n):
    a, b = 0, 1
    lst = []
    for i in range(n):
        lst.append(a)
        a, b = b, a + b
    return lst



def fib_gen(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b



def fib_gen2(n):
    a, b = 0, 1
    lst = []
    for i in range(n):
        lst.append(a)
        a, b = b, a + b
    yield lst