import builtins

# LEGB-rule Local<-Enclosed<-Global<-Builtins
builtins.a = "built-in"


var_b = 'eee'

def enclosed():
    global var_b
    print(var_b)
    var_b = 3

if __name__ == '__main__':
    var_b = 'var_b'
    enclosed()
    print(var_b)