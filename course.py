from enum import Enum

class Quarters(Enum):
    FALL = 1
    WINTER = 2
    SPRING = 3
    SUMMER = 4


class Course:
    def __init__(self, name, cid, avail, pre):
        _name  = name  # string
        _id    = cid   # string
        _avail = avail # list
        _pre   = pre   # list
