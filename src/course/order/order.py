import random
import string
from datetime import datetime

class Order(object):


    def __init__(self, *args, **kwargs):
        self._created_at = datetime.now()
        self._id = ''.join(random.choice(string.ascii_uppercase) for _ in range(20))


    @property
    def id(self):
        return self._id

    @property
    def created_at(self): return self._created_at


    def __lt__(self, other):
        return self.created_at > other.created_at


    def __gt__(self, other):
        return self.created_at < other.created_at


    def __eq__(self, other): return self.created_at == other.created_at