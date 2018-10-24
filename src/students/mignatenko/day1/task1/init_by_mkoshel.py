"""
Первая версия первого задания
"""
from collections import Counter
import timeit

from students.mignatenko.day1.task1.constants import (
    TEXT,
    REPEAT_COUNT,
    VOVELS,
    CONSONANTS,

)


def func():
    lower = TEXT.lower()
    return {
        'vovels': Counter(c for c in lower if c in VOVELS),
        'consonants': Counter(c for c in lower if c in CONSONANTS)
    }
    return result


if __name__ == "__main__":
    # print(func())
    r = timeit.Timer(func)
    print(r.timeit(REPEAT_COUNT))
