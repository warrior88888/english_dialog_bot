from enum import IntEnum, StrEnum

class ModeChecksEnum(IntEnum):
    relax = 7
    normal = 5
    hard = 3


class ModeLvlEnum(StrEnum):
    relax = "relax"
    normal = "normal"
    hard = "hard"


class EnglishLvlEnum(StrEnum):
    a1 = "a1"
    a2 = "a2"
    b1 = "b1"
    b2 = "b2"
    c1 = "c1"
    c2 = "c2"


class RolesEnum(StrEnum):
    ai = "Bot"
    user = "User"
    msg_split = ' NEXT_STEP '