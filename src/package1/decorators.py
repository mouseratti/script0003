
def cacher(fn):
    cache = {}
    def wrapper(i):
        if i in cache:
            return cache[i]
        cache[i] = fn(i)
        return cache[i]
    return wrapper



