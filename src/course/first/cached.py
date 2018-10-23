


def f(l=[]):
    l.append(1)
    print(l)



l2 = []


def f2():
    l2.append(1)



if __name__ == '__main__':
    f(); f(); f()
    f2(); f2(); f2()
    print('l2 is {}'.format(l2))