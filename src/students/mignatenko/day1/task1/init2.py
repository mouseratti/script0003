"""
Вторая версия первого задания. Пробегает по тексту всего 1 раз! И без доп модулей
"""
from students.mignatenko.day1.task1.constants import TEXT, REPEAT_COUNT
import timeit

def func():
    result={'vowels': {},'consonants': {}}
    for l in TEXT.lower():
        if l in 'aeiou':
            if l not in result['vowels'].keys():
                result['vowels'][l] = 1
            else:
                result['vowels'][l] += 1
        if l in 'bcdfghjklmnpqrstvwxyz':
            if l not in result['consonants'].keys():
                result['consonants'][l] = 1
            else:
                result['consonants'][l] += 1
    return result


if __name__ == "__main__":
    # r = timeit.Timer(func)
    # print(r.timeit(REPEAT_COUNT))
    print(func())