"""
Первая версия первого задания
"""
from collections import Counter
import timeit
from students.mignatenko.day1.task1.constants import TEXT, REPEAT_COUNT, VOVELS, CONSONANTS



def func():
    result={}
    result['vowels'] = dict(Counter(c for c in TEXT.lower() if c in VOVELS))
    result['consonants'] = dict(Counter(c for c in TEXT.lower() if c in CONSONANTS))
    return result


if __name__ == "__main__":
    r = timeit.Timer(func)
    print(r.timeit(REPEAT_COUNT))
    # print(func())