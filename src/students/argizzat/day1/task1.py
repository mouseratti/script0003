from time import time
import timeit

text = """Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium,
    totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. 
    Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos 
    qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur,
     adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. 
     Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea 
     commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae 
     consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"""
vovels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

def func():
    a = text
    result = {'vowels':{},'consonants':{}}
    la = list(a.lower())
    sa = set(la)
    for i in sa:
        for j in la:
            if i == j:
                if i in vovels:
                    result['vowels'].update({(i, a.count(i))})
                    break
                elif i in consonants:
                    result['consonants'].update({(i, a.count(i))})
                    break
    return result

if __name__ == "__main__":
    print(func())

    # a = 0
    # start = time()
    # while True:
    #     func(text)
    #     a+=1
    #     if a>10000:
    #         break
    # finish = time()
    # print(finish - start)

    r = timeit.Timer(func)
    print(r.timeit(10000))

