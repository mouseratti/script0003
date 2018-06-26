
def cacher(fn):
    cache = {}
    def wrapper(i):
        if i in cache:
            # print("returned from cache! {}".format(cache[i]))
            return cache[i]
        cache[i] = fn(i)
        return cache[i]
    return wrapper




# @cacher
@cacher
def return5(x):
    return 5


# return5 = cacher(return5)



if __name__ == '__main__':
    for val in range(5):
        print(return5(val))
    for val in range(5):
        print(return5(val))
