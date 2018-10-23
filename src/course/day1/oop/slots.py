class Ordinary(object): pass


class WithSlots(object):

    __slots__ = [
        'static_attr1',
        'static_attr2',
    ]
if __name__ == '__main__':
    import sys
    global_a = Ordinary()
    b = WithSlots()
    global_a.__dict__ # {}
 #   b.__dict__  # AttributeError
    global_a.static_attr1 = 1
    b.static_attr1 = 1
    global_a.dynamic_attr = 2
  #  b.dynamic_attr = 2  # AttributeError
    print(sys.getsizeof(global_a), sys.getsizeof(b))
