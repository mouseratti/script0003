var_a: int = 5


b = "%s %s" % (var_a, 6)
c = "{}".format(var_a)
d = "{PLACEHOLDER}".format(PLACEHOLDER=var_a)
e = f"a is {var_a}"


if __name__ == '__main__':
    [print(_) for _ in (b,c,d,e)]




