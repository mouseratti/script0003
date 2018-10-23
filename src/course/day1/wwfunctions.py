# mypy
# PEP-484
a: int = 5

b: str = 6


# def func_a(a: int) -> int:
#     return a +1
#
# func_a("newstring")
#
# if __name__ == '__main__':
#     func_a("a")

#
#
# def func_with_default(a=0):
#     return a +1
#
#
#
# def fullfunc(*args, **kwargs):
#     print("args are {}\nkwargs are {}".format(args, kwargs))
#     print(kwargs.get('b'))
#
#
def func_two_args(arg1 = 0, arg2 = 1):
    return arg1.__add__(arg2)
#
def func_accepting_another_func(f):
    print("calling {}".format(f))
    return f(1, 2)

#
if __name__ == '__main__':
    # func_a()
    # func_with_default()
    # fullfunc(1,2,3,4, a=5, b=6)
    # func_two_args(1, ' ')
    # result = func_accepting_another_func(func_two_args)
    # print(result)
    func_accepting_another_func(lambda x, y: x + y)
