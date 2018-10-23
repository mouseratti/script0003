

def simple_function(*args, **kwargs):
    result =f"im simple_function with {args} {kwargs}"
    print(result)
    return result


def decor(func):
    def wrapper(*args, **kwargs):
        wrapper_result = f"im wrapper with {args} {kwargs}"
        print(wrapper_result)
        func_result = func(*args, **kwargs)
        return '{} {}'.format(wrapper_result, func_result)
    return wrapper



if __name__ == '__main__':
    r1 = simple_function(1,2,3, a=1)
    simple_function = decor(simple_function)
    r2 = simple_function(1,2,3,a=1)
    print("+++++++++++++++")
    print(r1, "\n\n\n", r2)