# 1) Write a python program to convert a list of characters into a string
def list_to_string (l):
    s=''
    for i in l:
        s += i
    return s


# 2)Write a python program to flatten a nested list.
def flatten_nested_list(l):
    new_list = []
    for i in range(0,len(l)):
        if isinstance(l[i], (list, tuple)):
            tmp_list =l[i]
            for j in range(0, len(tmp_list)):
                new_list.append(tmp_list[j])
        elif  isinstance(l[i], dict):
            new_list += list(l[i].values())
        else:
            new_list.append(l[i])
    return new_list


# 3) Write a python function to print a dictionary where the keys are numbers
# between 1 and n (both included) and the values are square of keys. “n” is
# passed as function parameter.
def generate_dict(n):
    my_dict = {}
    for i in range(1,n+1):
        my_dict[i] =i**2
    return my_dict


def generate_dict2(n): return {x:x**2 for x in range(1,n+1)}

def flatten_list2(l, c=[]):
    for elem in l:
        if isinstance(elem, list):
            flatten_list2(elem, c)
        else:
            c.append(elem)
    return c


if __name__ == '__main__':
    d = flatten_nested_list([1,2,3,(7,8,9),{7:'v'}])
    print (d)

    print (generate_dict(10))
    print (list_to_string(('P','r','i','v','e','t')))
