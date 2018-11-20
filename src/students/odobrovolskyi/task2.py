import re
import timeit

def search_and_sort(list1, list2):
    return sorted(set(
        [x for x in list1 for y in list2 if re.search(r'\b.*' + re.escape(x) + r'.*\b', y)]), key=lambda s: s.casefold())

def search_and_sort_by_mkoshel(list1, list2):
    result = []
    for elem1 in list1:
        for elem2 in list2:
            if elem1 in elem2:
                result.append(elem1)
                break
    return sorted(result, key=lambda s: s.lower())

a1 = ["arp", "live", "strong", "zzz", "Bill", "Ali", "cow", "boy"]
a2 = ["lively", "alive", "harp", "Billy", "sharp", "armstrong", "Alice", "cowboy"]
a3 = ["tarp", "mice", "bull", "qqq", "ely", "li"]
a4 = ["lively", "alive", "harp", "sharp", "armstrong"]

def f1():
    search_and_sort(a1,a2)
    search_and_sort(a3,a4)
def f2():
    search_and_sort_by_mkoshel(a1, a2)
    search_and_sort_by_mkoshel(a3, a4)


if __name__ == '__main__':
    print(search_and_sort(a1, a2))
    print(search_and_sort(a3, a4))

    assert search_and_sort(a1, a2) == search_and_sort_by_mkoshel(a1, a2)
    assert search_and_sort(a3, a4) == search_and_sort_by_mkoshel(a3, a4)

    t = timeit.Timer(f1)
    print(t.timeit(10000))

    t2 = timeit.Timer(f2)
    print(t2.timeit(10000))
