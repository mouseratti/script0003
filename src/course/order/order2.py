import datetime
import string
import random

class Order(object):

    def __init__(self):
        self._created_at = datetime.datetime.now()
        self._id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
        self._delivery_date = None

    @property
    def id(self):
        return self._id

    @property
    def created_at(self):
        return self._created_at

    def __eq__(self, other):
        return self.created_at == other.created_at

    def __lt__(self, other):
        return self.created_at > other.created_at

    def __gt__(self, other):
        return self.created_at < other.created_at


    
    @delivery_date.setter
    def delivery_date(self, date):
        self.delivery_date = date
