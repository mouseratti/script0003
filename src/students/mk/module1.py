
def func1(string, filename):
    with open(filename, "a") as f:
        f.write(string + '\n')




if __name__ == '__main__':
    FILENAME = "eeeee"
    func("testrun!!!!", FILENAME)