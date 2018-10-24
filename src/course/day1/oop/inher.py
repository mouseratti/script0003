

class A:

    def method1(self, *args, **kwargs):
        print("called method A.method1")
        return 1


class B(A):


    def method1(self, *args, **kwargs):
        print("called method B.method1")
        parent_result = super().method1(*args, **kwargs)
        return parent_result * 2

    def __call__(self, *args, **kwargs):
        print("im callable")

    def __add__(self, other):pass

    def __cmp__(self, other): pass



if __name__ == '__main__':
    b = B()
    b.method1()

    assert callable(b)
    b()
