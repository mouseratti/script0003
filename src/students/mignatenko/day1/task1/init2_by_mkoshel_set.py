"""
Вторая версия первого задания. Пробегает по тексту всего 1 раз! И без доп модулей
"""

from students.mignatenko.day1.task1.constants import TEXT, REPEAT_COUNT, CONSONANTS, VOVELS
import timeit
from collections import defaultdict, Counter
from time import time

def func():
    result = {
        'vowels': {},
        'consonants': {},
    }
    lower = TEXT.lower()
    char_set = set(lower)
    for l in char_set:
        if l in VOVELS: result['vowels'][l] = lower.count(l)
        if l in CONSONANTS: result['consonants'][l] = lower.count(l)
    return result


if __name__ == "__main__":
    print(func())
    r = timeit.Timer(func)
    print(r.timeit(REPEAT_COUNT))
    # start = time()
    # print(func())
    # finish = time()
    # print(finish-start)