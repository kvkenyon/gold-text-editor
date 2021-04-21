import pytest

from gold.piecetable import PieceTable, Piece, PieceType

@pytest.fixture
def input_file_simple():
    return './tests/data/simple.txt'

# PieceTable Tests
def test_init():
    pt = PieceTable()
    assert pt != None 
    assert isinstance(pt, PieceTable)
    assert pt.original == ''
    assert pt.added == ''
    assert len(pt.pieces) == 0

def test_from_file(input_file_simple):
    pt = PieceTable.fromfile(input_file_simple)
    assert len(pt.pieces) == 1
    piece = pt.pieces[0]
    assert piece.start == 0
    assert piece.length == 44
    assert piece.piece_type == PieceType.ORIGINAL
    assert len(pt.original) == 44
    line_starts = piece.line_starts
    assert len(line_starts) == 2
    assert line_starts[0] == 0
    assert line_starts[1] == 20

def test_get_piece_from_offset():
    piece1 = Piece(start=0, length=20)
    piece2 = Piece(start=0, length=21, piece_type=PieceType.ADDED) 
    piece3 = Piece(start=20, length=24)
    pt = PieceTable(pieces=[piece1, piece2, piece3])
    piece4, po = pt.get_piece_from_offset(20)
    assert piece4 is piece1
    assert po == 20
    piece4, po = pt.get_piece_from_offset(21)
    assert piece4 is piece2
    assert po == 1
    piece4, po = pt.get_piece_from_offset(41)
    assert piece4 is piece2
    assert po == 21
    piece4, po = pt.get_piece_from_offset(63)
    assert piece4 is piece3
    assert po == 22
    
def test_insert_middle(input_file_simple):
    pt = PieceTable.fromfile(input_file_simple)
    print(pt.original)
    assert len(pt.pieces) == 1
    pt.insert(20, "went to the park and\n")
    assert len(pt.pieces) == 3
    assert pt.pieces[0].start == 0
    assert pt.pieces[0].length == 20
    assert pt.pieces[0].piece_type == PieceType.ORIGINAL
    assert pt.pieces[1].start == 0
    assert pt.pieces[1].length == 21
    assert pt.pieces[1].piece_type == PieceType.ADDED
    assert pt.pieces[2].start == 20
    assert pt.pieces[2].length == 24
    assert pt.pieces[2].piece_type == PieceType.ORIGINAL

def test_get_contents_after_insert(input_file_simple):
    print("HELLO")
    pt = PieceTable.fromfile(input_file_simple)
    assert len(pt.pieces) == 1
    pt.insert(20, "went to the park and\n")
    exp = 'the quick brown fox\nwent to the park and\njumped over the lazy dog'
    assert pt.get_contents() == exp

def test_get_contents_after_insert2(input_file_simple):
    pt = PieceTable.fromfile(input_file_simple)
    assert len(pt.pieces) == 1
    pt.insert(1,'a')
    exp = 'tahe quick brown fox\njumped over the lazy dog'
    assert pt.get_contents() == exp
    print(pt.pieces)
    assert len(pt.pieces) == 3 

def test_get_contents_after_insert3(input_file_simple):
    pt = PieceTable.fromfile(input_file_simple)
    assert len(pt.pieces) == 1
    pt.insert(1, 'a')
    pt.insert(1, 'a')
    print(pt.pieces)
    exp = 'taahe quick brown fox\njumped over the lazy dog'
    assert pt.get_contents() == exp
    assert len(pt.pieces) == 4 

def test_get_contents_after_insert4(input_file_simple):
    pt = PieceTable.fromfile(input_file_simple)
    assert len(pt.pieces) == 1
    pt.insert(0, 'unseriousnessbywayofhowtosandhacks\n') 
    print(pt.pieces)
    exp = 'unseriousnessbywayofhowtosandhacks\nthe quick brown fox\njumped over the lazy dog'
    assert pt.get_contents() == exp
    assert len(pt.pieces) == 2 
    
# Piece Tests
def test_construct_piece():
    piece = Piece(piece_type=PieceType.ORIGINAL,
                  start=0,
                  length=10,
                  line_starts=[])
    assert piece.start == 0
    assert piece.length == 10
    assert len(piece.line_starts) == 0
    assert piece.piece_type == PieceType.ORIGINAL

def test_piece_repr():
    p = Piece(start=0, length=44, line_starts=[0,20])
    assert p.__repr__() == 'Piece(start=0, length=44, line_starts=[0, 20], piece_type=original)'

def test_piecetypes():
    original = PieceType.ORIGINAL
    added = PieceType.ADDED
    assert original is PieceType.ORIGINAL
    assert added is PieceType.ADDED
