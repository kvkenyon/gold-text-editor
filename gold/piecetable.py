# piecetable.py
from enum import Enum

class PieceTable:
    pass

class PieceType(Enum):
    ORIGINAL = 0 
    ADDED = 1 

class Piece:
    __slots__ = ('__piece_type',
                 '__start',
                 '__length',
                 '__line_starts')

    def __init__(self, piece_type=PieceType.ORIGINAL,
                 start=0,
                 length=0,
                 line_starts=[]):
        self.__piece_type = piece_type
        self.__start = start
        self.__length = length
        self.__line_starts = line_starts

    @property
    def start(self):
        return self.__start

    @property
    def length(self):
        return self.__length

    @property
    def line_starts(self):
        return self.__line_starts

    @property
    def piece_type(self):
        return self.__piece_type
