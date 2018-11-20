from collections import Counter, defaultdict

VOVELS = 'aeiou'

TEXT = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore ' \
       'magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea ' \
       'commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat ' \
       'nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit ' \
       'anim id est laborum. '


def countLettersGroupedBySounds(text):
    all_chars = Counter(text)
    result = {"vowels": {}, "consonants": {}}
    for ch in all_chars:
        if ch.lower() in VOVELS:
            result["vowels"][ch] = all_chars[ch]
        else:
            result["consonants"][ch] = all_chars[ch]
    return result


if __name__ == '__main__':
    print(countLettersGroupedBySounds(TEXT))
