from enum import IntEnum


class Command(IntEnum):
    START = 1
    STEP = 2
    YOUWIN = 3

class State(IntEnum):
    START = 1
    INGAME = 2
    END = 3

class Message:
    command = ""
    row = ""
    column = ""



