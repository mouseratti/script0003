from time import sleep
class CacheNoLimit:

    def __init__(self, func):
        self.storage = {}
        self.func = func

    def __call__(self, *args):
        if not args in self.storage:
            self.storage[args] = self.func(*args)
        return self.storage[args]



class Cache:

    def __init__(self, size):
        self.storage = {}
        self.size = size

    def __call__(self, func, *args):

        def wrapper(*args):
            if args in self.storage:
                return self.storage[args]
            if len(self.storage) > self.size:
                self.storage.pop(0)
            result = func(*args)
            self.storage[args] = result
            return result
        return wrapper


@Cache(2)
def calculation(a, b):
    sleep(4)
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

