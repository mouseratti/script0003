"""
Первая версия первого задания
"""
from collections import Counter
import timeit
from students.mignatenko.day1.task1.constants import TEXT, REPEAT_COUNT, VOVELS, CONSONANTS



def func():
    result={}
    result['vowels'] = dict(Counter(c for c in TEXT.lower() if c in VOVELS))
    result['consonants'] = dict(Counter(c for c in TEXT.lower() if c in CONSONANTS))
    return result


def simple_function(): return list(range(10))

def simple_gen():
    for x in range(10):
        yield x



def func(x,*args, **kwargs):
    """
    docstring for function func


    """
    print(x)
    print(args[1], args[2])
    print(kwargs)
    kwargs.get("key")
    return 0


def lambdax(x): return x + 1



class A:
    value1 = None


a,b,c = A(), A(), A()




if __name__ == "__main__":
    r = timeit.Timer(func)
    print(r.timeit(REPEAT_COUNT))
    # print(func())