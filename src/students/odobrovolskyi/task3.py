from queue import Queue
class CacheNoLimit:
    storage = dict()

    def __init__(self, func):
        self.func = func
        pass

    def __call__(self, *args, **kwargs):
        key = str(args[0]) + "=" + str(args[1])
        if key in self.storage:
            return self.storage[key]
        else:
            result = self.func(*args, **kwargs)
            self.storage[key] = result
            return result



class Cache(object):
    storage = dict()

    def __init__(self, size):
        self.size = size
        pass

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            key = str(args[0]) + "=" + str(args[1])
            if key in self.storage:
                return self.storage[key]
            else:
                result = func(*args, **kwargs)
                self.storage[key] = result
                if len(self.storage) > self.size:
                    self.storage.pop(list(self.storage.keys())[0])
                return result
        return wrapper


@Cache(2)
def calculation(a, b):
    print(f"invoked calculation for {a}, {b}")
    return a + b


if __name__ == '__main__':
    print(calculation(1, 2))
    print(calculation(1, 2))
    print(calculation(1, 2))

    print(calculation(1, 3))
    print(calculation(1, 3))
    print(calculation(1, 3))

    print(calculation(1, 4))
    print(calculation(1, 4))
    print(calculation(1, 4))

    print(calculation(1, 2))
    print(calculation(1, 4))
    print(calculation(1, 4))
    print(calculation(1, 2))
    print(calculation(1, 2))
    print(calculation(1, 4))

