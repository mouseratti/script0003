import subprocess


if __name__ == '__main__':
    result = subprocess.run('ping ya.ru -c 3', shell=True, capture_output=True)
    result = subprocess.run(
        'ping ya.ru -c 2'.split(),
        stdout=open("eee.log", "a"),
    )
    print(type(result))
    result = subprocess.run(
        'ping ya.ru'.split(),
        timeout=3
    )
    result = subprocess.run("ls -1 | grep log", shell=True, capture_output=True)