from re import *


class TestDayOne:

    def count_some_things(self, string: str):
        vowels = 0
        consonants = 0
        for value in string:
            if match("[A-Za-z]+", value):
                if match("[aeiouy]+", value.lower()):
                    vowels += 1
                else:
                    consonants +=1
        return {'vowels': vowels, 'consonants': consonants}

    def test_2(self, a1: list, a2: list):
        result_array = []
        a1.sort()
        for element1 in a1:
            isFound = False
            for element2 in a2:
                if element2.find(element1) != -1:
                    isFound = True
            if isFound:
                result_array.append(element1)
        return result_array


TestDayOne().test_2(["tarp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"])
# TestDayOne().test_2(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"])
# TestDayOne().count_some_things("vowels")


