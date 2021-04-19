import pytest

from gold.piecetable import PieceTable, Piece, PieceType


@pytest.fixture
def input_file_simple():
    return './tests/data/simple.txt'

# PieceTable Tests
def test_init(input_file_simple):
    pt = PieceTable()
    assert pt != None 
    assert isinstance(pt, PieceTable)


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

def test_piecetypes():
    original = PieceType.ORIGINAL
    added = PieceType.ADDED

    assert original is PieceType.ORIGINAL
    assert added is PieceType.ADDED


# def test_fromfile():
#     """
#     GIVEN: Given a file, create a PieceTable instance.
#     WHEN: The classmethod fromfile is called.
#     THEN: A new instance of type PieceTable should exist.
#     """
#     piece_table =  PieceTable.from_file('data/simple.txt')
    