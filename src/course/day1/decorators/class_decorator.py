from functools import update_wrapper, wraps, lru_cache

#
class Wrapper:
    def __init__(self, func):
        self.func = func
        # update_wrapper(self, func)
        pass

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs) * 2
        pass


class WrapperWithParams(object):
    def __init__(self, multiplier):
        self.multiplier = multiplier
        pass

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * self.multiplier
        return wrapper




# @Wrapper
# def decorated1(i):return i

@WrapperWithParams(3)
def decorated3(i):return i
#
#
@WrapperWithParams(4)
def decorated4(i):return i
#


if __name__ == '__main__':
    # decorated1 = Wrapper(decorated1)
    # print(decorated1(1))

    print(decorated3(1))
    # decorated3 = WrapperWithParams(3)(decorated3)
    # print(fn3(1))
    #
    # fn4 = decorated4
    print(decorated4(1))