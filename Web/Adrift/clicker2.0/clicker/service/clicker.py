import sys

from ..app import db
from ..config import Config

clickers = Config.CLICKERS.keys()


class base(object):
    def __init__(self):
        self.name = self.__class__.__name__
        self.value = Config.CLICKERS[self.name]['value']
        self.price = Config.CLICKERS[self.name]['price']
        self.scale = 1.15
        self.max = 10


class momo(base):
    pass


class mgb(base):
    pass


class profk(base):
    pass


class passion(base):
    pass


class hyper(base):
    pass


class bigj(base):
    pass


class ghost(base):
    pass


class tnek(base):
    pass


class captiosus(base):
    pass


def get_all_clickers():
    clicker_list = []
    for clicker in clickers:
        clicker_list.append(get_clicker(clicker))
    return str(clicker_list)


def get_clicker(name):
    thismodule = sys.modules[__name__]
    try:
        clicker_name = getattr(thismodule, name)
    except AttributeError:
        return None
    return clicker_name().__dict__


def get_clicker_field(name, field):
    thismodule = sys.modules[__name__]
    try:
        clicker_name = getattr(thismodule, name)
    except AttributeError:
        return None
    try:
        field_val = getattr(clicker_name(), field)
    except AttributeError:
        return None
    return {field: field_val}
