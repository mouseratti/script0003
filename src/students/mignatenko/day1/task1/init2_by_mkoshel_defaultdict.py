"""
Вторая версия первого задания. Пробегает по тексту всего 1 раз! И без доп модулей
"""

from students.mignatenko.day1.task1.constants import TEXT, REPEAT_COUNT, CONSONANTS, VOVELS
import timeit
from collections import defaultdict, Counter
from time import time

def func():
    result = {
        'vowels': defaultdict(int),
        'consonants': defaultdict(int),
    }
    for l in TEXT.lower():
        if l in VOVELS: result['vowels'][l] += 1
        if l in CONSONANTS: result['consonants'][l] += 1
    return result


if __name__ == "__main__":
    print(func())
    r = timeit.Timer(func)
    print(r.timeit(REPEAT_COUNT))
    # start = time()
    # print(func())
    # finish = time()
    # print(finish-start)