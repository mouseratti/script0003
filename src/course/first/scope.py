import builtins

builtins.a = "built-in"


a = "global"

def enclosed():
    a = "enclosed"
    def internal():
        global a
        nonlocal a
        a = "internal"
        print (a)
        return a
    return internal()



if __name__ == '__main__':
    enclosed()
