import functools

def decor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper_result = f"im wrapper with {args} {kwargs}"
        print(wrapper_result)
        func_result = func(*args, **kwargs)
        return '{} {}'.format(wrapper_result, func_result)
    return wrapper


@decor
def simple_function(*args, **kwargs):
    """ function simple_function
    :returns str
    """
    result =f"im simple_function with {args} {kwargs}"
    print(result)
    return result


if __name__ == '__main__':
    r1 = simple_function(1,2,3, a=1)
    # print(r1)
    simple_function = decor(simple_function)
