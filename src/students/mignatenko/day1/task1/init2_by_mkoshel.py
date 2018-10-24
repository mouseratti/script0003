"""
Вторая версия первого задания. Пробегает по тексту всего 1 раз! И без доп модулей
"""
from students.mignatenko.day1.task1.constants import TEXT, REPEAT_COUNT, CONSONANTS, VOVELS
import timeit
from collections import defaultdict, Counter


def func():
    result = {
        'vowels': defaultdict(int),
        'consonants': defaultdict(int),
    }
    # result = {
    #     'vowels': Counter(),
    #     'consonants': Counter(),
    # }

    for l in TEXT.lower():
        if l in VOVELS: result['vowels'][l] += 1
        if l in CONSONANTS: result['consonants'][l] += 1
    return result


if __name__ == "__main__":
    r = timeit.Timer(func)
    print(r.timeit(REPEAT_COUNT))
    # print(func())
