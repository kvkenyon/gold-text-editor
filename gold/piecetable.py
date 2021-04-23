# piecetable.py

from enum import Enum

class PieceTable:

    def __init__(self, original='', pieces=[]): 
        self.__original = original
        self.__added = '' 
        self.__pieces = pieces 

    def insert(self, offset, text):
        piece, piece_offset = self.get_piece_from_offset(offset)
        piece_index = self.pieces.index(piece)
        if piece_offset == 0:
            # append at front
            self.__pieces.insert(piece_index,
                                 Piece(PieceType.ADDED,
                                       start=len(self.added),
                                       length=len(text)))
        elif piece_offset == piece.length:
            # append at end
            self.__pieces.insert(piece_index + 1,
                                 Piece(PieceType.ADDED,
                                       start=len(self.added),
                                       length=len(text)))
        else:
            # middle

            left = Piece(piece_type=piece.piece_type,
                         start=piece.start,
                         length=piece_offset)
            middle = Piece(PieceType.ADDED, start=len(self.added),
                            length=len(text))
            right = Piece(piece_type=piece.piece_type,
                          start=piece_offset,
                          length=piece.length - piece_offset)
            self.__pieces.remove(piece)
            self.__pieces.insert(piece_index, left)
            self.__pieces.insert(piece_index + 1, middle)
            self.__pieces.insert(piece_index + 2, right)
        self.__added += text
    

    def get_contents(self):
        contents = []
        for piece in self.pieces:
            start = piece.start
            end = start + piece.length
            if piece.piece_type == PieceType.ORIGINAL:
                contents.append(self.original[start:end])
            else:
                contents.append(self.added[start:end]) 
        return ''.join(contents)

    def get_piece_from_offset(self, offset):
        'Find the piece that contains the offset.'
        curr_offset = 0 
        curr_piece = None
        piece_offset = -1
        for piece in self.pieces:
            if curr_offset + piece.length >= offset:
                curr_piece = piece
                piece_offset = offset - curr_offset
                break
            else:
                curr_offset += piece.length
                
        return curr_piece, piece_offset

    @classmethod
    def fromfile(cls, filename):
        self = None
        with open(filename, "r") as f:
            lines = f.readlines()
            result = []
            start = 0
            line_starts = [] 
            for line in lines:
                result.append(line)
                line_starts.append(start)
                start += len(line)

            original = ''.join(result)

            piece = Piece(start=0,
                          length=len(original),
                          line_starts=line_starts)

            pieces = [piece] 
            self = cls(original, pieces)

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
    ORIGINAL = 'original' 
    ADDED = 'added' 

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

    def __repr__(self):
        return f'Piece(start={self.__start}, length={self.__length}, line_starts={self.__line_starts}, piece_type={self.__piece_type.value})'
