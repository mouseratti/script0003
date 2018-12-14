
class ClassA:

    param3 = []
    my_args = None
    my_kwargs = None
    __my_property = None
    __my_instance = None

    def __new__(cls, *args, **kwargs):


    def __init__(self, *args,**kwargs):

        self.param3 = []
        self._x = None
        self.my_args = args
        self.my_kwargs = kwargs

    def my_method(self, *args, **kwargs):
        print(args, **kwargs)

    # @property
    # def x(self):
    #     # return None
    #     return self._x
    #
    # @x.setter
    # def x(self, value):
    #     self._x = value

    # x = property

if __name__ == '__main__':

    class_a = ClassA(1,2,3,4,5, x=2)
    print(class_a)
    print(class_a.__dict__)
    print(ClassA.__dict__)
