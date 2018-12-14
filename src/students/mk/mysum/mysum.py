

def my_sum(*args):
    """:returns sum of args"""
    result = 0
    for pos in args: result += pos
    return result