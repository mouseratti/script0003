from time import sleep
import subprocess



class B:

    def get_value(self, inputted):
        result = subprocess.run("ping ya.ru".split(), timeout=10)
        return result.returncode
