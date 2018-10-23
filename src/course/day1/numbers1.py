

a = ''
b = ""
c = ''''''
d = """"""

assert  a == b == c == d

assert a is b is c is d
id(a) == id(b)

print(id(a), id(b), id(c), id(d))