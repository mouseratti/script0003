from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple
#from collections import ChainMap
#from collections import Counter





if __name__ == '__main__':
    d = OrderedDict()
    d['one'] = 1
    d['two'] = 2
    d['three'] = 3
    [print(_) for _ in d.keys()]

    dd = defaultdict(list)
    for l in 'veryloooongstringwithUPPERandlovercase':
        dd[l].append(l)
    [print(_, dd.get(_)) for _ in dd]
    ddi  = defaultdict(int)
    ddi.default_factory

    NT = namedtuple("NT", 'field_a, field_b')
    nt = NT
    nt.field_a  = 1
    nt.field_b = 2

