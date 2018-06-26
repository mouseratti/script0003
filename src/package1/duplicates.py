def remove_duplicates(l=[]):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    if len(n) == 1:
        return n[0]
    return sorted(n)
