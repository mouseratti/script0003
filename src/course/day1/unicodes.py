# https://www.fileformat.info/info/charset/UTF-8/list.htm?start=1024
"""
UNICODE -> BYTES : use .encode()
BYTES -> UNICODE: use .decode()

"""

if __name__ == '__main__':
    latin_string = 'string'
    print(latin_string.encode())
    print(len(latin_string))
    assert (len(latin_string)) == len(latin_string)


    cyr_string = 'строка'
    encoded_cyr_string = cyr_string.encode()
    print(encoded_cyr_string)
    print(len(cyr_string))
    assert (len(encoded_cyr_string)) == len(cyr_string)
    assert encoded_cyr_string.decode() == cyr_string
    win_string = cyr_string.encode('windows-1251')
    print(win_string)
    # win_string.decode()
    # win_string.decode('windows-1251')