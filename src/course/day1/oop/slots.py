class Ordinary: pass



class WithSlots:

    __slots__ = [
        'static_attr1',
        'static_attr2',
    ]



if __name__ == '__main__':
    a = Ordinary()
    b = WithSlots()
    a.__dict__ # {}
   b.__dict__  # AttributeError
    a.static_attr1 = 1
    b.static_attr1 = 1
    a.dynamic_attr = 2
