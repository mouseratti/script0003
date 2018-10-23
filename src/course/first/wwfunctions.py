


def func_a(a):
    return a +1


def func_with_default(a=0):
    return a +1



def fullfunc(*args, **kwargs):
    print(args, kwargs)


def func_two_args(arg1, arg2):
    print("im func_two_args called with {}".format([arg1, arg2]))
    return arg1 + arg2

def func_accepting_another_func(f):
    print("calling {}".format(f))
    return f(1, 2)


if __name__ == '__main__':
    func_a()
    func_with_default()
    fullfunc(1,2,3,4, a=5, b=6)
    func_accepting_another_func(func_two_args)
    func_accepting_another_func(lambda x, y: x * y )