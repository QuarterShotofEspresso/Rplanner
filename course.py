from enum import Enum

class Quarters(Enum):
    FALL   = 'FALL'
    WINTER = 'WINTER'
    SPRING = 'SPRING'
    SUMMER = 'SUMMER'


class Course:
    def __init__(self, name, cid, avail, pre):
        _name  = name  # string
        _id    = cid   # string
        _avail = avail # list
        _pre   = pre   # list

    def amIPre(crsObj):
        return ( self._id in crsObj._pre )

    def wasHePre(crsObj):
        return ( crsObj._id in self._pre )
