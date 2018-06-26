
def s0(myList):
    myString=''
    myString=' '.join(myList)
    return myString

def s1(myList):
    myString='' 
    for l in myList: 
        myString+=str(l)
    return myString

def flatten(myList):
    try:
        for subl in myList:
            for el in flatten(subl):
                yield el
    except TypeError:
        yield myList


if __name__ == '__main__':
    myList=['str1', '123', '788']
    print(s0(myList))

    myList=['str1', 123, 788]
    print(s1(myList))

    myList=[[[1],2],3,4,[5,[6,7]],8]
    print(list(flatten(myList)))







