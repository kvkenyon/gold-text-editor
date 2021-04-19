# piecetable.py
from enum import Enum

class PieceTable:

    def __init__(self, original=''): 
        self.__original = original
        self.__added = '' 
        self.__pieces = [] 

    @classmethod
    def fromfile(cls, filename):
        self = cls()
        with open(filename, "r") as f:
            lines = f.readlines()
            result = []
            start = 0
            line_starts = [] 
            for line in lines:
                result.append(line)
                line_starts.append(start)
                start += len(line)

            self.__original = ''.join(result)

            piece = Piece(start=0,
                          length=len(self.__original),
                          line_starts=line_starts)

            self.__pieces.append(piece)        

        return self

    @property
    def original(self):
        return self.__original

    @property
    def added(self):
        return self.__added

    @property
    def pieces(self):
        return self.__pieces

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
