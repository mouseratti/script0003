import builtins

# LEGB-rule Local<-Enclosed<-Global<-Builtins
builtins.a = "built-in"


var_b = 'eee'
var_list = []

def enclosed():
    # global var_b
    print(var_b)



if __name__ == '__main__':
    # var_list = [1]
    enclosed()
    print(var_list)