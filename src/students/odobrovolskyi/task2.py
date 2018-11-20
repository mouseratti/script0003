import re

def search_and_sort(list1, list2):
    return sorted(set([x for x in list1 for y in list2 if re.search(r'\b.*' + re.escape(x) + r'.*\b', y)]), key=lambda s: s.casefold())

if __name__ == '__main__':
    a1 = ["arp", "live", "strong", "zzz", "Bill", "Ali", "cow", "boy"]
    a2 = ["lively", "alive", "harp", "Billy", "sharp", "armstrong", "Alice", "cowboy"]
    print(search_and_sort(a1, a2))
    a1 = ["tarp", "mice", "bull", "qqq", "ely", "li"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    print(search_and_sort(a1, a2))
